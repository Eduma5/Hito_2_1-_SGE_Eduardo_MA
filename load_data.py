from tkinter import messagebox
from connect_db import connect_db

def load_data(treeview):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM encuesta")
        rows = cursor.fetchall()
        for row in rows:
            treeview.insert("", "end", values=row)
        connection.close()
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")
def export_data():
    # Implementación de export_data
    pass

def show_data_graph():
    # Implementación de show_data_graph
    pass

def update_record(table):
    # Implementación de update_record
    pass

def delete_record(table):
    # Implementación de delete_record
    pass