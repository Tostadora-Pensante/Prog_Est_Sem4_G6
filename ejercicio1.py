def calcular_pago(horas, tarifa):
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)


calcular_pago(40, 120)

# La siguiente instrucción produciría NameError:
print(pago)
#este print(pago) da error porque la variable que se pide era una variable local de la funcion calcular_pago, por ende no existe fuera de la misma.
#Por ende, el programa no la reconoce porque para el es como si no existiera fuera del programa.