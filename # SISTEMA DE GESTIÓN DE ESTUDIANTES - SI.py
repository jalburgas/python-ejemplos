# SISTEMA SIMPLE DE CALIFICACIONES - PROYECTO PARA EXAMEN

estudiantes = []  # Lista para guardar los estudiantes

while True:
    print("\n" + "="*30)
    print("1. Agregar estudiante")
    print("2. Ver estudiantes")
    print("3. Calcular promedio")
    print("4. Salir")
    print("="*30)
    
    opcion = input("Elija opción (1-4): ")
    
    # OPCIÓN 1: AGREGAR ESTUDIANTE
    if opcion == "1":
        print("\n--- NUEVO ESTUDIANTE ---")
        nombre = input("Nombre: ").upper()
        apellido = input("Apellido: ").upper()
        
        # Validación con operador lógico OR
        if nombre == "" or apellido == "":
            print("Error: Nombre y apellido son obligatorios")
        else:
            nota = float(input("Nota (0-20): "))
            
            # Validación con operador lógico AND
            if nota >= 0 and nota <= 20:
                # Crear diccionario
                estudiante = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "nota": nota
                }
                estudiantes.append(estudiante)
                print(f"¡{nombre} {apellido} agregado!")
            else:
                print("Nota inválida")
    
    # OPCIÓN 2: VER ESTUDIANTES
    elif opcion == "2":
        print("\n--- LISTA DE ESTUDIANTES ---")
        
        # IF para verificar si hay estudiantes
        if len(estudiantes) == 0:
            print("No hay estudiantes")
        else:
            # FOR para mostrar cada estudiante
            for i in range(len(estudiantes)):
                # IF para determinar estado
                if estudiantes[i]["nota"] >= 12:
                    estado = "APROBADO"
                else:
                    estado = "DESAPROBADO"
                
                print(f"{i+1}. {estudiantes[i]['nombre']} {estudiantes[i]['apellido']} - Nota: {estudiantes[i]['nota']} - {estado}")
    
    # OPCIÓN 3: CALCULAR PROMEDIO
    elif opcion == "3":
        print("\n--- PROMEDIO GENERAL ---")
        
        if len(estudiantes) == 0:
            print("No hay estudiantes")
        else:
            suma = 0
            # FOR para sumar todas las notas
            for est in estudiantes:
                suma = suma + est["nota"]
            
            promedio = suma / len(estudiantes)
            print(f"Total estudiantes: {len(estudiantes)}")
            print(f"Promedio general: {promedio:.2f}")
            
            # IF con operadores lógicos
            if promedio >= 12:
                print("Nivel: APROBATORIO")
            else:
                print("Nivel: NECESITA MEJORAR")
    
    # OPCIÓN 4: SALIR
    elif opcion == "4":
        print("\n¡Hasta luego!")
        break  # Sale del while
    
    # OPCIÓN INVÁLIDA
    else:
        print("Opción inválida")

print(f"Total de estudiantes registrados: {len(estudiantes)}")