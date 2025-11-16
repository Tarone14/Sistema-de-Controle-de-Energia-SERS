import plotly.graph_objects as go

def preparar_tempo(df):
    # Garante coluna timestamp
    if "timestamp" not in df:
        df["timestamp"] = (
            df["ano"].astype(str) + "-" +
            df["mes"].astype(str).str.zfill(2) + "-" +
            df["dia"].astype(str).str.zfill(2) + " " +
            df["hora"]
        )
    return df


def grafico_brilho(df):
    df = preparar_tempo(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["brilho"],
        mode="lines+markers",
        name="Brilho (%)"
    ))

    fig.update_layout(
        title="🔆 Brilho ao Longo do Tempo",
        xaxis_title="Data / Hora",
        yaxis_title="Brilho (%)",
        template="simple_white"
    )
    return fig


def grafico_tensao(df):
    df = preparar_tempo(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["tensao"],
        mode="lines+markers",
        name="Tensão (V)"
    ))

    fig.update_layout(
        title="⚡ Tensão ao Longo do Tempo",
        xaxis_title="Data / Hora",
        yaxis_title="Tensão (V)",
        template="simple_white"
    )
    return fig
