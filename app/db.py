#Instalar pymysql (pip install PyMySQL)

#Importar pymysql / SQLalchemy / dbmysql
import pymysql

from dotenv import load_dotenv
import os
# Cargar las variables de entorno desde el archivo .env
load_dotenv()
#Conectar con el servidor MySQL
def conectar_mysql():
    #Datos sensibles, debemos utilizar variables de entorno
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    db = os.getenv('DB_NAME')
    return pymysql.connect(host=host,user=user,password=password,database=db)