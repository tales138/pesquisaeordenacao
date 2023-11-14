import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def countingSort(vec):

  max_value = max(vec) + 1

  contador = [0] * max_value

  for num in vec:
    contador[num] += 1

  sortedArr = []

  for i in range(max_value):
    sortedArr.extend([i] * contador[i])

  return sortedArr


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


def insertion_sort(bucket):
  for i in range(1, len(bucket)):
    key = bucket[i]
    j = i - 1
    while j >= 0 and bucket[j] > key:
      bucket[j + 1] = bucket[j]
      j -= 1
    bucket[j + 1] = key


def bucket_sort(arr):

  min_value = min(arr)
  max_value = max(arr)
  range_value = max_value - min_value

  num_buckets = len(arr)
  buckets = [[] for _ in range(num_buckets)]

  for num in arr:
    if range_value != 0:
      index = int((num - min_value) / range_value * (num_buckets - 1))
    else:
      index = 0
    buckets[index].append(num)

  for bucket in buckets:
    insertion_sort(bucket)

  sorted_arr = []
  for bucket in buckets:
    sorted_arr.extend(bucket)

  return sorted_arr


temposBucketSort = []
temposQuickSort = []
temposMergeSort = []
temposCountingSort = []
size_axis = []

for i in range(10000, 100001, 10000):
  size_axis.append(i)
  lista = np.random.randint(0, i, i)

  auxarray2 = lista.copy()
  start_time = perf_counter()
  auxarray2 = bucket_sort(auxarray2)
  end_time = perf_counter()
  temposBucketSort.append((end_time - start_time) * 1000)

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
plt.plot(size_axis, temposBucketSort, label="Bucket Sort")
plt.plot(size_axis, temposMergeSort, label="Merge Sort")
plt.plot(size_axis, temposQuickSort, label="Quick Sort")
plt.plot(size_axis, temposCountingSort, label="Counting Sort")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
