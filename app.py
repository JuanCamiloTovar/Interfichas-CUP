from flask import Flask, render_template,flash, request, redirect, url_for, get_flashed_messages
from config_db import ConfigDB
from models_db import db
import pymysql

app = Flask(__name__)
app.secret_key = 'secretkey'

app.config.from_object(ConfigDB)
db.init_app(app)

with app.app_context():
    db.create_all()


def conexion():
    return pymysql.connect(host='localhost',user='root',passwd='290307',db='interfichas', charset='utf8mb4')

# ---------------------------
# RUTAS PARA LA PAGINA WEB
# ---------------------------

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/equipos', methods=['GET'])
def equipos():
    try:
        conn = conexion()
        cur = conn.cursor()
        cur.execute('SELECT * FROM lista_equipos')
        equipos = cur.fetchall()
        lista = []
        
        for equipo in equipos:
            dato = {
                'id' : equipo[0],
                'ficha' : equipo[1],
                'equipo' : equipo[2],
                'jornada' : equipo[3]
            }
            lista.append(dato)
        print(lista)
        return render_template('equipos.html', lista=lista)
    except Exception as error:
        print(error)

@app.route('/partidos', methods=['GET'])
def partidos():
    return render_template('Partidos.html')

@app.route('/tabla', methods=['GET'])
def tabla():
    try:
        conn = conexion()
        cur = conn.cursor()
        cur.execute('SELECT * FROM lista_equipos')
        equipos = cur.fetchall()
        lista = []
        
        for equipo in equipos:
            dato = {
                'id' : equipo[0],
                'ficha' : equipo[1],
                'equipo' : equipo[2],
                'jornada' : equipo[3],
                'estado': equipo[4]
            }
            lista.append(dato)
        print(lista)
        return render_template('Tabla.html', lista=lista)
    except Exception as error:
        print(error)


# ---------------------------
# RUTAS PARA LA PAGINA WEB
# ---------------------------

@app.route('/login', methods =['GET','POST'])
def login():
    try:
        if request.method == 'POST':  
            username = request.form['username']
            password = request.form['pass']

            conn = conexion()
            cur = conn.cursor()
            cur.execute('SELECT * from users where username = %s', (username))
            user = cur.fetchone()
            conn.close()
            cur.close()
            if user:
                if password == user[2]:
                    return redirect(url_for('dashboard', username = username))
                else:
                    flash('La contraseña es incorrecta...', "error")
                    return render_template('login.html')
            else:
                flash('Usuario no encontrado...', "error")
                return render_template('login.html')
        else:
            return render_template('login.html')
    except Exception as err:
        flash('Error al conectar con la base de datos')
        print(err)


# RUTA PARA INGRESAR USUARIOS NUEVOS

@app.route('/users', methods = ['GET', 'POST'])
def users():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['pass']
            print(username)
            print(password)
            conn = conexion()
            cur = conn.cursor()
            cur.execute('INSERT INTO users (username,password) VALUES (%s,%s)', (username,password))
            conn.commit()
            flash('Usuario registrado con exito...', "success")
            conn.close()
            cur.close()
            return redirect(url_for('login'))
        else:
            return render_template('registro_users.html')
    except Exception as err:
        flash('Error al conectar con la base de datos...')
        print(err)

@app.route('/dashboard/<username>', methods = ['GET','POST'])
def dashboard(username):
    try: 
        
        conn = conexion()
        cur = conn.cursor()
        cur.execute('SELECT * FROM lista_equipos')
        datos = cur.fetchall()
        lista = []
        conn.close()
        cur.close()
        for dato in datos:
            equipo = {
                'id' : dato[0],
                'ficha' : dato[1],
                'equipo' : dato[2],
                'jornada' : dato[3], 
                'estado' : dato[4]
                }
            lista.append(equipo)
        print(lista)
        return render_template('dashboard.html', username=username, lista=lista)
    except Exception as err:
        flash('Error al conectar con la base de datos', "error")
        print(err)

@app.route('/registrar', methods=['GET','POST'])
def registrar_equipos():
    try:
        if request.method == 'POST':
            
            equipo = request.form['equipo']
            ficha = request.form['ficha']
            jornada = request.form['jornada']
            estado = request.form['estado']
            
            conn = conexion()
            cur = conn.cursor()
            cur.execute('INSERT INTO lista_equipos (equipo,ficha,jornada,estado) VALUES (%s,%s,%s,%s)', (equipo,ficha,jornada,estado) )
            conn.commit()
            flash('Equipo regitrado exitosamente', 'success')
            conn.close()
            cur.close()
            return redirect(url_for('dashboard', username = 'hola'))
        else:
            return render_template('registrar_equi.html')
    except Exception as err:
        flash('Error al conectar con la base de datos...', 'error')
        print(err)

@app.route('/actualizar/<int:id>', methods = ['GET','POST'])
def actualizar_equipos(id):
    try:
        if request.method == 'POST':
            
            equipo = request.form['equipo']
            ficha = request.form['ficha']
            jornada = request.form['jornada']
            estado = request.form['estado']
            
            conn = conexion()
            cur = conn.cursor()
            cur.execute('UPDATE lista_equipos SET equipo = %s, ficha = %s, jornada = %s, estado = %s WHERE id = %s',
                        (equipo,ficha,jornada,estado,id))
            conn.commit()
            flash('Equipo actualizado correctamente', 'success')
            conn.close()
            cur.close()
            
            return redirect( url_for('dashboard', username = 'hola') )
        else:
            return render_template('actualizar_equi.html')
        
    except Exception as err:
        flash('Error al conectar con la base de datos', 'error')
        print(err)

@app.route('/eliminar/<int:id>', methods = ['GET','POST'])
def eliminar_equi(id):
    try:
        conn = conexion()
        cur = conn.cursor()
        cur.execute('DELETE FROM lista_equipos WHERE id = %s',
                    (id))
        conn.commit()
        flash('Equipo eliminado correctamente', 'success')
        conn.close()
        cur.close()
        return redirect(url_for('dashboard', username = 'hola'))
    except Exception as err:
        flash('Error al conectar con la base de datos...', 'error')
        print(err)


if __name__ == '__main__':
    app.run(debug=True)