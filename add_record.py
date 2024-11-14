import tkinter as tk
from tkinter import simpledialog, messagebox
from connect_db import connect_db

def add_record(table):
    idEncuesta = simpledialog.askinteger("Input", "ID Encuesta:")
    edad = simpledialog.askinteger("Input", "Edad:")
    sexo = simpledialog.askstring("Input", "Sexo:")
    bebidasSemana = simpledialog.askinteger("Input", "Bebidas por Semana:")
    problemasDigestivos = simpledialog.askstring("Input", "Problemas Digestivos:")

    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO encuesta (idEncuesta, Edad, Sexo, BebidasSemana, ProblemasDigestivos) VALUES (%s, %s, %s, %s, %s)",
                       (idEncuesta, edad, sexo, bebidasSemana, problemasDigestivos))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Registro agregado exitosamente")
        table.insert("", "end", values=(idEncuesta, edad, sexo, bebidasSemana, problemasDigestivos))
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")