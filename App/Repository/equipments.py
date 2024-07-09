from App.DataBase import get_connection

class Equipments:

    def create_equipment_data(equipment_id: str, timestamp: str, value: str):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                insert_query = """
                INSERT INTO equipment (equipmentId, timestamp, value)
                VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (equipment_id, timestamp, value))
            connection.commit()
        finally:
            connection.close()
    
    def get_by_date(period: str):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                get_equipment = """
                SELECT * FROM equipment WHERE timestamp <= %s
                """
                
                cursor.execute(get_equipment, period)
                return cursor.fetchall()
        finally:
            connection.close()
        