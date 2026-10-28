temp = float(input("Ingrese la temperatura de la incubadora: "))
if temp > 34:
    print("T.alta")
elif temp < 26:
    print("T.baja")
else:
    print("T.normal")