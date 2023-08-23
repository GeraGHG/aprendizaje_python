# decoradores
def revisar(func):
    def otra_funcion(a, b):
        if b == 0:
            return "No puedes dividir entre cero"
        return func(a, b)
    return otra_funcion


@revisar
def dividir(a, b):
    return a / b

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def ejecutar_operacion(operacion, a , b):
    return operacion(a, b)


# a(b) -> c
def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print(">>> Antes de la ejecución")
        return funcion_b(*args, **kwargs)
    return funcion_c

@funcion_a
def saludar():
    print("Hola, desde una función!")
saludar()

@funcion_a
def sumar(a, b):
    return a + b
print(sumar(5, 6))