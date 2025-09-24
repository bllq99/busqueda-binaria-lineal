# Búsqueda Binaria vs Búsqueda Lineal

Este programa implementa y compara dos algoritmos fundamentales de búsqueda: **búsqueda lineal** y **búsqueda binaria**, demostrando sus diferencias en términos de eficiencia y complejidad temporal.

## Descripción

El programa contiene implementaciones de:
- **Búsqueda Lineal**: Algoritmo que inspecciona cada elemento secuencialmente
- **Búsqueda Binaria**: Algoritmo que utiliza la técnica "divide y vencerás" en listas ordenadas

## Características

- Implementación completa de ambos algoritmos
- Comparación de rendimiento con listas de 10,000 elementos
- Medición de tiempo de ejecución

## Complejidad de Algoritmos

| Algoritmo | Complejidad Temporal | Complejidad Espacial | Requisitos |
|-----------|---------------------|---------------------|------------|
| Búsqueda Lineal | O(n) | O(1) | Ninguno |
| Búsqueda Binaria | O(log n) | O(log n)* | Lista ordenada |

*O(1) en implementación iterativa

## Requisitos

- Python 3.6+
- Librerías estándar: `random`, `time`

## Uso

1. Clona el repositorio:
```bash
git clone https://github.com/bllq99/busqueda-binaria-lineal.git
cd busqueda-binaria-lineal
```

2. Ejecuta el script:
```bash
python busqueda-binaria-lineal.py
```

## Ejemplo de Salida

```
Busqueda lineal tiempo:  0.8234 segundos
Busqueda binaria tiempo:  0.0145 segundos
```

## Cómo Funcionan los Algoritmos

### Búsqueda Lineal
```python
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
```
- Recorre la lista elemento por elemento
- No requiere que la lista esté ordenada
- En el peor caso, revisa todos los elementos

### Búsqueda Binaria
```python
def busqueda_binaria(lista, objetivo, inicio=None, fin=None):
    # Divide la lista por la mitad en cada iteración
    # Solo funciona con listas ordenadas
    # Reduce el espacio de búsqueda a la mitad en cada paso
```
- Utiliza recursión para dividir el problema
- Requiere lista ordenada
- Mucho más eficiente para listas grandes

## Casos de Uso

### Búsqueda Lineal - Ideal para:
- Listas pequeñas (< 100 elementos)
- Listas no ordenadas
- Cuando necesitas encontrar múltiples ocurrencias
- Estructuras de datos sin acceso aleatorio

### Búsqueda Binaria - Ideal para:
- Listas grandes ordenadas
- Cuando el rendimiento es crítico
- Búsquedas frecuentes en el mismo conjunto de datos
- Datos que se mantienen ordenados