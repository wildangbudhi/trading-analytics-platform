from utils import logger_setup, Server

from tasks import scrape_cot_task, scrape_tradingeconomics_task, scrape_investing_technical_summary

logger_setup()
server = Server()
app = server.celery_app

@app.task( name='cot_data_pipeline', autoretry_for=( Exception, ValueError, ), retry_kwargs={ 'max_retries': 10, 'countdown': 5 })
def cot_data_pipeline():
    scrape_cot_task( server=server )

@app.task( name='economics_data_pipeline', autoretry_for=( Exception, ValueError, ), retry_kwargs={ 'max_retries': 10, 'countdown': 5 })
def economics_data_pipeline():
    scrape_tradingeconomics_task( server=server )

@app.task( name='investing_technical_data', autoretry_for=( Exception, ValueError, ), retry_kwargs={ 'max_retries': 10, 'countdown': 5 })
def investing_technical_data():
    scrape_investing_technical_summary( server=server )