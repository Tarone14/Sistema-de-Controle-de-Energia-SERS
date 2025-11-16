import os
import pandas as pd

CSV_FILE = "data/medicoes.csv"

def salvar_medicao(dado):
    df = pd.DataFrame([dado])

    # Cria pasta data/ caso não exista
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, index=False)
    else:
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)

def carregar_historico():
    if not os.path.exists(CSV_FILE):
        return pd.DataFrame(columns=["ano","mes","dia","hora","brilho","tensao"])
    return pd.read_csv(CSV_FILE)
