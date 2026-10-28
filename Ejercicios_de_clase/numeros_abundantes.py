
def suma_divisores(num):
    suma = 0

    for i in range(1, num):
        if num % i == 0:
            suma += i

    return suma


inicio = int(input("Rango inicial: "))
final = int(input("Rango final: "))

print("Los números abundantes entre", inicio, "y", final, "son:")

for num in range(inicio, final + 1):
    if suma_divisores(num) > num:
        print(num, end=", ")



    
