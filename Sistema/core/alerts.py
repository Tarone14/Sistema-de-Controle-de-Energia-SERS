import pandas as pd

def detectar_alertas(df):
    tensao_baixa = df[df["tensao"] < 2.0].assign(alerta="TENSÃO MUITO BAIXA (< 2V)")
    brilho_baixo = df[df["brilho"] < 30].assign(alerta="BRILHO MUITO BAIXO (< 30%)")
    return pd.concat([tensao_baixa, brilho_baixo], ignore_index=True)
