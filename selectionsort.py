import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def selectionSort(array):

  for i in range(len(array)):

    min_id = i
    for j in range(i + 1, len(array)):
      if array[min_id] > array[j]:
        min_id = j

    array[i], array[min_id] = array[min_id], array[i]
  return array


temposListaAleatoriaInsertionSort = []
temposListaOrdenadaInsertionSort = []
temposListaInvertidaInsertionSort = []

size_axis = []
for i in range(1000, 10001, 1000):
  size_axis.append(i)

  lista = np.random.randint(0, i, i)

  start_time = perf_counter()
  lista1 = selectionSort(lista)
  end_time = perf_counter()

  temposListaAleatoriaInsertionSort.append((end_time - start_time) * 1000)

  start_time2 = perf_counter()
  lista2 = selectionSort(lista1)
  end_time2 = perf_counter()

  temposListaOrdenadaInsertionSort.append((end_time2 - start_time2) * 1000)

  lista_invertida = lista1[::-1]

  start_time3 = perf_counter()
  lista_invertida = selectionSort(lista_invertida)
  end_time3 = perf_counter()

  temposListaInvertidaInsertionSort.append((end_time3 - start_time3) * 1000)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposListaOrdenadaInsertionSort, label="Ordenado")
plt.plot(size_axis, temposListaAleatoriaInsertionSort, label="Aleatorio")
plt.plot(size_axis, temposListaInvertidaInsertionSort, label="Invertido")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
