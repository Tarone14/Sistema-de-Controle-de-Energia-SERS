import streamlit as st
import time


from plotly_charts import (
    create_voltage_chart,
    create_light_chart,
    create_compare_chart
)

# Interface
from ui.layout import left_menu

# Núcleo
from core.simulate import gerar_dado_simulado
from core.storage import salvar_medicao, carregar_historico
from core.filters import filtrar
from core.alerts import detectar_alertas


# Inicialização
st.set_page_config(page_title="Dashboard Solar", layout="wide")


st.title("🔆 Dashboard de Energia Solar — Simulação")

# Estado
if "intervalo" not in st.session_state:
    st.session_state["intervalo"] = 1

# Menu lateral
menu = left_menu()

# =====================================================================
# 📈 GRÁFICOS
# =====================================================================
if menu == "📈 Gráficos":
    st.header("📊 Leituras em Tempo Real")
    placeholder = st.empty()

    for _ in range(40):
        dado = gerar_dado_simulado()
        salvar_medicao(dado)
        df = carregar_historico()

        with placeholder.container():
            col1, col2 = st.columns(2)

            # ----------- NOVO: gráficos Plotly ------------
            with col1:
                st.subheader("🔆 Brilho (%)")
                st.plotly_chart(create_light_chart(df), use_container_width=True)

            with col2:
                st.subheader("⚡ Tensão (V)")
                st.plotly_chart(create_voltage_chart(df), use_container_width=True)

            st.success(
                f"Última leitura → Brilho {dado['brilho']}% | "
                f"Tensão {dado['tensao']} V"
            )

        time.sleep(st.session_state["intervalo"])

# =====================================================================
# 📚 HISTÓRICO
# =====================================================================
elif menu == "📚 Histórico":
    st.header("📚 Histórico de Medições — Busca Avançada")
    df = carregar_historico()

    if df.empty:
        st.warning("Nenhum dado salvo.")
        st.stop()

    anos = ["Todos"] + sorted(df["ano"].unique().tolist())
    ano = st.selectbox("Ano", anos)

    meses = ["Todos"] + sorted(df["mes"].unique().tolist())
    mes = st.selectbox("Mês", meses)

    dias = ["Todos"] + sorted(df["dia"].unique().tolist())
    dia = st.selectbox("Dia", dias)

    brilho = st.slider("Brilho (%)", 0.0, 100.0, (0.0, 100.0))
    tensao = st.slider("Tensão (V)", 0.0, 5.0, (0.0, 5.0))

    h_ini = st.text_input("Hora inicial", "00:00:00")
    h_fim = st.text_input("Hora final", "23:59:59")

    filtrado = filtrar(df, ano, mes, dia, brilho, tensao, h_ini, h_fim)

    st.subheader("Resultados")
    st.dataframe(filtrado)

    st.download_button("📥 Baixar CSV", filtrado.to_csv(index=False), "resultado.csv")

# =====================================================================
# ⚙ CONFIGURAÇÕES
# =====================================================================
elif menu == "⚙ Configurações":
    st.header("⚙ Configurações do Sistema")

    st.session_state["intervalo"] = st.slider(
        "Intervalo entre leituras (segundos)",
        1, 10, st.session_state["intervalo"]
    )

    if st.button("🗑 Limpar histórico"):
        import os
        if os.path.exists("data/medicoes.csv"):
            os.remove("data/medicoes.csv")
        st.success("Histórico removido!")

# =====================================================================
# 🚨 ALERTAS
# =====================================================================
elif menu == "🚨 Alertas":
    st.header("🚨 Alertas Automáticos")
    df = carregar_historico()

    if df.empty:
        st.warning("Nenhum dado disponível.")
    else:
        alertas = detectar_alertas(df)
        st.dataframe(alertas)
        st.error(f"Total de alertas: {len(alertas)}")

