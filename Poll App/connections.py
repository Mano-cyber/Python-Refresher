import os
import pyscopg2

def create_connection():
    return pyscopg2.connect(os.environ.get("DATABASE_URL"))