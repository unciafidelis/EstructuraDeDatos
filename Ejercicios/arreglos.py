# Crear un arreglo de números enteros
arreglo_enteros = [1, 2, 3, 4, 5]

# Acceder a elementos individuales del arreglo
primer_elemento = arreglo_enteros[0]  # 1
ultimo_elemento = arreglo_enteros[-1]  # 5

# Modificar un elemento del arreglo
arreglo_enteros[2] = 10
# Ahora el arreglo es: [1, 2, 10, 4, 5]

# Agregar elementos al final del arreglo
arreglo_enteros.append(6)
# Ahora el arreglo es: [1, 2, 10, 4, 5, 6]

# Eliminar elementos del arreglo
del arreglo_enteros[1]
# Ahora el arreglo es: [1, 10, 4, 5, 6]

# Calcular la longitud del arreglo
longitud_arreglo = len(arreglo_enteros)  # 5

# Iterar sobre los elementos del arreglo
for elemento in arreglo_enteros:
    print(elemento)

# Crear un arreglo de cadenas de caracteres
arreglo_cadenas = ["Hola", "Mundo", "!"]

print(arreglo_cadenas)

# Acceder a elementos individuales del arreglo de cadenas
palabra_mundo = arreglo_cadenas[1]  # "Mundo"
print(palabra_mundo)
# Concatenar arreglos
arreglo_combinado = arreglo_enteros + arreglo_cadenas
print(arreglo_combinado)
# Ahora el arreglo combinado es: [1, 10, 4, 5, 6, "Hola", "Mundo", "!"]
