import aritmetica as arit

def menu():
    print("Bienvenidos a mi calculadora")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("0.Salir")
    op = int(input("Digite el # de la opcion que desea usar: "))
    return op

def showAdd(num1,num2):
    print(f"El resultado de la suma de {num1} + {num2} es: {arit.add(num1,num2)}")

def showSubs(num1,num2):
    print(f"La diferencia de {num1} - {num2} es: {arit.substract(num1,num2)}")

def showMult(num1,num2):
    print(f"El resultado de la multiplicacion de {num1} * {num2} es: {arit.mult(num1,num2)}")

def showDiv(num1,num2):
    print(f"El resultado de la division de {num1} / {num2} es: {arit.div(num1,num2)}")

def readValues():
    num1 = float(input("Digite el primer valor: "))
    num2 = float(input("Digite el segundo valor: "))
    return num1,num2

def chooseOp(op):
    if op == 1:
        num1,num2 = readValues()
        showAdd(num1,num2)
    elif op ==2:
        num1,num2 = readValues()
        showSubs(num1,num2)
    elif op ==3:
        num1,num2 = readValues()
        showMult(num1,num2)
    elif op ==4:
        num1,num2 = readValues()
        showDiv(num1,num2)
    elif op==0:
        print("Gracias por usar mi calculadora :D")
        
    

def main():
    while True:
        op = menu()
        if op > 0 and op <=4: chooseOp(op)
        elif op ==(0): break
        else: print("Opcion no valida, intente de nuevo")    
        
        

main()    