import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Banco T")

def evento_bottom_enviar():
    enviar.config(text="Mensaje enviado")
    mensaje_envidado = ttk.Button(ventana, text="Credenciales correctas")
    mensaje_envidado.pack()

enviar = ttk.Button(ventana, text="Enviar", command=evento_bottom_enviar)
enviar.pack()

ventana.mainloop()