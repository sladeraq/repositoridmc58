import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")


# app.py
# Servidor web simple usando solo librerías nativas de Python

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

HOST = "localhost"
PORT = 8080

class MiServidor(BaseHTTPRequestHandler):

    def do_GET(self):
        # Página con formulario
        html = """
        <html>
        <head>
            <title>Login</title>
        </head>
        <body>
            <h2>Ingreso</h2>

            <form method="POST">
                Usuario:<br>
                <input type="text" name="usuario"><br><br>

                Contraseña:<br>
                <input type="password" name="clave"><br><br>

                <input type="submit" value="Enviar">
            </form>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def do_POST(self):
        # Leer datos enviados
        longitud = int(self.headers['Content-Length'])
        datos = self.rfile.read(longitud).decode()

        parametros = parse_qs(datos)

        usuario = parametros.get("usuario", [""])[0]
        clave = parametros.get("clave", [""])[0]

        respuesta = f"""
        <html>
        <head>
            <title>Datos recibidos</title>
        </head>
        <body>
            <h2>Datos ingresados</h2>

            Usuario: {usuario}<br>
            Contraseña: {clave}
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(respuesta.encode())

# Iniciar servidor
print(f"Servidor iniciado en http://{HOST}:{PORT}")

servidor = HTTPServer((HOST, PORT), MiServidor)
servidor.serve_forever()
