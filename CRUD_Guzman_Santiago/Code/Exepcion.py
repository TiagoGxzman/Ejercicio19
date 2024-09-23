print("Ingrese el primer numero")
num1 = int(input())
print("El primer numero es", num1)

print("Ingrese el segundo numero")
num2 = int(input())
print("El segundo numero es", num2)

try:
 
    num1/num2
    result = num1/num2
    print("El resultado de la division es: ", result)

except ZeroDivisionError:
    print("¡CUIDADO! si un cero es ingresado voy a explotar durisimo")

