# Curso de Análise e Desenvolvimento de Sistemas - UNISENAC - 2024/1

# Rastreio de Pessoas com OpenCV

Este projeto utiliza OpenCV para rastrear pessoas em um vídeo e contar quantas pessoas passam por um determinado ponto.

## Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

## Instalação

Siga as etapas abaixo para instalar as dependências necessárias:

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/ThomasMBG120/visao-computacional.git
   cd visao-computacional

# Crie um ambiente virtual:

python3 -m venv venv
source venv/bin/activate   

# No Windows use `venv\Scripts\activate`

# Instale as dependências:

pip install numpy opencv-contrib-python

# Utilização

Coloque seu arquivo de vídeo na pasta do projeto.

Edite o script rastreio.py e altere 'seu_video.mp4' para o nome do seu arquivo de vídeo.

Execute o script:

python rastreio-mercadocaixa/rastreio.py

# Problemas Comuns

**Erro ao abrir o arquivo de vídeo:** Certifique-se de que o caminho do vídeo está correto e que o vídeo está no formato compatível.

**Importação de módulos:** Certifique-se de que as bibliotecas foram instaladas no ambiente virtual correto.