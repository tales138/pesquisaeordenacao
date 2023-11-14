import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def mergeSort(arr):
  if len(arr) > 1:

    midpoint = len(arr) // 2

    left = arr[:midpoint]

    right = arr[midpoint:]

    mergeSort(left)

    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1
  return arr


def particao(array, menor, maior):

  pivot = array[menor]
  i = menor - 1
  j = maior + 1

  while (True):

    i += 1
    while (array[i] < pivot):
      i += 1

    j -= 1
    while (array[j] > pivot):
      j -= 1

    if (i >= j):
      return j

    array[i], array[j] = array[j], array[i]


def quickSort(array, menor, maior):
  if (menor < maior):

    pi = particao(array, menor, maior)

    quickSort(array, menor, pi)
    quickSort(array, pi + 1, maior)
  return array


def countingSort(vec, n):
  contador = dict()

  for i in range(0, n):
    contador[i] = 0

  for i in range(0, n):
    if vec[i] in contador.keys():
      contador[vec[i]] += 1
    else:
      contador[vec[i]] = 1

  sortedArr = []
  i = 0
  while (n > 0):
    if (contador[i] == 0):
      i += 1

    else:
      sortedArr.append(i)
      contador[i] -= 1
      n = n - 1

  return sortedArr


def selectionSort(array):

  for i in range(len(array)):

    min_id = i
    for j in range(i + 1, len(array)):
      if array[min_id] > array[j]:
        min_id = j

    array[i], array[min_id] = array[min_id], array[i]
  return array


temposSelectionSort = []
temposQuickSort = []
temposMergeSort = []
temposCountingSort = []
size_axis = []

for i in range(10000, 100001, 10000):
  size_axis.append(i)
  lista = np.random.randint(0, i, i)

  auxarray2 = lista.copy()
  start_time = perf_counter()
  auxarray2 = selectionSort(auxarray2)
  end_time = perf_counter()
  temposSelectionSort.append((end_time - start_time) * 1000)

  auxarray5 = lista.copy()
  start_time = perf_counter()
  auxarray5 = mergeSort(auxarray5)
  end_time = perf_counter()
  temposMergeSort.append((end_time - start_time) * 1000)

  auxarray4 = lista.copy()
  tamanho = len(auxarray4)

  start_time = perf_counter()
  auxarray4 = quickSort(auxarray4, 0, tamanho - 1)
  end_time = perf_counter()
  temposQuickSort.append((end_time - start_time) * 1000)

  auxarray6 = lista.copy()
  start_time = perf_counter()
  auxarray6 = countingSort(auxarray6, len(auxarray6))
  end_time = perf_counter()
  temposCountingSort.append((end_time - start_time) * 1000)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposSelectionSort, label="Selection Sort")
plt.plot(size_axis, temposMergeSort, label="Merge Sort")
plt.plot(size_axis, temposQuickSort, label="Quick Sort")
plt.plot(size_axis, temposCountingSort, label="Counting Sort")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
