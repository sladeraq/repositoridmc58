import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

# Programa simple con interfaz gráfica usando Tkinter
# Pide usuario y clave, y al presionar el botón muestra los datos ingresados

import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al presionar el botón
def mostrar_datos():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    messagebox.showinfo(
        "Datos ingresados",
        f"Usuario: {usuario}\nClave: {clave}"
    )

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Login Web")
ventana.geometry("300x200")

# Etiqueta Usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)

# Caja de texto Usuario
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

# Etiqueta Clave
label_clave = tk.Label(ventana, text="Clave:")
label_clave.pack(pady=5)

# Caja de texto Clave (oculta caracteres)
entry_clave = tk.Entry(ventana, show="*")
entry_clave.pack(pady=5)

# Botón
boton = tk.Button(
    ventana,
    text="Ingresar",
    command=mostrar_datos
)
boton.pack(pady=15)

# Ejecutar ventana
ventana.mainloop()
