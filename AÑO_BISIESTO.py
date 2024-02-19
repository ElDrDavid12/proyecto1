for i in range(1800, 2025):
    if (i & 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"El año {i} es bisiesto")
    else:
        print(f"El año {i} es no bisiesto")    