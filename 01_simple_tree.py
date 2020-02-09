class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        if root is None or root is SimpleTreeNode:
            self.Root = root  # корень, может быть None
        else:
            raise TypeError

    def AddChild(self, ParentNode, NewChild):
        if self.Root is not None:
            node = self.FindNode(ParentNode)
        else:
            return
        node.Children.append(NewChild)
        NewChild.Parent = node
        return
        # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if self.Root is not None:
            node = self.FindNode(NodeToDelete)
            if node == self.Root:
                self.Root = None
            else:
                node.Parent.Children.remove(node)
                del node
            return
        else:
            return
        # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):

        def appendnodetolist(x, s):
            s.append(x)
            for children in x.Children:
                appendnodetolist(children, s)
            return s

        if self.Root is not None:
            lst = []
            lst = appendnodetolist(self.Root, lst)
            return lst
        else:
            return [None]
        # ваш код выдачи всех узлов дерева в определённом порядке

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        return []

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        pass

    def Count(self):
        # количество всех узлов в дереве
        return 0

    def LeafCount(self):
        # количество листьев в дереве
        return 0

    def FindNode(self, val):

        def findtreenode(x, neededtreenode):                # Воспользуемся рекурсией!
            if x.NodeValue == neededtreenode:
                return x
            else:
                for children in x.Children:
                    findtreenode(children, neededtreenode)
                return

        if self.Root is not None:
            node = findtreenode(self.Root, val)
            return node
        else:
            return
