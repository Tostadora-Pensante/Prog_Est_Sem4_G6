#Este programa va a leer la edad de una persona y decirme si es menor o mayor de edad XD
age = 0
def readAge():
    print("Digame su edad ministro ")
    global age 
    age = int(input())

def evalAge(age):
    return age >= 18

def show():
    global age
    print("Mayor de edad" if evalAge(age) else "Menor de edad")

readAge()
show()