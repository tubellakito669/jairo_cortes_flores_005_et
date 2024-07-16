import random
import math
lista_empleados = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = {}

def asignar_sueldos_aleatorios():
    print("Los sueldos se han asignado de forma correcta.")
    global sueldos
    sueldos = {empleado: random.randint(300000, 2500000) for empleado in lista_empleados}
    

def clasificar_sueldos():
    menores_800000 = []
    entre_800000_y_2M = []
    superiores_2M = []
    
    for empleado, sueldo in sueldos.items():
        if sueldo < 800000:
            menores_800000.append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800000_y_2M.append((empleado, sueldo))
        else:
            superiores_2M.append((empleado, sueldo))
    print()
    print("Sueldos menores a $800,000")
    print()
    print("TOTAL:", len(menores_800000))
    for empleado, sueldo in menores_800000:
        print(f"{empleado} ${sueldo}")
    


    print()
    print("Sueldos entre $800,000 y $2,000,000")
    print("TOTAL:", len(entre_800000_y_2M))
    for empleado, sueldo in entre_800000_y_2M:
        print(f"{empleado} ${sueldo}")

    print()
    print("Sueldos superiores a $2,000,000")
    print("TOTAL:", len(superiores_2M))
    for empleado, sueldo in superiores_2M:
        print(f"{empleado} ${sueldo}")
    print()
    print("TOTAL SUELDOS: $", sum(sueldo for _, sueldo in sueldos.items()))

def ver_estadisticas():
    sueldos_lista = list(sueldos.values())
    if sueldos_lista:
        max_sueldo = max(sueldos_lista)
        min_sueldo = min(sueldos_lista)
        promedio_sueldos = sum(sueldos_lista) / len(sueldos_lista)
        producto_sueldos = math.prod(sueldos_lista)
        media_geometrica = producto_sueldos ** (1 / len(sueldos_lista))
        
        print()
        print(f"Sueldo mas alto: ${max_sueldo}")
        print(f"Sueldo mas bajo: ${min_sueldo}")
        print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
        print(f"Media geometrica: ${media_geometrica:.2f}")
    else:
        print("No se han asignado sueldos todavía.")


        