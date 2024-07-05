from App.DataBase import get_connection

class Equipaments:
    def get_table() -> str:
        return "equipment" 

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