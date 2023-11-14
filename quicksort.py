import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


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


def insertionSort(arr):

  for i in range(1, len(arr)):

    key = arr[i]
    k = i - 1
    while k >= 0 and key < arr[k]:
      arr[k + 1] = arr[k]
      k -= 1

    arr[k + 1] = key

  return arr


def selectionSort(array):

  for i in range(len(array)):

    min_id = i
    for j in range(i + 1, len(array)):
      if array[min_id] > array[j]:
        min_id = j

    array[i], array[min_id] = array[min_id], array[i]
  return array


temposBubbleSort = []
temposInsertionSort = []
temposSelectionSort = []
temposQuickSort = []

size_axis = []
for i in range(10000, 100001, 10000):
  size_axis.append(i)

  lista = np.random.randint(0, i, i)

  auxarray = lista.copy()
  start_time = perf_counter()
  lista1 = bubbleSort(auxarray)
  end_time = perf_counter()
  temposBubbleSort.append((end_time - start_time) * 1000)

  auxarray2 = lista.copy()
  start_time = perf_counter()
  auxarray2 = selectionSort(auxarray2)
  end_time = perf_counter()
  temposSelectionSort.append((end_time - start_time) * 1000)

  auxarray3 = lista.copy()
  start_time = perf_counter()
  auxarray3 = insertionSort(auxarray3)
  end_time = perf_counter()
  temposInsertionSort.append((end_time - start_time) * 1000)

  auxarray4 = lista.copy()
  tamanho = len(auxarray4)

  start_time = perf_counter()
  auxarray4 = quickSort(auxarray4, 0, tamanho - 1)
  end_time = perf_counter()
  temposQuickSort.append((end_time - start_time) * 1000)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposBubbleSort, label="Bubble Sort")
plt.plot(size_axis, temposSelectionSort, label="Selection Sort")
plt.plot(size_axis, temposInsertionSort, label="Insertion Sort")
plt.plot(size_axis, temposQuickSort, label="Quick Sort")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
