class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):

        # self.Root.Level = 1

        def createSubTree(roditel, arr):
            if arr:
                node = BSTNode(arr[len(arr) // 2], roditel)
                if roditel is None:
                    node.Level = 1
                else:
                    node.Level = roditel.Level + 1
                node.LeftChild = createSubTree(node, arr[:(len(arr) // 2)])
                node.RightChild = createSubTree(node, arr[(len(arr) // 2) + 1:])
                return node
            else:
                return None

        a.sort()
        self.Root = createSubTree(None, a)
        return self.Root
    # создаём дерево с нуля из неотсортированного массива a
    # ...

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        def depth(root):
            if root is None:
                return 0
            return max(depth(root.LeftChild), depth(root.RightChild)) + 1

        left_side_tree = depth(root_node.LeftChild)
        right_side_tree = depth(root_node.RightChild)
        if abs(left_side_tree - right_side_tree) <= 1 and self.IsBalanced(
                root_node.LeftChild) is True and self.IsBalanced(root_node.RightChild) is True:
            return True
        return False  # сбалансировано ли дерево с корнем root_node
