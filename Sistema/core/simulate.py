import numpy as np
from datetime import datetime

def gerar_dado_simulado():
    """
    Gera medições simuladas.
    """
    agora = datetime.now()
    brilho = np.random.uniform(0, 100)
    tensao = np.random.uniform(0, 5)

    return {
        "ano": agora.year,
        "mes": agora.month,
        "dia": agora.day,
        "hora": agora.strftime("%H:%M:%S"),
        "brilho": round(brilho, 2),
        "tensao": round(tensao, 2)
    }
