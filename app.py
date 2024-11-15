import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from connect_db import load_data, connect_db
from add_record import add_record
from update_record import update_record
from delete_record import delete_record
from filter_data import filter_data
import matplotlib.pyplot as plt
import pandas as pd

filtered_data = []
current_filter = "Sin filtro aplicado"


def apply_filter(treeview, field, order, value):
    global filtered_data, current_filter
    if field == "Edad" or field == "idEncuesta":
        condition = f"1=1 ORDER BY {field} {order}"
        current_filter = f"Ordenado por {field} en orden {'ascendente' if order == 'ASC' else 'descendente'}"
    elif field == "Sexo":
        condition = f"Sexo = '{value}'"
        current_filter = f"Filtrado por sexo: {value}"
    else:
        condition = "1=1"
        current_filter = "Sin filtro aplicado"

    filtered_data = filter_data(condition)

    for row in treeview.get_children():
        treeview.delete(row)
    for row in filtered_data:
        treeview.insert("", "end", values=row)


def export_to_excel():
    try:
        if filtered_data:
            filepath = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
                title="Guardar archivo como"
            )
            if filepath:
                df = pd.DataFrame(filtered_data, columns=[
                    "idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                    "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol",
                    "ProblemasDigestivos", "TensionAlta", "DolorCabeza"
                ])
                df.to_excel(filepath, index=False)
                messagebox.showinfo("Éxito", f"Datos exportados a {filepath}")
        else:
            messagebox.showinfo("Información", "No hay datos filtrados para exportar")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al exportar los datos: {e}")


def show_graph():
    if filtered_data:
        df = pd.DataFrame(filtered_data, columns=[
            "idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
            "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol",
            "ProblemasDigestivos", "TensionAlta", "DolorCabeza"
        ])
        edades = df['Edad'].value_counts().index.tolist()
        counts = df['Edad'].value_counts().values.tolist()

        # Crear el gráfico
        plt.figure(figsize=(10, 6))
        bars = plt.bar(edades, counts, color='skyblue', edgecolor='black')

        # Etiquetas en las barras
        for bar, count in zip(bars, counts):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5,
                     str(count), ha='center', va='bottom', fontsize=10, color='black')

        # Títulos y etiquetas
        plt.xlabel('Edad', fontsize=12)
        plt.ylabel('Cantidad de Encuestados', fontsize=12)
        plt.title('Distribución de Edades en Encuestas', fontsize=14, weight='bold')

        # Añadir información del filtro
        plt.figtext(0.5, -0.05,
                    f"Datos mostrados bajo el filtro aplicado: {current_filter}",
                    wrap=True, horizontalalignment='center', fontsize=10)

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("Información", "No hay datos filtrados para mostrar en el gráfico")


def on_closing(root):
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        root.destroy()


def run_app():
    try:
        print("Iniciando la aplicación...")
        root = tk.Tk()
        root.title("Gestión de Encuestas")
        root.geometry("800x600")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Helvetica', 12), padding=10, background='#4CAF50', foreground='white')
        style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), background='#4CAF50', foreground='white')
        style.configure('Treeview', font=('Helvetica', 10), background='#f0f0f0', foreground='black',
                        fieldbackground='#f0f0f0')

        root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))

        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Exportar a Excel", command=export_to_excel)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=lambda: on_closing(root))

        view_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Ver", menu=view_menu)
        view_menu.add_command(label="Mostrar Gráfico", command=show_graph)

        columns = ["idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                   "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol",
                   "ProblemasDigestivos", "TensionAlta", "DolorCabeza"]
        treeview = ttk.Treeview(root, columns=columns, show="headings", height=20)

        for col in columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=150)

        treeview.pack(fill="both", expand=True)

        ttk.Button(root, text="Cargar Datos", command=lambda: load_data(treeview)).pack(pady=10)

        frame = ttk.Frame(root)
        frame.pack(pady=10)

        ttk.Button(frame, text="Agregar", command=lambda: add_record(treeview)).pack(side="left", padx=5)
        ttk.Button(frame, text="Actualizar", command=lambda: update_record(treeview)).pack(side="left", padx=5)
        ttk.Button(frame, text="Eliminar", command=lambda: delete_record(treeview)).pack(side="left", padx=5)

        filter_frame = ttk.Frame(root)
        filter_frame.pack(pady=10)

        ttk.Label(filter_frame, text="Campo de Filtro:").pack(side="left", padx=5)
        filter_field = ttk.Combobox(filter_frame, values=["Edad", "Sexo", "idEncuesta"])
        filter_field.pack(side="left", padx=5)

        order_combobox = ttk.Combobox(filter_frame, values=["ASC", "DESC"])
        order_combobox.pack(side="left", padx=5)

        value_combobox = ttk.Combobox(filter_frame, values=["Hombre", "Mujer"])
        value_combobox.pack(side="left", padx=5)

        def on_filter():
            field = filter_field.get()
            if field in ["Edad", "idEncuesta"]:
                order = order_combobox.get()
                apply_filter(treeview, field, order, None)
            elif field == "Sexo":
                value = value_combobox.get()
                apply_filter(treeview, field, None, value)

        ttk.Button(filter_frame, text="Aplicar Filtro", command=on_filter).pack(side="left", padx=5)

        root.mainloop()
        print("Aplicación finalizada.")
    except Exception as e:
        print(f"Error: {e}")


run_app()
