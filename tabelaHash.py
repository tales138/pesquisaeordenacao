import requests
import random
import numpy as np

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
else:
  print("Erro ao fazer a solicitação HTTP:", response.status_code)


##Tabela hash de endereçamento aberto
class TabelaHashEnderecamentoAberto:

  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.tabela = [None] * tamanho

  def funcao_hash(self, chave):
    return hash(chave) % self.tamanho

  def inserir(self, chave):
    indice = self.funcao_hash(chave)

    while self.tabela[indice] is not None:
      indice = (indice + 1) % self.tamanho

    self.tabela[indice] = chave

  def pesquisar(self, chave):
    indice = self.funcao_hash(chave)

    while self.tabela[indice] is not None:
      if self.tabela[indice] == chave:
        return True
      indice = (indice + 1) % self.tamanho

    return False

  def deletar(self, chave):
    indice = self.funcao_hash(chave)

    while self.tabela[indice] is not None:
      if self.tabela[indice] == chave:
        self.tabela[indice] = None
        return
      indice = (indice + 1) % self.tamanho

  def imprimir_tabela(self):
    for i in range(self.tamanho):
      print(f"Índice {i}: {self.tabela[i]}")


tabela_enderecamento_aberto = TabelaHashEnderecamentoAberto(tamanho=1000)

for palavra in conjunto_palavras_aleatorias:
  tabela_enderecamento_aberto.inserir(palavra)

tabela_enderecamento_aberto.imprimir_tabela()

##Tabela Hash Encadeamento Separado


class No:

  def __init__(self, chave):
    self.chave = chave
    self.proximo = None


class TabelaHashEncadeamentoSeparado:

  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.tabela = [None] * tamanho

  def funcao_hash(self, chave):
    return hash(chave) % self.tamanho

  def inserir(self, chave):
    indice = self.funcao_hash(chave)

    if self.tabela[indice] is None:
      self.tabela[indice] = No(chave)
    else:
      no = self.tabela[indice]
      while no.proximo is not None:
        no = no.proximo
      no.proximo = No(chave)

  def pesquisar(self, chave):
    indice = self.funcao_hash(chave)

    no = self.tabela[indice]
    while no is not None:
      if no.chave == chave:
        return True
      no = no.proximo

    return False

  def deletar(self, chave):
    indice = self.funcao_hash(chave)

    if self.tabela[indice] is None:
      return

    if self.tabela[indice].chave == chave:
      self.tabela[indice] = self.tabela[indice].proximo
      return

    prev_no = self.tabela[indice]
    no = self.tabela[indice].proximo

    while no is not None:
      if no.chave == chave:
        prev_no.proximo = no.proximo
        return
      prev_no = no
      no = no.proximo

  def imprimir_tabela(self):
    for i in range(self.tamanho):
      print(f"Índice {i}: ", end="")
      no = self.tabela[i]
      while no is not None:
        print(no.chave, end=" => ")
        no = no.proximo
      print("None")


tabela_encadeamento_separado = TabelaHashEncadeamentoSeparado(tamanho=1000)

for palavra in conjunto_palavras_aleatorias:
  tabela_encadeamento_separado.inserir(palavra)

tabela_encadeamento_separado.imprimir_tabela()
