from colorama import Fore
def amountGrades():
    grades = int(input("Ingrese la cantidad de notas a evaluar"))
    return grades

def readValue():
    grade = float(input("Digite la nota a evaluar porfavor: "))
    return grade


def evaluationGrade(grade):

    for i in range(amountGrades):
     print(f"Evaluando nota {i+1}:")
     grade = readValue()

    if grade < 60 and grade>=0:
       print(Fore.RED + "Esta nota es de aprendizaje inicial, se recomienda estudiar :U", Fore.RESET)
                 
    elif grade <= 75:
         print(Fore.YELLOW +"esta nota es de aprendizaje fundamental, aceptable :v", Fore.RESET)

    elif grade <= 89:
         print(Fore.LIGHTGREEN_EX + "Esta nota es de aprendizaje Satisfactoria, en hora buena :D", Fore.RESET) 

    elif grade <= 100:
        print(Fore.GREEN + "Esta nota es de aprendizaje Avanzado! Buena nota :P", Fore.RESET)

    else:
        print(Fore.RED + "La nota es invalida pruebe de nuevo", Fore.RESET)


def explanation():
    print(Fore.LIGHTRED_EX + "Aprendizaje Inicial se refiere a cualquier nota por debajo de 60, normalmente es una forma suave de decir que el estudiante reprobo.", Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "Aprendizaje Fundamental se refiere a que el estudiante paso con el minimo necesario para aprobar la evaluación.",Fore.RESET)
    print(Fore.GREEN + "Aprendizaje Satisfactorio significa que el estudiante paso de forma buena la evaluación.", Fore.RESET)
    print(Fore.BLUE + "Aprendizaje Avanzado significa que el estudiante aprobo de forma más que satisfactoria la evaluación.", Fore.RESET)







                 