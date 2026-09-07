""" 
operaciones basicas:
suma, resta, multiplicacion y division
"""
def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1*number2

def div(number1, number2):
    try:
        return number1/number2
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    except TypeError:
        return "Tipo de dato incorrecto, debe ingresar un numero"

