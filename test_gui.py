import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Tabla en Tkinter")

# Crear un Treeview para la tabla
tabla = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")

# Configurar las cabeceras de la tabla
tabla.heading("col1", text="Nombre")
tabla.heading("col2", text="Edad")
tabla.heading("col3", text="Ciudad")

# Configurar el tamaño de las columnas
tabla.column("col1", width=100)
tabla.column("col2", width=50, anchor="center")
tabla.column("col3", width=100)

# Agregar datos a la tabla
datos = [
    ("Eduardo", 19, "Madrid"),
    ("Adrián", 22, "Sevilla"),
    ("Marcos", 20, "Barcelona"),
    ("Andrés", 23, "Valencia"),
]

for dato in datos:
    tabla.insert("", "end", values=dato)

# Colocar la tabla en la ventana
tabla.pack(pady=20)

# Iniciar el bucle de eventos
root.mainloop()