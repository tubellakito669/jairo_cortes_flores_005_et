from FUNCIONES_ET_JAIRO_CORTES_FLORES_005V import*

lista_empleados = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

print()
print("BIENVENIDO A NUESTRO SISTEMA DE GESTIÓN DE EMPLEADOS")

while True:
    print()
    print("Estas son las opciones a ejecutar en nuetra plataforma: ")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del rpograma")
    opcion = input("Ingrese una opcion a ejecutar porfavor: ")
        
    if opcion == '1':
            asignar_sueldos_aleatorios()
    elif opcion == '2':
            clasificar_sueldos()
    elif opcion == '3':
            ver_estadisticas()
    elif opcion == '4':
            reporte_sueldos()
    elif opcion == '5':
            print("¡Hasta luego!, Saliendo del programa........")
            break
    else:
            print("Opcion no valida. Por favor, intenta de nuevo.")