class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * (2 ** (depth + 1) - 1)
        a.sort(reverse=True)
        for i in range(min(len(a), (2 ** (depth + 1) - 1))):
            self.Add(a[i])
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1  # если куча пуста
        else:
            if self.HeapArray[len(self.HeapArray) - 1] is not None:
                indLast = len(self.HeapArray) - 1
            else:
                indLast = self.HeapArray.index(None) - 1

            if indLast == 0:
                znach = self.HeapArray[0]
                self.HeapArray[0] = None
                return znach
            else:
                znach = self.HeapArray[0]
                self.HeapArray[0] = self.HeapArray[indLast]
                self.HeapArray[indLast] = None

                def sitoDown(arr, x, leva, prav):
                    if (arr[leva] is None) and (arr[prav] is None):
                        return
                    elif (arr[leva] is not None) and (arr[prav] is None):
                        if arr[x] < arr[leva]:
                            arr[x], arr[leva] = arr[leva], arr[x]
                        return
                    elif (arr[leva] is not None) and (arr[prav] is not None):
                        if arr[leva] > arr[prav]:
                            if arr[x] < arr[leva]:
                                arr[x], arr[leva] = arr[leva], arr[x]
                                x = leva
                                leva = x * 2 + 1
                                prav = x * 2 + 2
                            else:
                                return
                        elif arr[prav] >= arr[leva]:
                            if arr[x] < arr[prav]:
                                arr[x], arr[prav] = arr[prav], arr[x]
                                x = prav
                                prav = x * 2 + 2
                                leva = x * 2 + 1
                            else:
                                return
                        if prav < len(arr):
                            sitoDown(arr, x, leva, prav)

                sitoDown(self.HeapArray, 0, 1, 2)
                return znach
        # вернуть значение корня и перестроить кучу

    def Add(self, key):
        if len(self.HeapArray) == 0 or self.HeapArray[len(self.HeapArray) - 1] is not None:
            return False  # если куча вся заполнена
        else:
            if self.HeapArray[0] is None:
                self.HeapArray[0] = key
            else:
                startIndex = self.HeapArray.index(None)
                parentIndex = (startIndex - 1) // 2

                def sitoUp(arr, el, newInd, oldInd):
                    if el <= arr[oldInd]:
                        arr[newInd] = el
                        return
                    else:
                        arr[newInd] = arr[oldInd]
                        arr[oldInd] = el
                        newInd = oldInd
                        oldInd = (newInd - 1) // 2
                        if oldInd >= 0:
                            sitoUp(arr, el, newInd, oldInd)
                        else:
                            return

                sitoUp(self.HeapArray, key, startIndex, parentIndex)
            return True
        # добавляем новый элемент key в кучу и перестраиваем её
