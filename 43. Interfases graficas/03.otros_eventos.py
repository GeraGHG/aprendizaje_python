import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

def mostrar_texto():
    texto = entrada.get()
    print(texto)

boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack()

area = tk.Text(ventana)
area.pack()

def mostrar_texto_area():
    area_text = entrada.get("1.0", tk.END)
    print(area_text)

boton2 = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto_area)
boton2.pack()

)

ventana.mainloop()