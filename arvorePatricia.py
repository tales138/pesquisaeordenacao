import requests
import random
import numpy as np


class NoPatricia:

  def __init__(self, chave):
    self.chave = chave
    self.esquerda = None
    self.direita = None
    self.e_folha = False


def inserir_palavra(raiz, palavra):
  if raiz is None:
    return NoPatricia(palavra)

  no_atual = raiz
  while True:
    tamanho_prefixo = obter_tamanho_prefixo(palavra, no_atual.chave)

    if tamanho_prefixo == len(no_atual.chave):
      palavra = palavra[tamanho_prefixo:]
      if no_atual.direita is None:
        no_atual.direita = NoPatricia(palavra)
        no_atual.direita.e_folha = True
        break
      else:
        no_atual = no_atual.direita
    else:
      if tamanho_prefixo > 0:
        prefixo = no_atual.chave[:tamanho_prefixo]
        no_atual.chave = no_atual.chave[tamanho_prefixo:]
        novo_no = NoPatricia(prefixo)

        if tamanho_prefixo == len(palavra):
          novo_no.e_folha = True
          novo_no.direita = NoPatricia(palavra)
        else:
          novo_no.direita = NoPatricia(palavra[tamanho_prefixo:])

        novo_no.esquerda = no_atual
        return novo_no

      if no_atual.esquerda is None:
        no_atual.esquerda = NoPatricia(palavra)
        no_atual.esquerda.e_folha = True
        break
      else:
        no_atual = no_atual.esquerda

  return raiz


def obter_tamanho_prefixo(palavra1, palavra2):
  tamanho = min(len(palavra1), len(palavra2))
  for i in range(tamanho):
    if palavra1[i] != palavra2[i]:
      return i
  return tamanho


def contar_nos(raiz):
  if raiz is None:
    return 0

  contagem = 1
  if raiz.e_folha:
    return contagem

  contagem += contar_nos(raiz.esquerda)
  contagem += contar_nos(raiz.direita)

  return contagem


url = "https://www.lexicodoportugues.com/downloads/lexporbr_alfa_txt.txt"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
  conteudo = response.text

  primeiras_palavras = []
  for linha in conteudo.splitlines():
    palavras = linha.split()
    if palavras:
      primeira_palavra = palavras[0]
      primeiras_palavras.append(primeira_palavra)

  primeiras_palavras = np.array(primeiras_palavras)

  conjunto_palavras_aleatorias = np.random.choice(primeiras_palavras,
                                                  size=1000,
                                                  replace=False)

  total_caracteres = np.sum(np.vectorize(len)(conjunto_palavras_aleatorias))
  print("Total de caracteres do conjunto de palavras selecionado:",
        total_caracteres)

  np.random.shuffle(conjunto_palavras_aleatorias)
  raiz1 = None
  for palavra in conjunto_palavras_aleatorias:
    raiz1 = inserir_palavra(raiz1, palavra)

  np.random.shuffle(conjunto_palavras_aleatorias)
  raiz2 = None
  for palavra in conjunto_palavras_aleatorias:
    raiz2 = inserir_palavra(raiz2, palavra)

  np.random.shuffle(conjunto_palavras_aleatorias)
  raiz3 = None
  for palavra in conjunto_palavras_aleatorias:
    raiz3 = inserir_palavra(raiz3, palavra)

  nos1 = contar_nos(raiz1)
  nos2 = contar_nos(raiz2)
  nos3 = contar_nos(raiz3)

  print("N° de nós da árvore Patricia 1:", nos1)
  print("N° de nós da árvore Patricia 2:", nos2)
  print("N° de nós da árvore Patricia 3:", nos3)
else:
  print("Erro ao fazer a solicitação HTTP:", response.status_code)
