import pymysql
from db import conectar_mysql

#CRUD Create / Read / Update / Delete

#GET OBTENER READ productos
def obtener_productos():
    #Conexión a MySQL
    conexion = conectar_mysql()
    # Creamos una variable para almacenar los productos
    productos = []
    #Consulta
    with conexion.cursor() as cursor:
        #Sentencia SQL para la consulta
        sql = """SELECT * 
        FROM `productos`"""
        #Ejecuta la consulta SQL
        cursor.execute(sql)
        #Almacena en la variable los datos obtenidos de la consulta mediante la función fetchAll que transforma todos los datos en algo legible
        productos = cursor.fetchall()
        #Comiteamos los cambios en la BD
        conexion.commit()
        #Cerramos la conexion a la DB
        conexion.close()
        #Devolvemos el resultado de la consulta
        return productos

#POST CARGAR CREATE producto
def cargar_producto(nombre, descripcion, precio):
    #Conexión a MySQL
    conexion = conectar_mysql()
    #Consulta
    with conexion.cursor() as cursor:
        #Sentencia SQL para la consulta de INSERT almacenada en la variable query
        query = """INSERT INTO productos (nombre, descripcion, precio) VALUES
          (%s,%s,%s) """
        #Ejecuta la consulta SQL y le pasa los parámetros del producto
        cursor.execute(query, (nombre, descripcion, precio))
        #Guardamos el resultado en "resultado"
        resultado = cursor
        #Comiteamos los cambios en la BD
        conexion.commit()
        #Cerramos la conexion a la DB
        conexion.close()
        #Devolvemos el resultado de la consulta
        return resultado
    
#PUT EDITAR UPDATE productos
#Creamos una función para obtener un producto por ID
def obtener_prod_id(id):
    #Conexión a MySQL
    conexion = conectar_mysql()
    # Creamos una variable para almacenar el producto
    producto = None
    #Consulta
    with conexion.cursor() as cursor:
        #Sentencia SELECT para obtener el producto por ID
        query = """SELECT * 
        FROM `productos`
        WHERE id=%s"""
        #Ejecuta la consulta SQL pasando el parámetro query con la consulta y el parámetro del ID
        cursor.execute(query,(id))
        #Almacena en la variable el dato obtenido del producto
        producto = cursor.fetchone()
        #Comiteamos los cambios en la BD
        conexion.commit()
        #Cerramos la conexion a la DB
        conexion.close()
        #Devolvemos el resultado de la consulta
        return producto
    
#Creamos la función para editar el producto por id
def editar_producto(nombre, descripcion, precio,id):
    #Conexión a MySQL
    conexion = conectar_mysql()
    #Consulta
    with conexion.cursor() as cursor:
        #Sentencia SQL para la consulta de UPDATE almacenada en la variable query
        query = """UPDATE productos 
        SET nombre = %s, descripcion = %s, precio = %s
        WHERE id = %s"""
        #Ejecuta la consulta SQL y le pasa los parámetros del producto
        cursor.execute(query, (nombre, descripcion, precio,id))
        #Guardamos el resultado en "resultado"
        resultado = cursor
        #Comiteamos los cambios en la BD
        conexion.commit()
        #Cerramos la conexion a la DB
        conexion.close()
        #Devolvemos el resultado de la consulta
        return resultado
    
def eliminar_producto(id):
    conexion = conectar_mysql()
    with conexion.cursor() as cursor:
        #Sentencia SQL para la consulta de DELETE almacenada en la variable query
        query = """DELETE FROM productos WHERE id = %s"""
        #Ejecuta la consulta SQL y le pasa los parámetros del producto
        cursor.execute(query, (id))
        #Guardamos el resultado en "resultado"
        resultado = cursor
        #Comiteamos los cambios en la BD
        conexion.commit()
        #Cerramos la conexion a la DB
        conexion.close()
        #Devolvemos el resultado de la consulta
        return resultado
