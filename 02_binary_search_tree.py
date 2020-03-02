class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self, reqkey, elem):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо добавить новый узел левым потомком
        while elem is not None:  # проверяем, не пустой ли корень + совершается столько циклов, сколько нужно
            if elem.NodeKey == reqkey:
                self.Node = elem
                self.NodeHasKey = True
                break
            elif elem.NodeKey < reqkey:
                if elem.RightChild is not None:
                    elem = elem.RightChild
                else:
                    self.Node = elem
                    self.NodeHasKey = False
                    self.ToLeft = False
                    break
            elif elem.NodeKey > reqkey:
                if elem.LeftChild is not None:
                    elem = elem.LeftChild
                else:
                    self.Node = elem
                    self.NodeHasKey = False
                    self.ToLeft = True
                    break

class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        node = BSTFind(key, self.Root)
        return node  # возвращает BSTFind

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
        else:
            nodeinf = self.FindNodeByKey(key)
            if nodeinf.NodeHasKey == False:
                if nodeinf.ToLeft == True:  # Добавляем левым потомком
                    nodeinf.Node.LeftChild = BSTNode(key, val, nodeinf.Node)
                else:  # nodeinf.ToLeft == False: Добавляем правым потомком
                    nodeinf.Node.RightChild = BSTNode(key, val, nodeinf.Node)
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
        nodeinf = self.FindNodeByKey(key)
        if nodeinf.NodeHasKey == True:
            if nodeinf.Node == self.Root:
                if nodeinf.Node.RightChild is None:
                    self.Root = None
                else:  # nodeinf.Node.RightChild is not None:
                    preemnik = nodeinf.Node.RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild
                    preemnik.Parent = None
                    self.Root = preemnik
            else:
                roditel = nodeinf.Node.Parent
                if nodeinf.Node.RightChild is None:
                    preemnik = None
                else:  # nodeinf[0].RightChild is not None:
                    preemnik = nodeinf.Node.RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild
                    preemnik.Parent = roditel
                if roditel.LeftChild == nodeinf.Node:
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
