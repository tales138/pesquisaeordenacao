class No:

  def __init__(self, folha=False):
    self.pares = []
    self.filhos = []
    self.folha = folha

  def inserir(self, par):
    self.pares.append(par)
    self.pares.sort(key=lambda x: x[0])

  def dividir(self):
    esquerda = No()
    direita = No()
    meio = len(self.pares) // 2
    chave_meio, _ = self.pares[meio]
    esquerda.pares = self.pares[:meio]
    direita.pares = self.pares[meio:]
    if self.folha:
      esquerda.filhos = self.filhos[:meio + 1]
      direita.filhos = self.filhos[meio + 1:]
    return chave_meio, esquerda, direita

  def __lt__(self, other):
    return self.pares[0][0] < other.pares[0][0]


class ArvoreBMais:

  def __init__(self):
    self.raiz = No(folha=True)

  def inserir(self, chave, valor):
    par = (chave, valor)
    if chave in [par[0] for par in self.raiz.pares]:

      return

    if len(self.raiz.pares) == 3:
      chave_meio, esquerda, direita = self.raiz.dividir()
      self.raiz = No()
      self.raiz.inserir((chave_meio, None))
      self.raiz.filhos = [esquerda, direita]

    noh = self.raiz
    while not noh.folha:
      indice = 0
      while indice < len(noh.pares) and chave > noh.pares[indice][0]:
        indice += 1
      noh = noh.filhos[indice]

    noh.inserir(par)
    if len(noh.pares) == 3:
      chave_meio, esquerda, direita = noh.dividir()
      noh.inserir((chave_meio, None))
      noh.filhos = [esquerda, direita]

  def buscar(self, chave):
    noh = self.raiz
    while not noh.folha:
      indice = 0
      while indice < len(noh.pares) and chave > noh.pares[indice][0]:
        indice += 1
      noh = noh.filhos[indice]

    for par in noh.pares:
      if chave == par[0]:
        return True

    return False

  def deletar(self, chave):
    noh = self.raiz
    while not noh.folha:
      indice = 0
      while indice < len(noh.pares) and chave > noh.pares[indice][0]:
        indice += 1
      noh = noh.filhos[indice]

    for i, par in enumerate(noh.pares):
      if chave == par[0]:
        del noh.pares[i]
        break


arvore = ArvoreBMais()

arvore.inserir(12, "Elemento 1")
arvore.inserir(21, "Elemento 2")
arvore.inserir(50, "Elemento 3")
arvore.inserir(65, "Elemento 4")
arvore.inserir(85, "Elemento 5")

print(arvore.buscar(
    12))  #Deve retornar True pois o elemento 12 foi inserido previamente.
print(arvore.buscar(
    21))  # Deve retornar True pois o elemento 21 foi inserido previamente.
print(arvore.buscar(
    50))  # Deve retornar True pois o elemento 50 foi inserido previamente.
print(arvore.buscar(
    65))  # Deve retornar True pois o elemento 65 foi inserido previamente.
print(arvore.buscar(
    85))  # Deve retornar True pois o elemento 85 foi inserido previamente.
print(arvore.buscar(
    30))  # Deve retornar Fase pois o elemento 30 não foi inserido previamente.

arvore.deletar(50)  #Exclui o valor 50 da árvore

print(arvore.buscar(
    12))  # Deve retornar True,pois o valor 12 não foi excluido da árvore
print(arvore.buscar(
    50))  # Deve retornar False,pois o valor 50 foi excluido da árvore.
