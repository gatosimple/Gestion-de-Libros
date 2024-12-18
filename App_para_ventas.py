# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:37:57 2023

@author: Windows
"""

import random
import ast

"Implementación------------------------------------------------------------------"
def ordenar_venta_total(): 
    ventas = diccionario_conjunto()
    for i in range(len(ventas) - 1):
        for j in range(len(ventas) - 1 - i):
            # k = k + 1
            if(ventas[j]["Total_venta"] < ventas[j + 1]["Total_venta"]):
                # k2 = k2 + 1
                aux = ventas[j + 1]
                ventas[j + 1] = ventas[j]
                ventas[j] = aux
    
    lineas = ""
    for venta in ventas:
        linea = {
                'Numero_de_venta': venta["Numero_de_venta"],
                'Código_inventario': venta["Código_inventario"],
                'Producto': venta["Producto"],
                'Descripción': venta["Descripción"],
                'Cantidad': venta["Cantidad"],
                'Precio_de_venta': venta["Precio_de_venta"],
                'Total_venta': venta["Total_venta"]
                } 
        linea = str(linea) + "\n"
        lineas = lineas + linea 
        
    file = open("ventas_total.txt","w")
    file.write(lineas.strip())
    file.close()
    
    return print("\n" + "Las ventas han sido correctamente ordenadas")
"implementación----------------------------------------------------------------"
#lista de los 3 productos
def diccionario_conjunto():
    lista1 = leer_ventas("Laptop")
    lista2 = leer_ventas("Desktop")
    lista3 = leer_ventas("Impresora")
    lista_total = []
    if lista1:
       lista_total = lista1
    if lista2:
       lista_total = lista_total + lista2
    if lista3:
       lista_total = lista_total + lista3
    return lista_total

"implementación----------------------------------------------------------------"
def quicksort(lista):
    if(len(lista) <= 1):
        return lista
    else:
        pivot = lista[0]
        menores = []
        mayores = []
        for i in range(1, len(lista)):
            if(lista[i] > pivot):
                mayores.append(lista[i])
            else:
                menores.append(lista[i])
        mayores = quicksort(mayores)
        menores = quicksort(menores)
        return menores + [pivot] + mayores

"implementación----------------------------------------------------------------"
def modificar_cantidad(diccionario, fila, nuevo_dato):
        #unidad
        elemento = diccionario[fila]
        #actualizo cantidad 
        nueva_cantidad = nuevo_dato
        #actualizo total
        precio_venta = elemento["Precio_de_venta"]
        total_venta = nueva_cantidad * precio_venta
        #demas datos
        numero_de_venta = elemento["Numero_de_venta"]
        producto = elemento['Producto']
        codigo = elemento['Código_inventario']
        descripcion = elemento["Descripción"]
        
        d = {
           'Numero_de_venta': numero_de_venta,
           'Código_inventario': codigo,
           'Producto': producto,
           'Descripción': descripcion,
           'Cantidad': nueva_cantidad,
           'Precio_de_venta': precio_venta,
           'Total_venta': total_venta 
           } 
        return d

"Raúl---------------------------------------------------------------"
def busqueda(numero, diccionario):
    lista = quicksort(diccionario) 
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if numero == lista[medio]:
            pos = medio
            break
        else:
            if numero < lista[medio]:
                der = medio - 1
            else:
                izq = medio + 1
    return pos

"Raúl---------------------------------------------------------------"
def modificar_laptop():
    numero_de_venta = int(input("\n" + "Ingrese el numero de venta a buscar: ")) 
    laptops = leer_ventas("Laptop")
    lista_numeros = []
    for laptop in laptops:
        numero = laptop["Numero_de_venta"]
        lista_numeros.append(numero)
    
    # función busqueda (binaria)
    i = busqueda(numero_de_venta, lista_numeros) 
    if i < 0:
        x = print("\n" + "El numero de venta digitado no existe, intente otra vez")
        return x
    
    else:
        x = int(input("ingrese la nueva cantidad: "))
        # función modificar_cantidad_laptop
        d = modificar_cantidad(laptops, i, x)
        # destino (file)
        with open("ventas_laptops.txt", "r") as file:
            lineas = file.readlines()
        
        linea_modificada = str(d) + "\n"
        lineas[i] = linea_modificada
        
        # grabar en el archivo de texto 'ventas_laptops.txt'
        with open('ventas_laptops.txt', 'w') as file:
            file.writelines(lineas) 
            
#Paolo--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def modificar_desktop():
    numero_de_venta = int(input("\n" + "Ingrese el numero de venta a buscar: ")) 
    desktops = leer_ventas("Desktop")
    lista_numeros = []
    for desktop in desktops:
        numero = desktop["Numero_de_venta"]
        lista_numeros.append(numero)
    
    # función busqueda (binaria)
    i = busqueda(numero_de_venta, lista_numeros) 
    if i < 0:
        x = print("\n" + "El numero de venta digitado no existe, intente otra vez")
        return x
    
    else:
        x = int(input("ingrese la nueva cantidad: "))
        # función modificar_cantidad_desktop
        d = modificar_cantidad(desktops, i, x)
        # destino (file)
        with open("ventas_desktops.txt", "r") as file:
            lineas = file.readlines()
        
        linea_modificada = str(d) + "\n"
        lineas[i] = linea_modificada
        
        # grabar en el archivo de texto 'ventas_desktops.txt'
        with open('ventas_desktops.txt', 'w') as file:
            file.writelines(lineas)   

"#LUCEN----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
def modificar_impresora():
    numero_de_venta = int(input("\n" + "Ingrese el numero de venta a buscar: ")) 
    impresoras = leer_ventas("Impresora")
    lista_numeros = []
    for impresora in impresoras:
        numero = impresora["Numero_de_venta"]
        lista_numeros.append(numero)
    
    # función busqueda (binaria)
    i = busqueda(numero_de_venta, lista_numeros) 
    if i < 0:
        x = print("\n" + "El numero de venta digitado no existe, intente otra vez")
        return x
    
    else:
        x = int(input("ingrese la nueva cantidad: "))
        # función modificar_cantidad_impresora
        d = modificar_cantidad(impresoras, i, x)
        # destino (file)
        with open("ventas_impresoras.txt", "r") as file:
            lineas = file.readlines()
        
        linea_modificada = str(d) + "\n"
        lineas[i] = linea_modificada
        
        # grabar en el archivo de texto 'ventas_impresoras.txt'
        with open('ventas_impresoras.txt', 'w') as file:
            file.writelines(lineas)   

"Raúl---------------------------------------------------------------"
def modificar_venta():
    print("""
Opciones de Venta:
    1) Laptop
    2) Desktop
    3) Impresora
          """)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1: # modificar venta laptop
        modificar_laptop()
    elif opcion == 2: # modificar venta desktop
        modificar_desktop()
    elif opcion == 3: # modificar venta impresora
        modificar_impresora()


#Raúl----------------------------------------------------------------------
def leer_ventas(text): # se relaciona con el cod_inv
    if text == "Laptop":
        file = open('ventas_laptops.txt', 'r')
        lines = file.readlines()
        resp = []
        for line in lines:
            venta_str = line.strip()
            venta = ast.literal_eval(venta_str)
            resp.append(venta)
        return resp
    
    if text == "Desktop":
        file = open('ventas_desktops.txt', 'r')
        lines = file.readlines()
        resp = []
        for line in lines:
            venta_str = line.strip()
            venta = ast.literal_eval(venta_str)
            resp.append(venta)
        return resp
    
    if text == "Impresora":
        file = open('ventas_impresoras.txt', 'r')
        lines = file.readlines()
        resp = []
        for line in lines:
            venta_str = line.strip()
            venta = ast.literal_eval(venta_str)
            resp.append(venta)
        return resp

#Raúl----------------------------------------------------------------------
def cod_inv(diccionario):  # se relaciona con leer_ventas
    if len(diccionario) == 0:
        return 2000
    else:
        mayor = 0
        for elemento in diccionario:
            codigo = elemento["Numero_de_venta"]
            if codigo > mayor:          
                mayor = codigo
        return mayor + 1

#Raúl----------------------------------------------------------------------
def generar_importado(text):
    new_text = text.lower()
    importado = False
    if new_text == "si":
        importado = True
        
    if importado:
        return "Importado"
    else:
        return "No importado"

#Raúl----------------------------------------------------------------------
def generar_costo_almacenamiento(text):
    if text == "Laptop": # aleatorio par entre 200 y 450
        resp = random.randint(200, 450)
        while resp % 2 != 0:
            resp = random.randint(200, 450)
        return resp
    elif text == "Desktop":
        resp = random.randint(180, 250)
        while resp % 3 != 0:
            resp = random.randint(180, 250)
        return resp
    elif text == "Impresora":
        resp = random.randint(90, 150)
        while resp % 2 == 0:
            resp = random.randint(90, 150)
        return resp
    
#Raúl----------------------------------------------------------------------   
def generar_costo_funda(text):
    if text == "Laptop": #aleatorio entre 80 y 150
        resp = random.randint(80, 150)
        return resp
    elif text == "Desktop": #aleatorio entre 150 y 250
        resp =  random.randint(150, 250)
        return resp

        
def leer_laptops():
    file = open('laptops.txt', 'r')
    lines = file.readlines()
    # Strips the newline character
    resp = []
    for line in lines:
        laptop_str = line.strip()
        laptop = ast.literal_eval(laptop_str)
        resp.append(laptop)
    return resp

#Paolo ---------------------------------------------------------------------
def leer_desktops():
    file = open('desktops.txt','r')
    lines = file.readlines()
    # Strips the newline character
    resp = []
    for line in lines:
        desktop_str = line.strip()
        desktop = ast.literal_eval(desktop_str)
        resp.append(desktop)
    return resp

def leer_impresoras():
    file = open('impresoras.txt', 'r')
    lines = file.readlines()
    # Strips the newline character
    resp = []
    for line in lines:
        impresora_str = line.strip()
        impresora = ast.literal_eval(impresora_str)
        resp.append(impresora)
    return resp
        
def generar_codigo():
    # aleatorio múltiplo de 7 entre 20000 y 90000
    resp = 0
    resp = random.randint(20000, 90000)
    while resp % 7 != 0:
        resp = random.randint(20000, 90000)
    return resp

#Raúl------------------------------------------------------------------------------
def ingresar_laptop():  
    # ingresar datos de latop
    print("\n" + "Ingrese los datos de una nueva laptop: ") 
    descripcion = input("Descripción: ")
    importado_str = input("Importado (si/no): ")
    codigo = generar_codigo()
    producto = 'Laptop'
    importado = generar_importado(importado_str)
    costo_almacenamiento = float(generar_costo_almacenamiento("Laptop"))
    costo_funda = float(generar_costo_funda("Laptop"))
    # creando una fila
    d = {
        'Código_inventario': codigo,
        'Producto': producto,
        'Descripción': descripcion,
        'Estado': importado,
        'Costo_almacenamiento': costo_almacenamiento,
        'Costo_funda': costo_funda
    }
    # grabar en el archivo de texto 'laptops.txt'
    with open('laptops.txt', 'a') as file:
        file.write(str(d) + "\n")
    return print("\n" + "Se ingresó con éxito una laptop")
        
#Paolo------------------------------------------------------------------------------------
def ingresar_desktop():
    # ingresar datos de desktop
    print("\n" + "Ingrese los datos de una nueva desktop: ") 
    descripcion = input("Descripción: ")
    importado_str = input("Importado (si/no): ")
    codigo = generar_codigo()
    producto = 'Desktop'
    importado = generar_importado(importado_str)
    costo_almacenamiento = float(generar_costo_almacenamiento("Desktop")) 
    costo_funda = float(generar_costo_funda("Desktop")) 
    # creando una fila
    d = {
        'Código_inventario': codigo,
        'Producto': producto,
        'Descripción': descripcion,
        'Estado': importado,
        'Costo_almacenamiento': costo_almacenamiento,
        'Costo_funda': costo_funda
    }
    # grabar en el archivo de texto 'desktops.txt'
    with open('desktops.txt', 'a') as file:
        file.write(str(d) + "\n")
    return print("\n" + "Se ingresó con éxito una desktop")    

def ingresar_impresora():
    # ingresar datos de impresora
    print("\n" + "Ingrese los datos de una nueva impresora: ") 
    descripcion = input("Descripción: ")
    importado_str = input("Importado (si/no): ")
    codigo = generar_codigo()
    producto = 'Impresora'
    importado = generar_importado(importado_str)
    costo_almacenamiento = float(generar_costo_almacenamiento("Impresora"))
    #creando una fila
    d = {
        'Código_inventario': codigo,
        'Producto': producto,
        'Descripción': descripcion,
        'Estado': importado,
        'Costo_almacenamiento': costo_almacenamiento
    }
    # grabar en el archivo de texto 'impresora.txt'
    with open('impresoras.txt', 'a') as file:
        file.write(str(d) + "\n")
    return print("\n" + "Se ingresó con éxito una impresora")

#Raúl ----------------------------------------------------------------------------------------------
def vender_laptop():
    laptops = leer_laptops() # list[dic]
    for laptop in laptops:
        print(str(laptop['Código_inventario']) + ', ' + laptop['Descripción'])
    print("")
    codigo = int(input("Ingrese un código de inventario: "))
        
    total = diccionario_conjunto() 
    estado = False
    for laptop in laptops:
        if codigo == laptop['Código_inventario']:
            cantidad = int(input("Ingrese la cantidad vendida del producto: "))
            precio_venta = laptop['Costo_almacenamiento'] * 1.25
            producto = laptop['Producto']
            numero_de_venta = cod_inv(total)  
            descripcion = laptop['Descripción']
            total_venta = precio_venta * cantidad 
            d = {
                'Numero_de_venta': numero_de_venta,
                'Código_inventario': codigo,
                'Producto': producto,
                'Descripción': descripcion,
                'Cantidad': cantidad,
                'Precio_de_venta': precio_venta,
                'Total_venta': total_venta 
                } 
            # grabar en el archivo de texto 'ventas_laptops.txt'
            with open('ventas_laptops.txt', 'a') as file:
                file.write(str(d) + "\n")
            estado = True
    
    if estado:
        return print("Se ha ingresado la venta correctamente")
    else:
        return print("\n" + "El código de inventario ingresado no existe, inténtelo otra vez")

#Paolo-----------------------------------------------------------------------------------------------
def vender_desktop():               
    desktops = leer_desktops() # list[dic]
    for desktop in desktops:
        print(str(desktop['Código_inventario']) + ', ' + desktop['Descripción'])
    print("")
    codigo = int(input("Ingrese un código de inventario: "))
        
    total = diccionario_conjunto() 
    estado = False
    for desktop in desktops:
        if codigo == desktop['Código_inventario']:
            cantidad = int(input("Ingrese la cantidad vendida del producto: "))
            precio_venta = desktop['Costo_almacenamiento'] * 1.25
            producto = desktop['Producto']
            numero_de_venta = cod_inv(total)  
            descripcion = desktop['Descripción']
            total_venta = precio_venta * cantidad 
            d = {
                'Numero_de_venta': numero_de_venta,
                'Código_inventario': codigo,
                'Producto': producto,
                'Descripción': descripcion,
                'Cantidad': cantidad,
                'Precio_de_venta': precio_venta,
                'Total_venta': total_venta 
                } 
            # grabar en el archivo de texto 'ventas_desktops.txt'
            with open('ventas_desktops.txt', 'a') as file:
                file.write(str(d) + "\n")
            estado = True
    
    if estado:
        return print("Se ha ingresado la venta correctamente")
    else:
        return print("\n" + "El código de inventario ingresado no existe, inténtelo otra vez")

"NUEVO----------------------------------------------------------------------------------"
def vender_impresora():               
    impresoras = leer_impresoras() # list[dic]
    for impresora in impresoras:
        print(str(impresora['Código_inventario']) + ', ' + impresora['Descripción'])
    print("")
    codigo = int(input("Ingrese un código de inventario: "))
        
    total = diccionario_conjunto() 
    estado = False
    for impresora in impresoras:
        if codigo == impresora['Código_inventario']:
            cantidad = int(input("Ingrese la cantidad vendida del producto: "))
            precio_venta = impresora['Costo_almacenamiento'] * 1.25
            producto = impresora['Producto']
            numero_de_venta = cod_inv(total)  
            descripcion = impresora['Descripción']
            total_venta = precio_venta * cantidad 
            d = {
                'Numero_de_venta': numero_de_venta,
                'Código_inventario': codigo,
                'Producto': producto,
                'Descripción': descripcion,
                'Cantidad': cantidad,
                'Precio_de_venta': precio_venta,
                'Total_venta': total_venta 
                } 
            # grabar en el archivo de texto 'ventas_impresoras.txt'
            with open('ventas_impresoras.txt', 'a') as file:
                file.write(str(d) + "\n")
            estado = True
    
    if estado:
        return print("Se ha ingresado la venta correctamente")
    else:
        return print("\n" + "El código de inventario ingresado no existe, inténtelo otra vez")
    
    
def ingresar_venta(): 
    print("""
Opciones de Venta:
    1) Laptop
    2) Desktop
    3) Impresora
          """)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        # vender una o varias laptops
        vender_laptop()
    elif opcion == 2:
        # vender una o varias desktops
        vender_desktop()
    elif opcion == 3:
        #vender una o varias impresoras
        vender_impresora()

##########
def buscar_venta():
    encontrado = False
    ventas = diccionario_conjunto()
    while encontrado == False:
        numero_de_venta = int(input("\n" + "Ingrese el numero de venta a buscar: ")) 
        for venta in ventas:
            if numero_de_venta == venta["Numero_de_venta"]:
                encontrado = True
                return print(venta)
        if encontrado == False:
            return print("\n" + "El número de venta ingresado no existe, inténtelo otra vez")
    
#########

def mayor_venta(): 
    ventas_total = diccionario_conjunto()
    for i in range(len(ventas_total) - 1):
        for j in range(len(ventas_total) - 1 - i):
            # k = k + 1
            if(ventas_total[j]["Total_venta"] > ventas_total[j + 1]["Total_venta"]):
                # k2 = k2 + 1
                aux = ventas_total[j + 1]
                ventas_total[j + 1] = ventas_total[j]
                ventas_total[j] = aux
    z = ventas_total[len(ventas_total) - 1]# el mayor name
    print("\n" + "La mayor venta fue:" + "\n" + str(z))
    
def ordenar_venta(text): 
    ventas = leer_ventas(text)
    for i in range(len(ventas) - 1):
        for j in range(len(ventas) - 1 - i):
            # k = k + 1
            if(ventas[j]["Total_venta"] < ventas[j + 1]["Total_venta"]):
                # k2 = k2 + 1
                aux = ventas[j + 1]
                ventas[j + 1] = ventas[j]
                ventas[j] = aux
    
    name = text.lower()
    archivo = "ventas_" + name + "s.txt"
    
    lineas = ""
    for venta in ventas:
        linea = {
                'Numero_de_venta': venta["Numero_de_venta"],
                'Código_inventario': venta["Código_inventario"],
                'Producto': venta["Producto"],
                'Descripción': venta["Descripción"],
                'Cantidad': venta["Cantidad"],
                'Precio_de_venta': venta["Precio_de_venta"],
                'Total_venta': venta["Total_venta"]
                } 
        linea = str(linea) + "\n"
        lineas = lineas + linea 
        
    file = open(archivo,"w")
    file.write(lineas.strip())
    file.close()
    return print("\n" + "Se ordenaron correctamentes las ventas de",name + "s")
       
    
def ordenar_venta_por_producto(): 
    opcion = 99
    while opcion != 0:
        print("""
Opciones:
    1) Ordenar ventas de Laptops
    2) Ordenar ventas de Desktops
    3) Ordenar ventas de Impresoras
                """)
        opcion = int(input("Ingrese una opción: "))     
        if opcion == 1:
            text = "Laptop"
            return ordenar_venta(text)
        elif opcion == 2:
            text = "Desktop"
            return ordenar_venta(text)
        elif opcion == 3:
            text = "Impresora"
            return ordenar_venta(text)
        else:
            pass

          
def main():
    opcion = 99
    while opcion != 0:
        print("""
Opciones:
    1) Ingresar Laptop
    2) Ingresar Desktop
    3) Ingresar Impresora
    4) Registrar Venta
    5) Modificar Venta
    6) Ordenar Venta por Producto
    7) Ordenar Todas las Ventas
    8) Buscar Venta
    9) Venta más alta
    0) Salir
              """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingresar_laptop()
        elif opcion == 2:
            ingresar_desktop()
        elif opcion == 3:
            ingresar_impresora()
        elif opcion == 4:
            ingresar_venta()
        elif opcion == 5:
            modificar_venta()
        elif opcion == 6: 
            ordenar_venta_por_producto()
        elif opcion == 7:
            ordenar_venta_total() #####
        elif opcion == 8:
            buscar_venta()
        elif opcion == 9:
            mayor_venta()
        else:
            pass
            
    
main()