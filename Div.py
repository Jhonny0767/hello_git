n = int(input("Introduce tu numero a dividir: "))
m = int(input("Introduce tu numero divisor: "))
d = n / m
c = str(int(n) // int(m))
r = str(int(n) % int(m))
print("El resultado de la divicion es", str(d) + ' con un cociente de:'+ c +' y un resto:' + r)



n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))