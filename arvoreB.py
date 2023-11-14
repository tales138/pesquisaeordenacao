class NoB:

  def __init__(self, folha=False):
    self.chaves = []
    self.filhos = []
    self.folha = folha

  def inserir_elemento(self, chave):
    if not self.chaves:
      self.chaves.append(chave)
    else:
      i = len(self.chaves) - 1
      while i >= 0 and self.chaves[i] > chave:
        i -= 1
      if self.folha:
        self.chaves.insert(i + 1, chave)
      else:
        if i + 1 < len(self.filhos):
          if len(self.filhos[i + 1].chaves) == 2:
            self.dividir_filho(i + 1, self.filhos[i + 1])
            if chave > self.chaves[i + 1]:
              i += 1
          self.filhos[i + 1].inserir_elemento(chave)
        else:
          novo_no = NoB(folha=True)
          self.filhos.append(novo_no)
          novo_no.inserir_elemento(chave)

  def dividir_filho(self, indice, no):
    novo_no = NoB(folha=no.folha)
    self.filhos.insert(indice + 1, novo_no)
    self.chaves.insert(indice, no.chaves[1])
    novo_no.chaves = no.chaves[2:]
    no.chaves = no.chaves[:1]
    if not no.folha:
      novo_no.filhos = no.filhos[2:]
      no.filhos = no.filhos[:2]

  def buscar_elemento(self, chave):
    i = 0
    while i < len(self.chaves) and chave > self.chaves[i]:
      i += 1
    if i < len(self.chaves) and chave == self.chaves[i]:
      return True
    elif self.folha:
      return False
    else:
      return self.filhos[i].buscar_elemento(chave)

  def remover_elemento(self, chave):
    i = 0
    while i < len(self.chaves) and chave > self.chaves[i]:
      i += 1
    if i < len(self.chaves) and chave == self.chaves[i]:
      if self.folha:
        self.chaves.pop(i)
      else:
        self.remover_elemento_interno(i)
    elif self.folha:
      return False
    else:
      return self.remover_elemento_interno(i)

  def remover_elemento_interno(self, indice):
    filho_esquerdo = self.filhos[indice]
    filho_direito = self.filhos[indice + 1]

    if len(filho_esquerdo.chaves) > 1:
      predecessor = filho_esquerdo.chaves.pop()
      self.chaves[indice] = predecessor
    elif len(filho_direito.chaves) > 1:
      sucessor = filho_direito.chaves.pop(0)
      self.chaves[indice] = sucessor
    else:
      uniao = filho_esquerdo.chaves + [self.chaves[indice]
                                       ] + filho_direito.chaves
      self.chaves.pop(indice)
      self.filhos.pop(indice + 1)

      meio = len(uniao) // 2
      self.chaves.insert(indice, uniao[meio])
      novo_no = NoB(self.folha)

      novo_no.chaves = uniao[meio + 1:]
      novo_no.filhos = filho_esquerdo.filhos + filho_direito.filhos
      self.filhos.insert(indice + 1, novo_no)

  def __str__(self):
    return str(self.chaves)


class ArvoreB:

  def __init__(self):
    self.raiz = NoB(folha=True)

  def inserir_elemento(self, chave):
    raiz = self.raiz
    if len(raiz.chaves) == 2:
      novo_no = NoB()
      self.raiz = novo_no
      novo_no.filhos.append(raiz)
      novo_no.inserir_elemento(chave)
    else:
      raiz.inserir_elemento(chave)

  def buscar_elemento(self, chave):
    return self.raiz.buscar_elemento(chave)

  def remover_elemento(self, chave):
    return self.raiz.remover_elemento(chave)

  def __str__(self):
    return str(self.raiz)


arvore = ArvoreB()

arvore.inserir_elemento(10)
arvore.inserir_elemento(5)
arvore.inserir_elemento(7)
arvore.inserir_elemento(20)

print(
    arvore.buscar_elemento(7)
)  # Verifica se o elemento 7 está contido na árvore. Deve retornar True,pois o elemento 7 foi inserido previamente.
print(
    arvore.buscar_elemento(15)
)  # Verifica se o elemento 15 está contido na árvore. Deve retornar False,pois o elemento 15 não foi inserido previamente.

arvore.remover_elemento(7)  #remove o elemento 7
print(
    arvore.buscar_elemento(7)
)  # Verifica se o elemento 7 está contido na árvore. Deve retornar False,pois o elemento 7 foi removido previamente.
