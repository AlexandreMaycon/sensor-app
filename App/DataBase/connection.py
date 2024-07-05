import pymysql.cursors

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='challenge',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn