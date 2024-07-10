from flask import Flask, render_template, request, redirect
from data import personas
from datetime import date, datetime
from controller_db import obtener_productos, cargar_producto, obtener_prod_id, editar_producto, eliminar_producto

app = Flask(__name__)

#Obtener datos de tiempo actual
def basicInfo(getTitle):
    #Día actual
    hoy = date.today()
    #Fecha y hora actual
    now = datetime.now()
    #Sección
    title = getTitle
    return [title, hoy.strftime("%Y"), now]

#home > root
@app.route("/")
def hello_world():
    title = "Home"
    # return saludo
    return render_template("home.html", title=basicInfo(title))

@app.route("/contacto")
def cargarContacto():
    title ="Contacto"
    users = ["Marcelo","Emanuel","Stephanie","Miguel","Marisa","Julian"]
    return render_template("contacto.html", title=basicInfo(title), users=users)

@app.route("/staff")
def cargarStaff():
    title ="Staff"
    return render_template("staff.html", title=basicInfo(title), personas=personas)
@app.route("/staff/<int:id>")
def cargarPersona(id):
    title ="Persona"
    return render_template("persona.html", title=basicInfo(title), persona=personas[id])

@app.route("/tienda")
def cargarTienda():
    title ="Tienda"
    productos = obtener_productos()
    return render_template("tienda.html", title=basicInfo(title), productos= productos)

#Carga la ruta para acceder al formulario para crear un nuevo producto
@app.route("/cargar_prod", methods=["GET"])
def cargarNuevoProducto():
    title="Cargar Nuevo Producto"
    return render_template("form_nuevo_prod.html", title=basicInfo(title))
#Se envían los datos del nuevo producto por el método POST
@app.route("/insertar_prod", methods=["POST"])
def insertarNuevoProducto():
    print(request.form)
    #Guardamos en variables los datos obtenidos de los inputs del form de productos
    title_prod = request.form["nombre"]
    descripcion_prod = request.form["descripcion"]
    precio_prod = request.form["precio"]
    #Llamamos a la función en el controller y le pasamos los datos obtenidos del form y lo almacenamos en un resultado
    resultado = cargar_producto(title_prod,descripcion_prod,precio_prod)
    #Hacemos un print de lo enviado
    print(resultado)
    #Redireccionamos a una ruta
    return redirect("/tienda")

#Carga la ruta para acceder al formulario para editar un nuevo producto
@app.route("/editar_producto/<int:id>")
def editarProducto(id):
    title="Editar Nuevo Producto"
    prod_id= obtener_prod_id(id)
    return render_template("form_editar_prod.html", title=basicInfo(title),producto=prod_id)
#Se envían los datos del nuevo producto por el método POST
@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    print(request.form)
    #Guardamos en variables los datos obtenidos de los inputs del form de productos
    id_prod = request.form["id_prod"]
    title_prod_edit = request.form["nombre_edit"]
    descripcion_prod_edit = request.form["descripcion_edit"]
    precio_prod_edit = request.form["precio_edit"]
    #Llamamos a la función en el controller y le pasamos los datos obtenidos del form y lo almacenamos en un resultado
    resultado = editar_producto(title_prod_edit,descripcion_prod_edit,precio_prod_edit,id_prod )
    #Hacemos un print de lo enviado
    print(resultado)
    #Redireccionamos a una ruta
    return redirect("/tienda")

@app.route("/borrar_producto/<int:id>")
def borrar_producto(id):
    eliminar_producto(id)
    return redirect("/tienda")