import tkinter as tk
from tkinter import ttk

# Creación ventana
ventana = tk.Tk()

# Asignación tamaño a la ventana
ventana.geometry("600x400")

# Cambiando título
ventana.title("Banco T")

# Botón
enviar = ttk.Button(ventana, text="Enviar")
enviar.pack()

# Ultima línea a ejecutar
ventana.mainloop()

