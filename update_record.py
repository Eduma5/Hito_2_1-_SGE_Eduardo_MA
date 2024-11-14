import tkinter as tk
from tkinter import simpledialog, messagebox
from connect_db import connect_db

def update_record(table):
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Selecciona un registro para actualizar")
        return

    item = table.item(selected_item)
    idEncuesta = item["values"][0]

    edad = simpledialog.askinteger("Input", "Nueva Edad:", initialvalue=item["values"][1])
    sexo = simpledialog.askstring("Input", "Nuevo Sexo:", initialvalue=item["values"][2])
    bebidasSemana = simpledialog.askinteger("Input", "Nuevas Bebidas por Semana:", initialvalue=item["values"][3])
    problemasDigestivos = simpledialog.askstring("Input", "Nuevos Problemas Digestivos:", initialvalue=item["values"][4])

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE encuesta SET Edad=%s, Sexo=%s, BebidasSemana=%s, ProblemasDigestivos=%s WHERE idEncuesta=%s",
                       (edad, sexo, bebidasSemana, problemasDigestivos, idEncuesta))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Registro actualizado exitosamente")
        table.item(selected_item, values=(idEncuesta, edad, sexo, bebidasSemana, problemasDigestivos))
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")