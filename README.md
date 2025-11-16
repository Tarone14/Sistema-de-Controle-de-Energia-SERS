# Sistema-de-Controle-de-Energia-SERS
Um programa que analisa padrões de tensão energética saindo de uma estação de placas solares, e avalia a eficiência marcando flutuações grandes no fluxo.

**Dashboard Solar — Guia Completo de Instalação e Uso**

Este projeto é um Dashboard Interativo em Streamlit para monitoramento de um sistema solar simulado.
Ele mostra gráficos de brilho e tensão, gera dados automáticos, salva histórico em CSV, detecta alertas e permite filtros avançados.

Ideal para:

- estudos de IoT

- demonstrações de interface de sensores

- projetos educacionais

- monitoramento simulado de energia

# Pré-requisitos:

Certifique-se de ter instalado:

  Python 3.10+

-> Passo 1:

Para utilizá-lo, você precisará criar um ambiente virtual, há duas maneiras de se fazer isto.

Opção 1: Se você estiver utilizando o programa PyCharm, ele criará o ambiente virtual sozinho no mesmo diretório em que você rodar o programa pela primeira vez.

Opção 2: Digite no termial do seu programa de código:

  python -m venv .venv
  
E depois:

  .venv\Scripts\activate

-> Passo 2: 

Instale os pacotes requeridos para o funcionamento do programa no seu ambiente virtual.

Escreva no terminal do seu programa de código:

  pip install -r requirements.txt

Espere a instalação.

-> Pronto!

Agora o programa está prontamente instalado

Para rodar digite no terminal do seu programa:

  streamlit run app.py
