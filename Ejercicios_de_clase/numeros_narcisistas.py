
def es_narcisista(num):
    cantidad = 0
    temp = num

    while temp > 0:
        cantidad += 1
        temp = int(temp / 10)

    suma = 0
    temp = num

    while temp > 0:
        digito = temp % 10
        suma += digito ** cantidad
        temp = int(temp / 10)

    return suma == num


while True:
    num = int(input("Ingrese un número: "))

    if num <= 0:
        print("Programa terminado")
        break

    if es_narcisista(num):
        print("Número narcisista")
    else:
        print("Número no es narcisista")
