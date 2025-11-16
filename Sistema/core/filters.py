def filtrar(df, ano, mes, dia, brilho_range, tensao_range, h_ini, h_fim):
    filtrado = df.copy()

    # Data
    if ano != "Todos": filtrado = filtrado[filtrado["ano"] == ano]
    if mes != "Todos": filtrado = filtrado[filtrado["mes"] == mes]
    if dia != "Todos": filtrado = filtrado[filtrado["dia"] == dia]

    # Brilho
    filtrado = filtrado[
        (filtrado["brilho"] >= brilho_range[0]) &
        (filtrado["brilho"] <= brilho_range[1])
    ]

    # Tensão
    filtrado = filtrado[
        (filtrado["tensao"] >= tensao_range[0]) &
        (filtrado["tensao"] <= tensao_range[1])
    ]

    # Horas
    filtrado = filtrado[
        (filtrado["hora"] >= h_ini) &
        (filtrado["hora"] <= h_fim)
    ]

    return filtrado
