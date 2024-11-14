# app.py
import tkinter as tk
from tkinter import ttk, messagebox
from connect_db import load_data
from add_record import add_record
from update_record import update_record
from delete_record import delete_record

def run_app():
    try:
        print("Iniciando la aplicación...")
        root = tk.Tk()
        root.title("Gestión de Encuestas")
        root.geometry("800x600")

        # Menú
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Exportar a Excel")
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=root.quit)

        view_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Ver", menu=view_menu)
        view_menu.add_command(label="Mostrar Gráfico")

        # Crear un Treeview para la tabla
        columns = ["idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"]
        treeview = ttk.Treeview(root, columns=columns, show="headings", height=20)

        # Configurar encabezados y columnas
        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=150)

        # Agregar la tabla a la ventana
        treeview.pack(fill="both", expand=True)

        # Botón para cargar datos
        tk.Button(root, text="Cargar Datos", command=lambda: load_data(treeview)).pack(pady=10)

        # Botones de acción
        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Button(frame, text="Agregar", command=lambda: add_record(treeview)).pack(side="left", padx=5)
        tk.Button(frame, text="Actualizar", command=lambda: update_record(treeview)).pack(side="left", padx=5)
        tk.Button(frame, text="Eliminar", command=lambda: delete_record(treeview)).pack(side="left", padx=5)

        root.mainloop()
        print("Aplicación finalizada.")
    except Exception as e:
        print(f"Error: {e}")

run_app()