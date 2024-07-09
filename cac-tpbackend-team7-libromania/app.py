from flask import Flask, render_template, request, redirect, session, flash, get_flashed_messages
from flask_mysqldb import MySQL
from datetime import datetime
from flask import send_from_directory
import os
from functools import wraps
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "develoteca"
mysql = MySQL()

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sitio'

mysql.init_app(app)

# Decorador de verificación de sesión
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
            return redirect('/admin/login')
        return f(*args, **kwargs)
    return decorated_function

""" INICIO """
@app.route('/')
def inicio():
    conexion = mysql.connect
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `libros`")
    libros = cursor.fetchall()
    conexion.commit()
    return render_template('sitio/index.html', libros=libros)

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('templates/sitio/img'), imagen)

""" REGISTRO """
@app.route('/registro')
def registro():
    return render_template('sitio/registro.html')

""" ADMIN INDEX """
@app.route('/admin/')
@login_required
def admin_index():
    return render_template('admin/index.html')

""" LOGIN """
@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    _usuario = request.form['txtUsuario']
    _password = request.form['txtPassword']
    
    if _usuario == 'Sergio' and _password == '123':
        session["login"] = True
        session["usuario"] = "sergio"
        return redirect("/admin")
        
    return render_template('admin/login.html')

@app.route('/admin/libros')
@login_required
def admin_libros():
    conexion = mysql.connect
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `libros`")
    libros = cursor.fetchall()
    conexion.commit()
    return render_template("admin/libros.html", libros=libros)

@app.route('/admin/libros/guardar', methods=['POST'])
@login_required
def admin_libros_guardar():
    # Contar la cantidad de libros actuales
    conexion = mysql.connect
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM `libros`")
    cantidad_libros = cursor.fetchone()[0]
    
    # Verificar si se pueden agregar más libros (límite de 12)
    if cantidad_libros >= 10:
        flash('No se pueden agregar más libros. Límite alcanzado.', 'error')
        return redirect('/admin/libros')
    
    # Continuar con la inserción del libro
    _nombre = request.form['txtNombre']
    _who = request.form['txtWHO']
    _archivo = request.files['txtImagen']
    
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%Y%m%d%H%M%S')
    
    if _archivo.filename != "":
        nuevoNombre = horaActual + "_" + secure_filename(_archivo.filename)
        rutaArchivo = os.path.join("templates/sitio/img", nuevoNombre)
        _archivo.save(rutaArchivo)
    else:
        nuevoNombre = ''  # Opcional: asignar un valor por defecto si no se proporciona imagen
    
    sql = "INSERT INTO `libros` (`nombre`, `imagen`, `who`) VALUES (%s, %s, %s);"
    datos = (_nombre, nuevoNombre, _who)
    
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    
    return redirect('/admin/libros')

@app.route('/admin/libros/borrar', methods=['POST'])
@login_required
def admin_libros_borrar():
    _id = request.form['txtID']
    
    conexion = mysql.connect
    cursor = conexion.cursor()
    cursor.execute("SELECT imagen FROM `libros` WHERE id = %s", (_id,))
    libro = cursor.fetchall()
    conexion.commit()
    
    if os.path.exists('templates/sitio/img/' + str(libro[0][0])):
        os.unlink('templates/sitio/img/' + str(libro[0][0]))
    
    cursor.execute("DELETE FROM `libros` WHERE id = %s", (_id,))
    conexion.commit()
    
    return redirect('/admin/libros')

@app.route('/admin/libros/editar/<int:id>')
@login_required
def admin_libros_editar(id):
    conexion = mysql.connect
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM `libros` WHERE id = %s", (id,))
    libro = cursor.fetchone()
    conexion.commit()
    return render_template('admin/editar_libro.html', libro=libro)

@app.route('/admin/libros/actualizar', methods=['POST'])
@login_required
def admin_libros_actualizar():
    _id = request.form['txtID']
    _nombre = request.form['txtNombre']
    _who = request.form['txtWHO']
    _archivo = request.files['txtImagen']
    
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%Y%m%d%H%M%S')
    
    conexion = mysql.connection
    cursor = conexion.cursor()
    
    if _archivo.filename != "":
        nuevoNombre = horaActual + "_" + _archivo.filename
        rutaArchivo = os.path.join("templates/sitio/img", nuevoNombre)
        _archivo.save(rutaArchivo)
        
        # Actualizar con nueva imagen
        sql = "UPDATE `libros` SET nombre = %s, imagen = %s, who = %s WHERE id = %s;"
        datos = (_nombre, nuevoNombre, _who, _id)
        
        # Eliminar la imagen antigua
        cursor.execute("SELECT imagen FROM `libros` WHERE id = %s", (_id,))
        libro = cursor.fetchone()
        if os.path.exists('templates/sitio/img/' + str(libro[0])):
            os.unlink('templates/sitio/img/' + str(libro[0]))
    else:
        # Actualizar sin cambiar la imagen
        sql = "UPDATE `libros` SET nombre = %s, who = %s WHERE id = %s;"
        datos = (_nombre, _who, _id)
    
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    
    return redirect('/admin/libros')

@app.route('/admin/logout')
def admin_logout():
    session.pop('login', None)
    session.pop('usuario', None)
    return redirect('/admin/login')

if __name__ == '__main__':
    app.run(debug=True)
