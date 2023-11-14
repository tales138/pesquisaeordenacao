import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def countingsort(arr, exp1):

  k = len(arr)

  output = [0] * (k)

  count = [0] * (10)
  for i in range(0, k):
    index = arr[i] // exp1
    count[index % 10] += 1

  for i in range(1, 10):
    count[i] += count[i - 1]

  i = k - 1
  while i >= 0:
    index = arr[i] // exp1
    output[count[index % 10] - 1] = arr[i]
    count[index % 10] -= 1
    i -= 1

  i = 0
  for i in range(0, len(arr)):
    arr[i] = output[i]
  return arr


def radixSort(arr):

  max1 = max(arr)

  exp = 1
  array = []
  while max1 / exp >= 1:
    array = countingsort(arr, exp)
    exp *= 10
  return array


def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_arr = arr[:mid].copy()
    right_arr = arr[mid:].copy()

    merge_sort(left_arr)
    merge_sort(right_arr)

    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
      if left_arr[i] < right_arr[j]:
        arr[k] = left_arr[i]
        i += 1
      else:
        arr[k] = right_arr[j]
        j += 1
      k += 1

    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1

    while j < len(right_arr):
      arr[k] = right_arr[j]
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


def countingSort(vec):

  max_value = max(vec) + 1

  contador = [0] * max_value

  for num in vec:
    contador[num] += 1

  sortedArr = []

  for i in range(max_value):
    sortedArr.extend([i] * contador[i])

  return sortedArr


temposRadixSort = []
temposQuickSort = []
temposMergeSort = []
temposCountingSort = []
size_axis = []

for i in range(10000, 100001, 10000):
  size_axis.append(i)
  lista = np.random.randint(0, i, i)

  auxarray2 = lista.copy()
  start_time = perf_counter()
  auxarray2 = radixSort(auxarray2)
  end_time = perf_counter()
  temposRadixSort.append((end_time - start_time) * 1000)

  auxarray5 = lista.copy()
  start_time = perf_counter()
  auxarray5 = merge_sort(auxarray5)
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
  auxarray6 = countingSort(auxarray6)
  end_time = perf_counter()
  temposCountingSort.append((end_time - start_time) * 1000)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposRadixSort, label="Radix Sort")
plt.plot(size_axis, temposMergeSort, label="Merge Sort")
plt.plot(size_axis, temposQuickSort, label="Quick Sort")
plt.plot(size_axis, temposCountingSort, label="Counting Sort")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
