class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        i = 0
        while i < self.Tree.__len__():  # проверяем, не пустой ли корень + совершается столько циклов, сколько нужно
            if self.Tree[i] is None:
                return -i
            elif key == self.Tree[i]:
                return i
            elif key > self.Tree[i]:
                i = i * 2 + 2
            elif key < self.Tree[i]:
                i = i * 2 + 1
        else:  # ищем в массиве индекс ключа
            return None  # не найден

    def AddKey(self, key):
        # добавляем ключ в массив
        num = self.FindKeyIndex(key)
        if num is None:
            return -1
        elif num == 0:
            if self.Tree[num] is None:
                self.Tree[num] = key
                return num
            else:
                return num
        elif num < 0:
            self.Tree[-num] = key
            return -num
        elif num > 0:
            return num
        # индекс добавленного/существующего ключа или -1 если не удалось
