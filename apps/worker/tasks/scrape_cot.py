import pandas as pd
import requests
from bs4 import BeautifulSoup
import calendar
import time
import re
from sqlalchemy import create_engine 
from sqlalchemy.sql import text
import logging

from utils import Server

def scrape_cot_task( server: Server ):
    
    try:
        scrape_cot( server=server, url='https://www.cftc.gov/dea/futures/deacmesf.htm' )
        scrape_cot( server=server, url='https://www.cftc.gov/dea/futures/deanybtsf.htm' )
    except:
        return False
    
    return True

def scrape_cot( server: Server, url: str):

    conn = server.db_conn.connect()

    logging.info(f"[Scrape COT] Scrape Data - {url}")

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    val = soup.body.pre.text
    val = val.replace( "--------------------------------------------------------------| NONREPORTABLE", "" )
    val = val.replace( "      NON-COMMERCIAL      |   COMMERCIAL    |      TOTAL      |   POSITIONS", "" )
    val = val.replace( "--------------------------|-----------------|-----------------|-----------------", "" )
    val = val.replace( "  LONG  | SHORT  |SPREADS |  LONG  | SHORT  |  LONG  | SHORT  |  LONG  | SHORT", "" )
    val = val.replace( "--------------------------------------------------------------------------------", "" )
    val = val.replace( "|", "" )

    res = []

    selected_exchange = ''
    selected_date = ''
    data_id = 0

    for v in val.splitlines():
        v = v.lstrip().rstrip()
        v = re.sub( ' +', ' ', v )

        if v == '':
            continue

        if data_id > 3:
            selected_exchange = ''
            selected_date = ''
            data_id = 0

        if 'EXCHANGE' in v or 'ICE FUTURES U.S.' in v :
            selected_exchange = v.split(' - ')[0]
        
        if 'FUTURES ONLY POSITIONS AS OF ' in v:
            selected_date = v.replace( 'FUTURES ONLY POSITIONS AS OF ', '' )
        
        if re.match(r"^[\d ,-.]*$", v):
            data = v.replace(",", "")
            data = data.split(' ')
            data = [selected_date, selected_exchange, str(data_id)] + data
            res.append(data)
            data_id += 1

    logging.info("[Scrape COT] Process Data")

    cols = [ 
        'date', 
        'exchange', 
        'data_type', 

        'non_com_long', 
        'non_com_short', 
        'non_com_spreads', 
        
        'com_long', 
        'com_short', 

        'total_long', 
        'total_short',

        'non_reportable_long', 
        'non_reportable_short', 
    ]

    df = pd.DataFrame(res, columns=cols)
    df = df.replace( '.', None )
    df[ cols[3:] ] = df[ cols[3:] ].astype('float64')

    df['date'] = pd.to_datetime( df['date'], format='%m/%d/%y' )

    df['data_type'] = df['data_type'].replace( {
        '0' : 'COMMITMENTS',
        '1' : 'CHANGES',
        '2' : 'PERCENT OF OPEN INTEREST',
        '3' : 'NUMBER OF TRADERS',
    } )

    df['ts'] = calendar.timegm( time.gmtime() )

    logging.info("[Scrape COT] Write to Raw Table")

    res = df.to_sql(
        name='bronze__cftc__commitment_of_traders',
        schema='public',
        con=conn,
        if_exists='append',
        index=False
    )

    logging.info( f"[Scrape COT] Write to Raw Table -> {res}")

    logging.info("[Scrape COT] ETL Silver Table")

    sqlquery = """
    insert into public.silver__cftc__commitment_of_traders

    select
        md5(
            concat(
                "date"::varchar,
                exchange,
                data_type
            )::varchar
        ) as surr_key,
        "date",
        exchange,
        data_type,
        non_com_long,
        non_com_short,
        non_com_spreads,
        com_long,
        com_short,
        total_long,
        total_short,
        non_reportable_long,
        non_reportable_short,
        ts
    from
        public.bronze__cftc__commitment_of_traders
    where
        ts = (
            select max(ts)
            from public.bronze__cftc__commitment_of_traders
        )

    on conflict (surr_key) do update set
        "date" = excluded."date",
        exchange = excluded.exchange,
        data_type = excluded.data_type,
        non_com_long = excluded.non_com_long,
        non_com_short = excluded.non_com_short,
        non_com_spreads = excluded.non_com_spreads,
        com_long = excluded.com_long,
        com_short = excluded.com_short,
        total_long = excluded.total_long,
        total_short = excluded.total_short,
        non_reportable_long = excluded.non_reportable_long,
        non_reportable_short = excluded.non_reportable_short,
        ts = excluded.ts
    """

    conn.execute( text( sqlquery ) )
    conn.commit()
    
    conn.close()