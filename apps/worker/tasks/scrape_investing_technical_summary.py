import logging

import pandas as pd
from io import StringIO
import calendar
import time

import cfscrape 
from utils import Server
from sqlalchemy.sql import text

def scrape_investing_technical_summary( server: Server ):

    url = 'https://www.investing.com/currencies/service/Technical?pairid=0&sid=0.43038804868640823&smlID=1053843&category=Technical&download=true'

    logging.info( f"[Scrape Investing - Technical Summary] {url}" )

    header = {
        "User-Agent": "PostmanRuntime/7.36.0",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Host": "www.investing.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie" : 'ses_id=MH4%2Bf2FuZW0%2Fe2BmYTAyMGMzMG5lYWZnNTxjZWFlZ3Fnc2ZoM2Q2cDM8OXcwMzUpNT0%2BN2FmN2w3MmVhMzBiNDA8PmxhNWVsP2hgbGE3MjVjYDBtZWFmYjVlY2JhYGdoZzVmNDNkNjIzbDlnMGw1bTUnPiJhJTcmN2VlNTNyYiUwPz5%2FYTJlbz89YGhhYzJkYzowbmUwZmY1YWNiYWVnf2cs;; __cf_bm=5TmOorDJc_hdTayFnWWQMl5.A3uhwUcU8sqw.fGPu7k-1704726873-1-ATTA+Q8MgpsfDXOoVZvsA7KyWdqcGmmzh2r5ULtWyk5wdjUIpff0NVkyVd7d3q2d+OdgKxvFoL+qv8I4uCX1DU0=; firstUdid=0; ses_id=OXcyc2JtMzthJW5oYjMwMmU1Mmw1MTY3ND1vaTo%2BMCY4LDQ6NmFmID8wOnQ3NDUpNDYyYTEyYTRlZmNqY2I1ZDk4MjJiZjNpYWNuN2JgMDNlMTI6NTI2PDQ3b206PDA8OD00MzYwZmE%2FazpgN281aTQmMi4xdWFwZTdjM2MiNXI5NjJzYjIzamE%2BbjFiMDAzZTIyPTVhNjY0MG8%2FOmgwKDhz; smd=76255e3e0971adec3c1a70387f8122bc-1704725687; udid=76255e3e0971adec3c1a70387f8122bc; PHPSESSID=n150mn95o8kea6p0mqf5op76pn; __cflb=0H28vY1WcQgbwwJpSw5YiDRSJhpofbwYfyEth4cKBFJ; upa=eyJpbnZfcHJvX2Z1bm5lbCI6IiIsIm1haW5fYWMiOiI4IiwibWFpbl9zZWdtZW50IjoiMiIsImRpc3BsYXlfcmZtIjoiMTEyIiwiYWZmaW5pdHlfc2NvcmVfYWNfZXF1aXRpZXMiOiIzIiwiYWZmaW5pdHlfc2NvcmVfYWNfY3J5cHRvY3VycmVuY2llcyI6IjUiLCJhZmZpbml0eV9zY29yZV9hY19jdXJyZW5jaWVzIjoiOCIsImFjdGl2ZV9vbl9pb3NfYXBwIjoiMSIsImFjdGl2ZV9vbl9hbmRyb2lkX2FwcCI6IjAiLCJhY3RpdmVfb25fd2ViIjoiMSIsImludl9wcm9fdXNlcl9zY29yZSI6IjAifQ%3D%3D'
    }

    scraper = cfscrape.create_scraper() 
    scraped_data = scraper.get(url, headers=header) 

    now_ts = calendar.timegm( time.gmtime() )
    
    df = pd.read_csv( StringIO( scraped_data.text ) )
    df.columns = [ 'pair', 'hourly', 'daily', 'weekly', 'monthly' ]
    df.loc[ :,'ts' ] = now_ts

    conn = server.db_conn.connect()

    res = df.to_sql(
        name='bronze__investing__technical_summary',
        schema='public',
        con=conn,
        if_exists='append',
        index=False
    )
    
    logging.info( f"[Scrape Investing - Technical Summary] write result to bronze table - {res}" )

    logging.info("[Scrape Investing - Technical Summary] ETL Silver Table")

    sqlquery = """
    insert into public.silver__investing__technical_summary

    select
        md5(
            concat(
                pair
            )::varchar
        ) as surr_key,
        pair,
        hourly,
        daily,
        weekly,
        monthly,
        ts
    from
        public.bronze__investing__technical_summary
    where
        ts = (
            select max(ts)
            from public.bronze__investing__technical_summary
        )

    on conflict (surr_key) do update set
        pair = excluded.pair,
        hourly = excluded.hourly,
        daily = excluded.daily,
        weekly = excluded.weekly,
        monthly = excluded.monthly,
        ts = excluded.ts
    """

    conn.execute( text( sqlquery ) )

    logging.info("[Scrape Investing - Technical Summary] ETL Silver Table -  Done")

    conn.commit()
    conn.close()

# scrape_investing_technical_summary()