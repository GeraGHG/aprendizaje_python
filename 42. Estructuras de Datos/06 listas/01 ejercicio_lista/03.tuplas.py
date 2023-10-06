meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def funcion():
     sesion = False
     while not sesion:
        numero = int(input(f"Ingresa un número entre 1 y {len(meses)}: "))
        if 0 <= numero <= len(meses):
            print(meses[numero - 1])
        else:
            print(" Adios ".center(50, "-"))
            sesion = True

funcion()






