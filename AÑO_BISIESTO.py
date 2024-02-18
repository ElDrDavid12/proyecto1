modo = input("En un lapso de tiempo los años bisiestos y no bisiestos oh solo un año: ")
if "lapso de tiempo" or "lapso" in modo:
    for i in range (0, 2025):
        if i % 100 == 0 and i % 400 == 1:
            print(f"El año {i} no es Bisiesto")
        elif i % 4 == 0:
            print(f"el año {i} es Bisiesto")
        elif i % 100 == 0 and i % 400 == 0:
            print(f"El año {i} puede ser considerado bisiesto.")        