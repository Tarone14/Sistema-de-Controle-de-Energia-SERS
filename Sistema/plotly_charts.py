import plotly.graph_objects as go

def prepare_timestamp(df):
    """
    Gera uma coluna 'timestamp' a partir de ano/mes/dia/hora.
    """
    if "timestamp" not in df:
        df["timestamp"] = (
            df["ano"].astype(str) + "-" +
            df["mes"].astype(str).str.zfill(2) + "-" +
            df["dia"].astype(str).str.zfill(2) + " " +
            df["hora"]
        )
    return df


def create_voltage_chart(df):
    df = prepare_timestamp(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["tensao"],
        mode="lines+markers",
        name="Tensão (V)"
    ))

    fig.update_layout(
        title="⚡ Variação de Tensão ao Longo do Tempo",
        xaxis_title="Data e Hora",
        yaxis_title="Tensão (V)",
        template="plotly_white"
    )

    return fig


def create_light_chart(df):
    df = prepare_timestamp(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["brilho"],
        mode="lines+markers",
        name="Brilho (%)"
    ))

    fig.update_layout(
        title="🔆 Intensidade de Luz ao Longo do Tempo",
        xaxis_title="Data e Hora",
        yaxis_title="Brilho (%)",
        template="plotly_white"
    )

    return fig


def create_compare_chart(df):
    df = prepare_timestamp(df)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["tensao"],
        mode="lines",
        name="Tensão (V)"
    ))

    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["brilho"],
        mode="lines",
        name="Brilho (%)"
    ))

    fig.update_layout(
        title="📊 Comparativo — Tensão x Brilho",
        xaxis_title="Data e Hora",
        yaxis_title="Valores",
        template="plotly_white"
    )

    return fig
