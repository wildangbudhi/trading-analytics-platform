import schedule
import os
import time
from celery import Celery

import logging
import sys

def logger_setup():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

logger_setup()

print('Application started')

broker_url = os.getenv( "BROKER_URL", 'redis://localhost:6379/0' )
backend_url = os.getenv( "BACKEND_URL", 'redis://localhost:6379/1' )

celery_app = Celery(
    'DistributedTask',
    broker=broker_url,
    backend=backend_url,
)

def submit_task( name: str ):
    logging.info( f"[Scheduler] Submit Task {name}" )
    celery_app.send_task( name=name )

# schedule.every().day.at("05:00", "Asia/Jakarta").do( submit_task, name='cot_data_pipeline' )
# schedule.every().day.at("05:00", "Asia/Jakarta").do( submit_task, name='economics_data_pipeline' )

schedule.every().hour.at(":00", "Asia/Jakarta").do( submit_task, name='cot_data_pipeline' )
schedule.every().hour.at(":00", "Asia/Jakarta").do( submit_task, name='economics_data_pipeline' )

while True:
    schedule.run_pending()
    time.sleep(1)
