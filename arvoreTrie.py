import requests
import random

url = "https://www.lexicodoportugues.com/downloads/lexporbr_alfa_txt.txt"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
  content = response.text

  primeiras_palavras = []
  for linha in content.splitlines():
    palavras = linha.split()
    if palavras:
      primeira_palavra = palavras[0]
      primeiras_palavras.append(primeira_palavra)

  conjunto_palavras_aleatorias = random.sample(primeiras_palavras, 1000)

  total_caracteres = sum(
      len(palavra) for palavra in conjunto_palavras_aleatorias)
  print("N°caracteres:", total_caracteres)
else:
  print("Erro ao fazer a solicitação HTTP:", response.status_code)


class NoTrie:

  def __init__(self):
    self.filhos = {}
    self.e_fim_de_palavra = False


class Trie:

  def __init__(self):
    self.raiz = NoTrie()

  def inserir(self, palavra):
    no = self.raiz
    for caractere in palavra:
      if caractere not in no.filhos:
        no.filhos[caractere] = NoTrie()
      no = no.filhos[caractere]
    no.e_fim_de_palavra = True

  def numero_de_nos(self):
    return self._contar_nos(self.raiz)

  def _contar_nos(self, no):
    if not no:
      return 0
    total = 1
    for filho in no.filhos.values():
      total += self._contar_nos(filho)
    return total


trie1 = Trie()
for palavra in conjunto_palavras_aleatorias:
  trie1.inserir(palavra)

random.shuffle(conjunto_palavras_aleatorias)

trie2 = Trie()
for palavra in conjunto_palavras_aleatorias:
  trie2.inserir(palavra)

random.shuffle(conjunto_palavras_aleatorias)

trie3 = Trie()
for palavra in conjunto_palavras_aleatorias:
  trie3.inserir(palavra)

print("N° de nós da árvore Trie 1:", trie1.numero_de_nos())
print("N° de nós da árvore Trie 2:", trie2.numero_de_nos())
print("N° de nós da árvore Trie 3:", trie3.numero_de_nos())
