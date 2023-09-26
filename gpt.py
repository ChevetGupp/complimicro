import pandas as pd
import mysql.connector
import numpy as np

# Configurações de conexão com o banco de dados MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "test",
}

# Nome da planilha que você deseja importar
nome_planilha = "Controle NFES.ods"

# Ler a planilha usando o pandas
df = pd.read_excel(nome_planilha)

# Função para inserir dados no banco de dados
def inserir_dados_na_db(row):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Exemplo de como inserir dados em uma tabela chamada 'plan'
        query = "INSERT INTO plan (OS, CHAVES, versao, QTD, NFE, OFFICE, officever, officech, MAQ, officeqtd, officenfe) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (str(row["OS"]), str(row["CHAVES"]), str(row["VERSÃO"]), str(row["QTD"]), str(row["NFE"]), str(row["OFFICE"]), str(row["VERSÃO.1"]), str(row["CHAVES.1"]), str(row["MAQ"]), str(row["QTD.1"]), str(row["NFE.1"]))

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")

# Iterar sobre as linhas do DataFrame e inserir cada linha no banco de dados
for index, row in df.iterrows():
    inserir_dados_na_db(row)

print("Dados inseridos no banco de dados com sucesso!")
print(df.columns)
