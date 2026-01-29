import pandas as pd
from dotenv import load_dotenv
from loggers import logger
import os
import psycopg2
from psycopg2.extras import execute_values

class sql_runner:
    @logger.catch()
    def __init__(self):
        load_dotenv()
        self.db_user = os.getenv("dbuser")
        self.db_password = os.getenv("dbpassword")
        self.db_name = os.getenv("dbname")
        self.host_name="localhost"
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.host_name,
                port="5439"
            )
            self.cur = self.connection.cursor()
            logger.success("Database Connection Established Successfully")

        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            raise e        

    @logger.catch()
    def sql(self, query: str) -> pd.DataFrame:
        df=pd.DataFrame()
        try:
            df=pd.read_sql_query(query, self.connection)
            logger.info(f"Query: {query}")
            logger.success("SQL Query Executed Successfully")
        except Exception as e:
            logger.error(f"Error running SQL query: {e}")
        else:
            return df
            
    @logger.catch()
    def send_sql(self, query: str, params= None):
        try:
            if params is None:
                self.cur.execute(query)
            else:
                execute_values(self.cur, query, params)
            self.connection.commit()
            logger.info(f"Query: {query} | Params: {params}")
            logger.success("SQL Query Executed Successfully")
        except Exception as e:
            logger.error(f"Error running SQL query: {e}")
            raise e
            
    @logger.catch()
    def __enter__(self): 
        return self

    @logger.catch()
    def __exit__(self, exc_type, exc_value, traceback): 
        if self.connection: 
            self.cur.close() 
            self.connection.close() 
            logger.info("Database connection closed")

