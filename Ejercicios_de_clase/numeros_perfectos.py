
def sum_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum
            
while True:
    num = int(input("Ingrese un número: "))
    if num < 0:
        print("Programa terminado")
        break
    if num <= 2: 
        print("El número debe ser mayor que dos")
        continue
    
    if sum_num(num) == num:
        print("Número perfecto")
    else:
        print("Número no es perfecto")