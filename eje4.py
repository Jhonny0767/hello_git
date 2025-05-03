p = float(input("Introduce tu peso: "))
e = float(input("Introduce tu estatura: "))
imc = p / (e * e)
print("Tu masa corporal es", str(imc) + ' IMC')


peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))