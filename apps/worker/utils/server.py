from sqlalchemy import create_engine , Engine
import os
from celery import Celery

class Server():

    def __init__( self ):

        self.db_conn = self.__init_db_conn()
        self.celery_app = self.__init_celery()

    def __init_db_conn( self ) -> Engine:
        
        conn_string = os.getenv( "DB_CONN_STRING" )

        if not conn_string:
            raise ValueError("env DB_CONN_STRING not found")
        
        db = create_engine(conn_string) 
        # conn = db.connect() 
        
        return db

    def __init_celery( self ) -> Celery:
        
        broker_url = os.getenv( "BROKER_URL" )
        backend_url = os.getenv( "BACKEND_URL" )

        return Celery('DistributedTask', broker=broker_url, backend=backend_url)


    def close(self):
        self.db_conn.close()