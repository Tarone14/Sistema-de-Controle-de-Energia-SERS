import streamlit as st

def left_menu():
    return st.sidebar.radio(
        "Menu:",
        ["📈 Gráficos", "📚 Histórico", "⚙ Configurações", "🚨 Alertas"]
    )
