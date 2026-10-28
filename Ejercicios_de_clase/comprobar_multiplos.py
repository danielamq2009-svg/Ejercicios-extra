def es_multiplo(posible_multiplo, divisor):
    if divisor == 0:
        return False
    return posible_multiplo % divisor == 0

a = int(input("Ingrese el primer entero: "))
b = int(input("Ingrese el segundo entero: "))

retorno1 = es_multiplo(a, b)

#intercambiar
retorno2 = es_multiplo(b, a)

print(f"¿{a} es múltiplo de {b}?: {retorno1}")
print(f"¿{b} es múltiplo de {a}?: {retorno2}")