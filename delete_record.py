import tkinter as tk
from tkinter import messagebox
from connect_db import connect_db

def delete_record(table):
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Selecciona un registro para eliminar")
        return

    item = table.item(selected_item)
    idEncuesta = item["values"][0]

    if messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este registro?"):
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM encuesta WHERE idEncuesta=%s", (idEncuesta,))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Registro eliminado exitosamente")
            table.delete(selected_item)
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")