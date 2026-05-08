import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")


from flask import Flask, request

app = Flask(__name__)

# Página principal
@app.route('/')
def formulario():
    return '''
    <html>
        <head>
            <title>Login</title>
        </head>
        <body>
            <h2>Ingreso de Usuario</h2>

            <form action="/mostrar" method="post">
                <label>Usuario:</label><br>
                <input type="text" name="usuario"><br><br>

                <label>Clave:</label><br>
                <input type="password" name="clave"><br><br>

                <button type="submit">Ingresar</button>
            </form>
        </body>
    </html>
    '''

# Mostrar datos ingresados
@app.route('/mostrar', methods=['POST'])
def mostrar():
    usuario = request.form['usuario']
    clave = request.form['clave']

    return f'''
    <html>
        <head>
            <title>Datos Ingresados</title>
        </head>
        <body>
            <h2>Datos recibidos</h2>

            <p><b>Usuario:</b> {usuario}</p>
            <p><b>Clave:</b> {clave}</p>

            <br>
            <a href="/">Volver</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
