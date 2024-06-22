from selenium.webdriver.common.by import By
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2

# Configuração das opções do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Obtém o caminho do ChromeDriver usando ChromeDriverManager
chrome_driver_path = ChromeDriverManager().install()

# Configura o serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializa o driver do Chrome com as opções configuradas e o serviço
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/finance/quote/USD-BRL?sa=X&sqi=2&ved=2ahUKEwjHod2jweyEAxV4LrkGHTzSCNsQmY0JegQIDhAv")


valor_element = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[4]/div/main/div[2]/div[1]/c-wiz/div/div[1]/div/div[1]/div/div[1]/div/span/div/div")

valor_texto = valor_element.text.replace(',','.')

conexao_config = {
    'host': 'pg-90576f9-germinare-8711.e.aivencloud.com',
    'database': 'dbrpa',
    'user': 'avnadmin',
    'password': 'AVNS_5dJlXy00wwa8j288Qme',
    'port':'15864'
}

print(valor_texto)

conexao = psycopg2.connect(**conexao_config)

cursor = conexao.cursor()

consulta = f"CALL inserir_cotacao_dolar('{datetime.datetime.today().date()}', '{datetime.datetime.today().time()}', {float(valor_texto)})"

cursor.execute(consulta)

conexao.commit()

cursor.execute("SELECT * FROM cotacao_dolar;")
records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
conexao.close()

print(f"Inserido com sucesso\nData: {datetime.datetime.today().date()} - Hora:  {datetime.datetime.today().time()} - Valor {float(valor_texto)}")
