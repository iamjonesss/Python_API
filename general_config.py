# Carregamento do Dotenv
from dotenv import load_dotenv
load_dotenv(override=True)

# Importação de bibliotecas
import os
from flask import Flask
from src.database.class_BD.connection import SQL_Connection

# Inicialização do Flask
app = Flask(__name__)

# Classe que irá servir para exportar a conexão com o banco de dados
conn = SQL_Connection(username=os.getenv('USERNAME'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'), port=os.getenv('PORT'), database=os.getenv('DATABASE'))