import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def bubbleSort(arr):
  tamanho = len(arr)
  for k in range(tamanho):
    swap = False

    for y in range(0, tamanho - k - 1):
      if arr[y] > arr[y + 1]:
        arr[y], arr[y + 1] = arr[y + 1], arr[y]
        swap = True
    if (swap == False):
      break
  return arr


temposListaOrdenada = []
temposListaInvertida = []

size_axis = []
for i in range(1000, 10001, 1000):

  size_axis.append(i)

  lista = np.random.randint(0, i, i)

  start_time = perf_counter()
  lista_ordenada = bubbleSort(lista)
  end_time = perf_counter()
  aux_time = (end_time - start_time) * 1000
  temposListaOrdenada.append(aux_time)

  lista_invertida = lista_ordenada[::-1]

  start_time2 = perf_counter()
  lista_invertida = bubbleSort(lista_invertida)
  end_time2 = perf_counter()
  aux_time_invertida = (end_time2 - start_time2) * 1000
  temposListaInvertida.append(aux_time_invertida)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposListaOrdenada, label="Lista Ordenada")
plt.plot(size_axis, temposListaInvertida, label="Lista Invertida")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
