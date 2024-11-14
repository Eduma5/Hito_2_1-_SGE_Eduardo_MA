import mysql.connector
from tkinter import messagebox

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="curso",
            database="encuestas"
        )
        print("Conexión exitosa")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return None

def load_data(treeview):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ENCUESTA")
            rows = cursor.fetchall()
            if not rows:
                messagebox.showinfo("Información", "No se encontraron datos en la tabla ENCUESTA")
            for row in rows:
                treeview.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al cargar los datos: {err}")
        finally:
            connection.close()
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")