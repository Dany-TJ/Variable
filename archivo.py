#definición de las variables
entero = 25
flotante = 8.80
cedena = "Hermosa"
booleano = True 

#Concatenación de variables
resultado = cedena + str(entero) + str(flotante) + str(booleano)

#límites de los enteros 
#python no tiene límites fijos para enteros depende de la memoría del equipo
#el limite se encuentra se encuentra en sys.maxsize
import sys 
limite_enteros = sys.maxsize
#limites de los flotantes
#En Python, los números de punto flotante siguen el estándar IEEE 754
# Para ver los límites de los flotantes, podemos usar sys.float_info
import sys
limite_flotantes = sys.float_info

#impresión de los resultados
print(f"limites de enteros:{limite_enteros}")
print(f"limites de flotantes:{limite_flotantes}")

# Suma de los primeros n números pares
# La fórmula es n * (n + 1)
n = int(input("Ingrese un número entero para calcular la suma de los primeros n números pares: "))
suma_pares = n * (n + 1)

#impresión de los resultados
print("Resultado de la concatenación:", resultado)
print(f"Suma de los primeros {n} números pares:", suma_pares)