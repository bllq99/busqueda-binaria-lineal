import random
import time

# Implementación de un algoritmo de búsqueda binaria en Python

# Comparación entre búsqueda binaria y búsqueda lineal

# Búsqueda lineal: inspecciona cada elemento de la lista hasta encontrar el objetivo
# Si es encontrado, devuelve su índice; si no, devuelve -1

def busqueda_lineal(lista, objetivo):
    # Ejemplo lista = [3, 5, 2, 4, 9]
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Búsqueda binaria: Usa la técnica de "divide y vencerás"
# Requiere que la lista esté ordenada

def busqueda_binaria(lista, objetivo, inicio=None, fin=None):
    if inicio is None:
        inicio = 0
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1
    
    # Ejemplo lista = [2, 3, 4, 5, 9] 
    punto_medio = (inicio + fin) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, inicio, punto_medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio + 1, fin)
    
# Ejemplo de uso
if __name__ == "__main__":

    longitud = 10000
    # Generar una lista ordenada de números aleatorios
    lista_ordenada = set()
    while len(lista_ordenada) < longitud:
        lista_ordenada.add(random.randint(-3*longitud, 3*longitud))
    lista_ordenada = sorted(list(lista_ordenada))

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_lineal(lista_ordenada, objetivo)
    fin = time.time()
    print("Busqueda lineal tiempo: ", (fin - inicio), "segundos")

    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print("Busqueda binaria tiempo: ", (fin - inicio), "segundos")