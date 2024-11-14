from connect_db import connect_db

def filter_data(condition):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM encuesta WHERE {condition}"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows