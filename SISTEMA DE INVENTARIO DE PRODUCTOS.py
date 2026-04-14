# SISTEMA DE INVENTARIO DE PRODUCTOS - PROYECTO PARA EXAMEN

productos = []  # Lista para guardar los productos

while True:  # Bucle infinito hasta que el usuario decida salir
    print("\n" + "="*35)
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Calcular valor total")
    print("4. Buscar producto")
    print("5. Salir")
    print("="*35)
    
    opcion = input("Elija opción (1-5): ")
    
    # OPCIÓN 1: AGREGAR PRODUCTO
    if opcion == "1":
        print("\n--- NUEVO PRODUCTO ---")
        nombre = input("Nombre del producto: ").upper() # .upper() es un método de cadenas de texto en Python que convierte todas las letras a MAYÚSCULAS.
        
        # Validación con operador lógico OR
        if nombre == "":
            print("Error: El nombre del producto es obligatorio")
        else:
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio unitario: $"))
            
            # Validación con operador lógico AND
            if cantidad >= 0 and precio >= 0:
                # Crear diccionario del producto
                producto = {
                    "nombre": nombre,
                    "cantidad": cantidad,
                    "precio": precio
                }
                productos.append(producto)
                print(f"✓ {nombre} agregado al inventario!")
            else:
                print("Error: Cantidad y precio deben ser valores positivos")
    
    # OPCIÓN 2: VER INVENTARIO
    elif opcion == "2":
        print("\n--- LISTA DE INVENTARIO ---")
        
        # IF para verificar si hay productos
        if len(productos) == 0:
            print("Inventario vacío")
        else:
            # FOR para mostrar cada producto
            for i in range(len(productos)):
                # IF para determinar stock
                if productos[i]["cantidad"] == 0:
                    estado = "AGOTADO"
                elif productos[i]["cantidad"] < 5:
                    estado = "STOCK BAJO"
                else:
                    estado = "DISPONIBLE"
                
                valor_total = productos[i]["cantidad"] * productos[i]["precio"]
                print(f"{i+1}. {productos[i]['nombre']} - Cant: {productos[i]['cantidad']} - ${productos[i]['precio']:.2f} c/u - Total: ${valor_total:.2f} - {estado}")
    
    # OPCIÓN 3: CALCULAR VALOR TOTAL DEL INVENTARIO
    elif opcion == "3":
        print("\n--- VALOR TOTAL DEL INVENTARIO ---")
        
        if len(productos) == 0:
            print("No hay productos en el inventario")
        else:
            suma_total = 0
            suma_cantidades = 0
            
            # FOR para calcular valor total
            for prod in productos:
                suma_total = suma_total + (prod["cantidad"] * prod["precio"])
                suma_cantidades = suma_cantidades + prod["cantidad"]
            
            print(f"Total productos diferentes: {len(productos)}")
            print(f"Total unidades en stock: {suma_cantidades}")
            print(f"Valor total del inventario: ${suma_total:.2f}")
            
            # IF con operadores lógicos
            if suma_total >= 10000:
                print("Nivel: INVENTARIO DE ALTO VALOR")
            elif suma_total >= 5000:
                print("Nivel: INVENTARIO MEDIO")
            else:
                print("Nivel: INVENTARIO BAJO")
    
    # OPCIÓN 4: BUSCAR PRODUCTO
    elif opcion == "4":
        print("\n--- BUSCAR PRODUCTO ---")
        buscar = input("Nombre del producto a buscar: ").upper()
        encontrado = False
        
        # FOR para buscar el producto
        for prod in productos:
            if prod["nombre"] == buscar:
                encontrado = True
                valor_total = prod["cantidad"] * prod["precio"]
                print(f"\n✓ Producto encontrado:")
                print(f"  Nombre: {prod['nombre']}")
                print(f"  Cantidad: {prod['cantidad']}")
                print(f"  Precio unitario: ${prod['precio']:.2f}")
                print(f"  Valor total: ${valor_total:.2f}")
                break
        
        if not encontrado:
            print(f"No se encontró el producto '{buscar}'")
    
    # OPCIÓN 5: SALIR
    elif opcion == "5":
        print("\n¡Hasta luego! Cerrando sistema de inventario...")
        break  # Sale del while
    
    # OPCIÓN INVÁLIDA
    else:
        print("Opción inválida. Por favor elija 1-5")

# Mostrar resumen final
print(f"\n--- RESUMEN FINAL ---")
print(f"Total de productos registrados: {len(productos)}")
if len(productos) > 0:
    total_unidades = sum(prod["cantidad"] for prod in productos)
    print(f"Total de unidades en inventario: {total_unidades}")
