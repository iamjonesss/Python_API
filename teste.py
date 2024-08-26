import pymysql

# Substitua pelos valores corretos
host = 'viaduct.proxy.rlwy.net'
port = 3306
user = 'root'
password = 'XnTTpOEYXbCykZoWGwEnUihNChwMbmLW'
database = 'railway'

try:
    connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
    print("Conexão bem-sucedida!")
    connection.close()
except pymysql.MySQLError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")