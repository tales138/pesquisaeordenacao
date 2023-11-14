class Node:

  def __init__(self, key):
    self.key = key
    self.esquerda = None
    self.direita = None
    self.altura = 1


class ArvoreAVL:

  def __init__(self):
    self.root = None

  def inserir(self, key):
    self.root = self._inserir(self.root, key)

  def _inserir(self, node, key):
    if node is None:
      return Node(key)
    elif key < node.key:
      node.esquerda = self._inserir(node.esquerda, key)
    else:
      node.direita = self._inserir(node.direita, key)

    node.altura = 1 + max(self._altura(node.esquerda),
                          self._altura(node.direita))
    balance = self._get_balance(node)

    if balance > 1 and key < node.esquerda.key:
      return self._rotacionar_direita(node)

    if balance < -1 and key > node.direita.key:
      return self._rotacionar_esquerda(node)

    if balance > 1 and key > node.esquerda.key:
      node.esquerda = self._rotacionar_esquerda(node.esquerda)
      return self._rotacionar_direita(node)

    if balance < -1 and key < node.right.key:
      node.direita = self._rotate_right(node.direita)
      return self._rotacionar_esquerda(node)

    return node

  def remover(self, key):
    self.root = self._remover(self.root, key)

  def _remover(self, root, key):
    if root is None:
      return root

    elif key < root.key:
      root.esquerda = self._remover(root.esquerda, key)

    elif key > root.key:
      root.direita = self._remover(root.direita, key)

    else:
      if root.esquerda is None:
        temp = root.direita
        root = None
        return temp

      elif root.direita is None:
        temp = root.esquerda
        root = None
        return temp

      temp = self._get_min_value_node(root.direita)
      root.key = temp.key
      root.direita = self._remover(root.direita, temp.key)

    if root is None:
      return root

    root.altura = 1 + max(self._altura(root.esquerda),
                          self._altura(root.direita))
    balance = self._get_balance(root)

    if balance > 1 and self._get_balance(root.esquerda) >= 0:
      return self._rotacionar_direita(root)

    if balance < -1 and self._get_balance(root.direita) <= 0:
      return self._rotacionar_esquerda(root)

    if balance > 1 and self._get_balance(root.esquerda) < 0:
      root.left = self._rotacionar_esquerda(root.esquerda)
      return self._rotacionar_direita(root)

    if balance < -1 and self._get_balance(root.direita) > 0:
      root.right = self._rotacionar_direita(root.direita)
      return self._rotacionar_esquerda(root)

    return root

  def busca(self, key):
    return self._busca(self.root, key)

  def _busca(self, root, key):
    if root is None or root.key == key:
      return root is not None

    if key < root.key:
      return self._busca(root.esquerda, key)

    return self._busca(root.direita, key)

  def _altura(self, node):
    if node is None:
      return 0
    return node.altura

  def _get_balance(self, node):
    if node is None:
      return 0
    return self._altura(node.esquerda) - self._altura(node.direita)

  def _rotacionar_direita(self, z):
    y = z.esquerda
    T3 = y.direita

    y.direita = z
    z.esquerda = T3

    z.altura = 1 + max(self._altura(z.esquerda), self._altura(z.direita))
    y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

    return y

  def _rotacionar_esquerda(self, z):
    y = z.direita
    T2 = y.esquerda

    y.esquerda = z
    z.direita = T2

    z.altura = 1 + max(self._altura(z.esquerda), self._altura(z.direita))
    y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

    return y

  def _valor_minimo_no(self, node):
    if node is None or node.esquerda is None:
      return node

    return self._valor_minimo_no(node.esquerda)


arvore_avl = ArvoreAVL()

arvore_avl.inserir(10)
arvore_avl.inserir(20)
arvore_avl.inserir(30)
arvore_avl.inserir(40)
arvore_avl.inserir(50)

print(
    arvore_avl.busca(30)
)  # True // busca se o elemento 30 está contido na árvore. Deve retornar TRUE,pois o elemento 30 havia sido inserido previamente.
print(
    arvore_avl.busca(25)
)  # False // busca se o elemento 25 está contido na árvore. Deve retornar FALSE,pois o elemento 25 NÃO havia sido inserido previamente.

arvore_avl.remover(30)  # remove o elemento 30
print(
    arvore_avl.busca(30)
)  # False // busca se o elemento 30 está contido na árvore. Deve retornar FALSE,pois o elemento 30 havia sido removido da árvore previamente.
