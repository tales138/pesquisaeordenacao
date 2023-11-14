import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def heap(arr, N, i):
  maior = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < N and arr[maior] < arr[l]:
    maior = l

  if r < N and arr[maior] < arr[r]:
    maior = r

  if maior != i:
    arr[i], arr[maior] = arr[maior], arr[i]

    heap(arr, N, maior)


def heapSort(arr):
  N = len(arr)

  for i in range(N // 2 - 1, -1, -1):
    heap(arr, N, i)

  for i in range(N - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heap(arr, i, 0)
  return arr


def countingSort(vec):

  max_value = max(vec) + 1

  contador = [0] * max_value

  for num in vec:
    contador[num] += 1

  sortedArr = []

  for i in range(max_value):
    sortedArr.extend([i] * contador[i])

  return sortedArr


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


temposBucketSort = []
temposQuickSort = []
temposHeapSort = []
temposCountingSort = []
size_axis = []

for i in range(10000, 100001, 10000):
  size_axis.append(i)
  lista = np.random.randint(0, i, i)

  auxarray2 = np.copy(lista)
  start_time = perf_counter()
  auxarray2 = bucket_sort(auxarray2)
  end_time = perf_counter()
  temposBucketSort.append((end_time - start_time) * 1000)

  auxarray5 = np.copy(lista)
  start_time = perf_counter()
  auxarray5 = heapSort(auxarray5)
  end_time = perf_counter()
  temposHeapSort.append((end_time - start_time) * 1000)

  auxarray4 = np.copy(lista)
  tamanho = len(auxarray4)

  start_time = perf_counter()
  auxarray4 = quickSort(auxarray4, 0, tamanho - 1)
  end_time = perf_counter()
  temposQuickSort.append((end_time - start_time) * 1000)

  auxarray6 = np.copy(lista)
  start_time = perf_counter()
  auxarray6 = countingSort(auxarray6)
  end_time = perf_counter()
  temposCountingSort.append((end_time - start_time) * 1000)

plt.figure(figsize=(20, 10))
plt.plot(size_axis, temposBucketSort, label="Bucket Sort")
plt.plot(size_axis, temposHeapSort, label="Heap Sort")
plt.plot(size_axis, temposQuickSort, label="Quick Sort")
plt.plot(size_axis, temposCountingSort, label="Counting Sort")
plt.legend(loc="upper left")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo em Milisegundos")
plt.show()
