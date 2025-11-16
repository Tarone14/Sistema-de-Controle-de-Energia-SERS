import streamlit as st
import base64

def apply_visual_style(image_path: str):
    """
    Aplica imagem de fundo + caixas brancas translúcidas para o conteúdo.
    """

    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
    }}

    .stMarkdown, .stDataFrame, .stTextInput, .stSelectbox,
    .stPlotlyChart, .stButton, .stNumberInput, .stRadio,
    .stCheckbox, .stDownloadButton, .stDateInput {{
        background: rgba(255, 255, 255, 0.83) !important;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 12px;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
