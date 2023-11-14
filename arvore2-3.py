class No23:

  def __init__(self, valor):
    self.valores = [valor]
    self.filhos = []

  def eh_folha(self):
    return len(self.filhos) == 0


class Arvore23:

  def __init__(self):
    self.raiz = None

  def pesquisar(self, valor):
    return self.pesquisar_no(valor, self.raiz)

  def pesquisar_no(self, valor, no):
    if no is None:
      return False

    for i in range(len(no.valores)):
      if valor == no.valores[i]:
        return True
      elif valor < no.valores[i]:
        return self.pesquisar_no(valor, no.filhos[i])
    return self.pesquisar_no(valor, no.filhos[-1]) if no.filhos else False

  def inserir(self, valor):
    if self.raiz is None:
      self.raiz = No23(valor)
    else:
      no, valor_promovido = self.inserir_no(valor, self.raiz)
      if valor_promovido:
        nova_raiz = No23(valor_promovido)
        nova_raiz.filhos.append(self.raiz)
        nova_raiz.filhos.append(no)
        self.raiz = nova_raiz

  def inserir_no(self, valor, no):
    if no.eh_folha():
      no.valores.append(valor)
      no.valores.sort()
      if len(no.valores) > 2:
        meio = len(no.valores) // 2
        valor_promovido = no.valores[meio]
        novo_no = No23(no.valores.pop(meio))
        return novo_no, valor_promovido
      else:
        return None, None
    else:
      for i in range(len(no.valores)):
        if valor < no.valores[i]:
          no_filho, valor_promovido = self.inserir_no(valor, no.filhos[i])
          if valor_promovido:
            no.valores.insert(i, valor_promovido)
            no.filhos.insert(i + 1, no_filho)
            if len(no.valores) > 2:
              meio = len(no.valores) // 2
              valor_promovido = no.valores[meio]
              novo_no = No23(no.valores.pop(meio))
              novo_no.filhos.append(no.filhos.pop(meio + 1))
              return novo_no, valor_promovido
          return None, None
      no_filho, valor_promovido = self.inserir_no(valor, no.filhos[-1])
      if valor_promovido:
        no.valores.append(valor_promovido)
        no.filhos.append(no_filho)
        if len(no.valores) > 2:
          meio = len(no.valores) // 2
          valor_promovido = no.valores[meio]
          novo_no = No23(no.valores.pop(meio))
          novo_no.filhos.append(no.filhos.pop(meio + 1))
          return novo_no, valor_promovido
      return None, None

  def deletar(self, valor):
    self.raiz = self.deletar_no(valor, self.raiz)

  def deletar_no(self, valor, no):
    if no is None:
      return None

    for i in range(len(no.valores)):
      if valor == no.valores[i]:
        if no.eh_folha():
          no.valores.pop(i)
          return self.balancear_arvore(no)
        else:
          antecessor = self.maximo(no.filhos[i])
          no.valores[i] = antecessor
          no.filhos[i] = self.deletar_no(antecessor, no.filhos[i])
          return self.balancear_arvore(no)
      elif valor < no.valores[i]:
        no.filhos[i] = self.deletar_no(valor, no.filhos[i])
        return self.balancear_arvore(no)
    no.filhos[-1] = self.deletar_no(valor, no.filhos[-1])
    return self.balancear_arvore(no)

  def balancear_arvore(self, no):
    if len(no.valores) == 0:
      return no.filhos[0]
    elif len(no.valores) == 1:
      if no.filhos:
        filho = no.filhos[0]
        if len(filho.valores) == 1:
          no.valores.append(filho.valores[0])
          no.valores.sort()
          no.filhos = filho.filhos
    elif len(no.valores) == 2:
      if no.filhos:
        filho1 = no.filhos[0]
        filho2 = no.filhos[1]
        if len(filho1.valores) == 1 and len(filho2.valores) == 1:
          no.valores.insert(0, filho1.valores[0])
          no.valores.append(filho2.valores[0])
          no.filhos = filho1.filhos + filho2.filhos
    return no

  def maximo(self, no):
    if no is None:
      return None
    if no.eh_folha():
      return no.valores[-1]
    else:
      return self.maximo(no.filhos[-1])


#inserindo elemento na ávore
arvore = Arvore23()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print(
    arvore.pesquisar(7)
)  # Verifica se o valor 7 está contido na árvore. Como o valor 7 foi adicionado à árvore previamente deve retornar TRUE.
print(
    arvore.pesquisar(8)
)  # Verifica se o valor 8 está contido na árvore. Como o valor 8 NÃO foi adicionado à árvore previamente deve retornar FALSE.

arvore.deletar(7)
print(
    arvore.pesquisar(7)
)  # Deve retornar FALSE,pois o elemento 7 foi removido da árvore previamente pelo método deletar()
