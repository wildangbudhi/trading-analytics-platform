import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
import calendar
import time

from utils import Server
from sqlalchemy.sql import text

def scrape_tradingeconomics_task( server: Server ):

    try:
        logging.info("[Scrape Trading Economics] Task Starting")

        countries_code = [ "united-states", "euro-area", "united-kingdom", "australia", "new-zealand", "canada", "switzerland", "japan", "indonesia" ]
        now_ts = calendar.timegm( time.gmtime() )

        for c_code in countries_code:
            scrape_tradingeconomics( server=server, country_code=c_code, now_ts=now_ts )

        logging.info("[Scrape Trading Economics] ETL Silver Table")

        conn = server.db_conn.connect()

        sqlquery = """
        insert into public.silver__tradingeconomics__country_economics_data

        select
            md5(
                concat(
                    a.country_code,
                    a.category,
                    a.metrics,
                    a.last_data_date
                )::varchar
            ) as surr_key,
            a.country_code,
            a.category,
            a.metrics,
            a.last,
            a.previous,
            a.highest,
            a.lowest,
            a.unit,
            a.last_data_date,
            a.ts
        from 
            public.bronze__tradingeconomics__country_economics_data a
        where
            a.ts = (
                select max(x.ts)
                from public.bronze__tradingeconomics__country_economics_data x
            )

        on conflict (surr_key) do update set
            country_code = excluded.country_code,
            category = excluded.category,
            metrics = excluded.metrics,
            last = excluded.last,
            previous = excluded.previous,
            highest = excluded.highest,
            lowest = excluded.lowest,
            unit = excluded.unit,
            last_data_date = excluded.last_data_date,
            ts = excluded.ts
        """

        conn.execute( text( sqlquery ) )
        
        conn.commit()
        conn.close()

        logging.info("[Scrape Trading Economics] Task Done")
    except Exception as e:
        raise Exception( f"[Scrape Trading Economics] Failed - {str(e)}" )

def scrape_tradingeconomics( server: Server, country_code: str, now_ts: int ):

    url = f'https://tradingeconomics.com/{country_code}/indicators'

    logging.info( f"[Scrape Trading Economics] {url}" )

    header = {
        "User-Agent": "PostmanRuntime/7.32.3",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Host": "tradingeconomics.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find_all("div", {"role": "tabpanel"})

    final_res = None

    for child in table:

        tag_id = child.get('id')

        if tag_id == 'overview':
            continue

        table = StringIO(str(child))
        table.seek(0)
        table_df = pd.read_html(table)
        
        for df in table_df:
            df.columns = [ 'metrics', 'last', 'previous', 'highest', 'lowest', 'unit', 'last_data_date' ]
            df['category'] = tag_id
            df['country_code'] = country_code
            df['last_data_date'] = pd.to_datetime( df['last_data_date'], format='%b/%y' )
            df = df[[ 'country_code', 'category', 'metrics', 'last', 'previous', 'highest', 'lowest', 'unit', 'last_data_date' ]]
            df.loc[ :,'ts' ] = now_ts

            if final_res is None:
                final_res = df
            else:
                final_res = pd.concat( [ final_res, df ] )
    
    logging.info( f"[Scrape Trading Economics] write result to bronze table" )

    conn = server.db_conn.connect()

    res = final_res.to_sql(
        name='bronze__tradingeconomics__country_economics_data',
        schema='public',
        con=conn,
        if_exists='append',
        index=False
    )
    
    logging.info( f"[Scrape Trading Economics] write result to bronze table - {res}" )

    conn.commit()
    conn.close()
