import notas 
from colorama import Fore
def greet():
    print(Fore.CYAN + "Bienvenidos a este Programa Evaluador hecho en 10 minutos :v", Fore.RESET)
    print(Fore.BLUE + "Este sistema no te califica como tal, solo evalua tu nota y te dice como clasifica segun el sistema educativo del minet.", Fore.RESET)
    print(Fore.RED + "Recuerden una mala nota no los define, pero si estudien a no ser que quieran botar la carrera!", Fore.RESET)

def menu():
    print("Evaluador Insano:")
    print("1. Evaluar notas")
    print("2. Explicacion de que Significa cada categoria.")
    print("0. Salir del programa.")
    op = int(input("Digite el # de la opcion que desea usar."))
    return op


def chooseOp(op):
    if op == 1:
        nota = notas.readValue()
        notas.evaluationGrade(nota)
    elif op == 2:
        notas.explanation()
    elif op == 0:
        print("Gracias por usar mi calculadora :D")
        
def main():
    greet()
    while True:
            op = menu()
            if op > 0 and op <=2: chooseOp(op)
            elif op ==(0): break
            else: print("Opcion no valida, intente de nuevo")  

main()
 
