import matplotlib.pyplot as plt

def show_graph(data):
    edades = [row["Edad"] for row in data]
    bebidas = [row["BebidasSemana"] for row in data]

    plt.bar(edades, bebidas)
    plt.xlabel("Edad")
    plt.ylabel("Bebidas por Semana")
    plt.title("Consumo de Alcohol por Edad")
    plt.show()