# Usar uma imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar as dependências do sistema
RUN apt-get update && \
    apt-get install -y wget gnupg unzip

# Instalar o Chrome e o ChromeDriver
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y /tmp/chrome.deb && \
    rm /tmp/chrome.deb

# Baixar e instalar o ChromeDriver
RUN CHROMEDRIVER_VERSION=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/bin && \
    rm /tmp/chromedriver.zip && \
    chmod +x /usr/bin/chromedriver

# Copiar o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install -r requirements.txt

# Copiar o script Python para o contêiner
COPY rpa.py .

# Definir a variável de ambiente para evitar problemas com o Chrome
ENV DISPLAY=:99

# Executar o script Python
CMD ["python", "rpa.py"]
