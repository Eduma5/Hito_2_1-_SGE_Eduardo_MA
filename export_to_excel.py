import pandas as pd

def export_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("encuestas.xlsx", index=False)
    print("Datos exportados a encuestas.xlsx")