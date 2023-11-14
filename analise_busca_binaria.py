import numpy as np
import matplotlib.pyplot as plt


def busca_binaria(lista, valor):
  esquerda = 0
  direita = len(lista) - 1
  num_operacoes = 0

  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    num_operacoes += 1

    if lista[meio] == valor:
      return num_operacoes
    elif lista[meio] < valor:
      esquerda = meio + 1
    else:
      direita = meio - 1

  return -1


tamanhos = np.arange(10000, 100001, 10000)
num_elementos = 4
num_amostras = 100

media_operacoes = []

for tamanho in tamanhos:
  lista = np.sort(np.random.randint(1, tamanho * 10, tamanho))
  total_operacoes = 0

  for _ in range(num_amostras):
    elementos_aleatorios = np.random.choice(lista,
                                            size=num_elementos,
                                            replace=False)

    for elemento in elementos_aleatorios:
      num_operacoes = busca_binaria(lista, elemento)
      total_operacoes += num_operacoes

  media = total_operacoes / (num_elementos * num_amostras)
  media_operacoes.append(media)

# Plotando o gráfico
plt.plot(tamanhos, media_operacoes, marker='o')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Número Médio de Operações')
plt.title('Variação do Número de Operações na Busca Binária')
plt.grid(True)
plt.show()
