from connect_db import connect_db

def fetch_data(order_by="Edad"):
    connection = connect_db()
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM encuesta ORDER BY {order_by}")
        results = cursor.fetchall()
        connection.close()
        return results
    else:
        return []