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
            if reqkey == elem.NodeKey:
                self.Node = elem
                self.NodeHasKey = True
                break
            elif reqkey > elem.NodeKey:
                if elem.RightChild is not None:
                    elem = elem.RightChild
                else:
                    self.Node = elem
                    self.NodeHasKey = False
                    self.ToLeft = False
                    break
            else:  # reqkey < elem.NodeKey:
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
            return True
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
        inf = self.FindNodeByKey(key)
        if inf.NodeHasKey:
            delnode = inf.Node

            if delnode == self.Root:
                if delnode.RightChild is None:
                    if delnode.LeftChild is None:
                        self.Root = None
                    else:  # delnode.LeftChild is not None:
                        delnode.LeftChild.Parent = None
                        self.Root = delnode.LeftChild
                else:  # delnode.RightChild is not None:
                    preemnik = delnode.RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild

                    if preemnik.Parent == delnode:
                        if delnode.LeftChild is not None:
                            preemnik.LeftChild = delnode.LeftChild
                            delnode.LeftChild.Parent = preemnik
                        preemnik.Parent = None
                        self.Root = preemnik
                    else:  # preemnik.Parent != delnode:
                        rodpreem = preemnik.Parent

                        if preemnik.RightChild is None:
                            rodpreem.LeftChild = None
                            if delnode.LeftChild is not None:
                                preemnik.LeftChild = delnode.LeftChild
                                delnode.LeftChild.Parent = preemnik
                            preemnik.RightChild = delnode.RightChild
                            delnode.RightChild.Parent = preemnik
                            preemnik.Parent = None
                            self.Root = preemnik
                        else:  # preemnik.RightChild is not None:
                            naslednik = preemnik.RightChild
                            rodpreem.LeftChild = naslednik
                            naslednik.Parent = rodpreem
                            if delnode.LeftChild is not None:
                                preemnik.LeftChild = delnode.LeftChild
                                delnode.LeftChild.Parent = preemnik
                            preemnik.RightChild = delnode.RightChild
                            delnode.RightChild.Parent = preemnik
                            preemnik.Parent = None
                            self.Root = preemnik

            else:  # delnode != self.Root:
                roddel = delnode.Parent
                if delnode == roddel.LeftChild:
                    svyazLeft = True
                else:
                    svyazLeft = False

                if delnode.RightChild is None:
                    if delnode.LeftChild is None:
                        if svyazLeft:
                            roddel.LeftChild = None
                        else:
                            roddel.RightChild = None
                    else:  # delnode.LeftChild is not None:
                        if svyazLeft:
                            roddel.LeftChild = delnode.LeftChild
                            delnode.LeftChild.Parent = roddel
                        else:
                            roddel.RightChild = delnode.LeftChild
                            delnode.LeftChild.Parent = roddel
                else:  # delnode.RightChild is not None:
                    preemnik = delnode.RightChild
                    while preemnik.LeftChild is not None:
                        preemnik = preemnik.LeftChild

                    if preemnik.Parent == delnode:
                        if delnode.LeftChild is not None:
                            preemnik.LeftChild = delnode.LeftChild
                            delnode.LeftChild.Parent = preemnik
                        if svyazLeft:
                            roddel.LeftChild = preemnik
                        else:
                            roddel.RightChild = preemnik
                        preemnik.Parent = roddel
                    else:  # preemnik.Parent != delnode:
                        rodpreem = preemnik.Parent

                        if preemnik.RightChild is None:
                            rodpreem.LeftChild = None
                            if delnode.LeftChild is not None:
                                preemnik.LeftChild = delnode.LeftChild
                                delnode.LeftChild.Parent = preemnik
                            preemnik.RightChild = delnode.RightChild
                            delnode.RightChild.Parent = preemnik
                            if svyazLeft:
                                roddel.LeftChild = preemnik
                            else:
                                roddel.RightChild = preemnik
                            preemnik.Parent = roddel
                        else:  # preemnik.RightChild is not None:
                            naslednik = preemnik.RightChild
                            rodpreem.LeftChild = naslednik
                            naslednik.Parent = rodpreem
                            if delnode.LeftChild is not None:
                                preemnik.LeftChild = delnode.LeftChild
                                delnode.LeftChild.Parent = preemnik
                            preemnik.RightChild = delnode.RightChild
                            delnode.RightChild.Parent = preemnik
                            if svyazLeft:
                                roddel.LeftChild = preemnik
                            else:
                                roddel.RightChild = preemnik
                            preemnik.Parent = roddel

            return True
        else:
            return False  # если узел не найден
        # удаляем узел по ключу

    def Count(self):
        spisok = []
        if self.Root is not None:
            spisok.append(self.Root)
            for elem in spisok:
                for child in (elem.LeftChild, elem.RightChild):
                    if child is not None:
                        spisok.append(child)
        return len(spisok) # количество узлов в дереве
