from colorama import Fore
def amountGrades(grades):
    grades = int(input("Ingrese la cantidad de notas a evaluar"))
    return grades

def readValue():
    grade = float(input("Digite la nota a evaluar porfavor: "))
    return grade


def evaluationGrade(grade):
    if grade < 60:
       print(Fore.RED + "Esta nota es de aprendizaje inicial, se recomienda estudiar :U", Fore.RESET)
                 
    elif grade == 60 and grade <= 75:
         print(Fore.YELLOW +"esta nota es de aprendizaje fundamental, aceptable :v", Fore.RESET)

    elif grade >= 76 and grade <= 89:
         print(Fore.LIGHTGREEN_EX + "Esta nota es de aprendizaje Satisfactoria, en hora buena :D", Fore.RESET) 

    elif grade > 90 and grade <= 100:
        print(Fore.GREEN + "Esta nota es de aprendizaje Avanzado! Buena nota :P", Fore.RESET)



def explanation():
    print("Aprendizaje Inicial se refiere a cualquier nota por debajo de 60, normalmente es una forma suave de decir que el estudiante reprobo.")
    print("Aprendizaje Fundamental se refiere a que el estudiante paso con el minimo necesario para aprobar la evaluación.")
    print("Aprendizaje Satisfactorio significa que el estudiante paso de forma buena la evaluación.")
    print("Aprendizaje Avanzado significa que el estudiante aprobo de forma más que satisfactoria la evaluación.")







                 