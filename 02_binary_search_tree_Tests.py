class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком

    def do(self, reqkey, elem):  # в параметр "elem" нужно всегда подавать аргумент "self.root" дерева
        # (если хотим провести поиск по всему дереву)
        while elem is not None:  # проверяем, не пустой ли корень + совершается столько циклов, сколько нужно
            if elem.NodeKey == reqkey:
                self.Node = elem
                self.NodeHasKey = True
                return [self.Node, self.NodeHasKey, self.ToLeft]
            elif elem.NodeKey < reqkey:
                if elem.RightChild is not None:
                    elem = elem.RightChild
                else:
                    self.Node = elem
                    self.NodeHasKey = False
                    self.ToLeft = False
                    return [self.Node, self.NodeHasKey, self.ToLeft]
            elif elem.NodeKey > reqkey:
                if elem.LeftChild is not None:
                    elem = elem.LeftChild
                else:
                    self.Node = elem
                    self.NodeHasKey = False
                    self.ToLeft = True
                    return [self.Node, self.NodeHasKey, self.ToLeft]
        else:
            return [self.Node, self.NodeHasKey, self.ToLeft]


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        node = BSTFind().do(key, self.Root)
        if node[1] == True:
            return node[0]
        else:
            return   # возвращает BSTFind

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
        else:
            nodeinf = BSTFind().do(key, self.Root)
            if nodeinf[1] == False:
                if nodeinf[2] == True:  # Добавляем левым потомком
                    nodeinf[0].LeftChild = BSTNode(key, val, nodeinf[0])
                else:  # nodeinf[2] == False: Добавляем правым потомком
                    nodeinf[0].RightChild = BSTNode(key, val, nodeinf[0])
                return True
            else:
                return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is not None:
            if FindMax == True:
                maks = FromNode
                while maks.RightChild is not None:
                    maks = maks.RightChild
                return maks
            else:  # FindMax == False
                mnml = FromNode
                while mnml.LeftChild is not None:
                    mnml = mnml.LeftChild
                return mnml
        else:
            return None
        # ищем максимальное/минимальное (узел) в поддереве

    def DeleteNodeByKey(self, key):
        nodeinf = BSTFind().do(key, self.Root)
        if nodeinf[1] == True:
            if nodeinf[0] == self.Root:
                if nodeinf[0].RightChild is None:
                    self.Root = None
                else:  # nodeinf[0].RightChild is not None:
                    preemnik = nodeinf[0].RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild
                    preemnik.Parent = None
                    self.Root = preemnik
            else:
                roditel = nodeinf[0].Parent
                if nodeinf[0].RightChild is None:
                    preemnik = None
                else:  # nodeinf[0].RightChild is not None:
                    preemnik = nodeinf[0].RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild
                    preemnik.Parent = roditel
                if roditel.LeftChild.NodeKey == nodeinf[0].NodeKey:
                    roditel.LeftChild = preemnik
                else:
                    roditel.RightChild = preemnik
            return True
        else:
            return False  # если узел не найден
        # удаляем узел по ключу

    def Count(self):
        spisok = []
        x = self.Root
        k = 0
        if x is not None:
            spisok.append(x)
            while spisok:
                for elem in spisok:
                    for child in (elem.LeftChild, elem.RightChild):
                        if child is not None:
                            spisok.append(child)
                    spisok.remove(elem)
                    k += 1
        return k  # количество узлов в дереве


def VisBST(tree):
    spisok = []
    itogo = []
    x = tree.Root
    if x is not None:
        spisok.append(x)
        while spisok:
            for elem in spisok:
                for child in (elem.LeftChild, elem.RightChild):
                    if child is not None:
                        spisok.append(child)
                spisok.remove(elem)
                itogo.append(elem.NodeKey)
    return itogo  # Функция для печати вссех элементов в дереве


a0 = BSTNode(8, 'a0', None)  # Тестим метод COUNT для разных вариантов
s = BST(None)
print('---       Тестим метод Count()')
print(s.Count(),)
print(VisBST(s))  # Функция для вывода всех элементов дерева
print('---')
s = BST(a0)
print(s.Count(),)
print(VisBST(s))
print('---')
s.AddKeyValue(4, 'b1')
s.AddKeyValue(12, 'c1')
s.AddKeyValue(10, 'd2')
s.AddKeyValue(14, 'e2')
print(s.Count())
print(VisBST(s))
print('---      Пробуем добавить узлы с такими же ключами')
s.AddKeyValue(4, 'РРР')  # Пробуем добавить узлы с такими же ключами
s.AddKeyValue(12, 'ШШШ')
s.AddKeyValue(10, 'ДДД')
s.AddKeyValue(14, 'ААА')
print(s.Count())
print(VisBST(s))
print('---      Ищем максимальное и минимальное значения (с корня)')
ma = s.FinMinMax(s.Root, True)
mi = s.FinMinMax(s.Root, False)
print('{0}, {1}, {2}'.format(ma, ma.NodeKey, ma.NodeValue))
print('{0}, {1}, {2}'.format(mi, mi.NodeKey, mi.NodeValue))
print('---      Ищем максимальное и минимальное значения (с поддерева)')
ma = s.FinMinMax(s.Root.RightChild, True)
mi = s.FinMinMax(s.Root.RightChild, False)
print('{0}, {1}, {2}'.format(ma, ma.NodeKey, ma.NodeValue))
print('{0}, {1}, {2}'.format(mi, mi.NodeKey, mi.NodeValue))
print('---      Удаляем узел (10)')
s.DeleteNodeByKey(10)  # Удаляем узел
print(s.Count())
print(VisBST(s))
print('---      Удаляем корень (8)')
s.DeleteNodeByKey(8)  # Удаляем корень
print(s.Count())
print(VisBST(s))
print('---      Ищем несуществующий (1-ая строка) и существующий (2-ая строка) узлы')
print(s.FindNodeByKey(15))  # Ищем несуществующий узел
print('{0}, {1}, {2}'.format(s.FindNodeByKey(14),  # Ищем существующий узел
                             s.FindNodeByKey(14).NodeKey,
                             s.FindNodeByKey(14).NodeValue))

