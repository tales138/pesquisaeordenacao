import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def insertionSort(arr):

  for i in range(1, len(arr)):

    key = arr[i]
    k = i - 1
    while k >= 0 and key < arr[k]:
      arr[k + 1] = arr[k]
      k -= 1

    arr[k + 1] = key

  return arr


temposListaOrdenadaInsertionSort = []
temposListaAleatoriaInsertionSort = []
temposListaInvertidaInsertionSort = []

size_axis = []
for i in range(1000, 10001, 1000):

  size_axis.append(i)

  lista = np.random.randint(0, i, i)

  start_time = perf_counter()
  lista_aleatoria = insertionSort(lista)
  end_time = perf_counter()
  aux_time = (end_time - start_time) * 1000
  temposListaAleatoriaInsertionSort.append(aux_time)

  start_time3 = perf_counter()
  lista_ordenada = insertionSort(lista_aleatoria)
  end_time3 = perf_counter()
  aux_time3 = (end_time3 - start_time3) * 1000
  temposListaOrdenadaInsertionSort.append(aux_time3)

  lista_invertida = lista_aleatoria[::-1]

  start_time2 = perf_counter()
  lista_invertida = insertionSort(lista_invertida)
  end_time2 = perf_counter()
  aux_time_invertida = (end_time2 - start_time2) * 1000
  temposListaInvertidaInsertionSort.append(aux_time_invertida)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposListaOrdenadaInsertionSort, label="Lista Ordenada")
plt.plot(size_axis, temposListaAleatoriaInsertionSort, label="Lista Aleatoria")
plt.plot(size_axis, temposListaInvertidaInsertionSort, label="Lista Invertida")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
