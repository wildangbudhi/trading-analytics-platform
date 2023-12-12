from utils import logger_setup, Server

from tasks import scrape_cot_task

logger_setup()
server = Server()
app = server.celery_app

@app.task(name='cot_data_pipeline')
def cot_data_pipeline():
    return scrape_cot_task( server=server )