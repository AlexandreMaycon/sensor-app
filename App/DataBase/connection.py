import pymysql.cursors
import os
from dotenv import load_dotenv

def get_connection():
    load_dotenv()
    
    conn = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'),
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn