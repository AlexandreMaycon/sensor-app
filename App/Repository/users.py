from App.DataBase import get_connection

class Users:
    
    def create_user(name: str, login: str, password: str):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                insert_query = """
                INSERT INTO user (name, login, password)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (name, login, password))
            connection.commit()
        finally:
            connection.close()
            
    def get_user_by_login(login: str):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                get_user = """
                SELECT * FROM user WHERE login = %s
                """
                
                cursor.execute(get_user, login)
                return cursor.fetchone()
        finally:
            connection.close()