class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def push(self, value):
        self.stack.append(value)
        return


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        try:
            ind = self.vertex.index(None)
        except ValueError:
            return False
        self.vertex[ind] = Vertex(v)
        return True
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex

        # здесь и далее, параметры v -- индекс вершины

    # в списке  vertex
    def RemoveVertex(self, v):
        if 0 <= v < self.max_vertex:
            self.vertex[v] = None
            self.m_adjacency[v] = [0] * self.max_vertex
            for el in self.m_adjacency:
                el[v] = 0
            return True
        else:
            return False
        # ваш код удаления вершины со всеми её рёбрами

    def IsEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
                return True
            else:
                return False
        else:
            return False
        # True если есть ребро между вершинами v1 и v2

    def AddEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2

    def RemoveEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2

    def DepthFirstSearch(self, VFrom, VTo):
        st = Stack()
        for elem in self.vertex:  # Убираем Hit в каждом узле
            if elem is not None:
                elem.Hit = False

        def step(VOt, VDo):
            nonlocal st
            self.vertex[VOt].Hit = True
            st.push(self.vertex[VOt])
            for i in range(self.max_vertex):
                if self.m_adjacency[VOt][i] == 1 and self.vertex[i].Hit == False:
                    if self.vertex[i] == self.vertex[VDo]:
                        st.push(self.vertex[i])
                        return st.stack
                    else:
                        step(i, VDo)
                        if st.stack[-1] == self.vertex[VDo]:
                            return st.stack
            st.pop()
            return st.stack

        # def dfs(Vn, Vk):  # Более быстрый и компактный код, но не трушный поиск в глубину
        #     nonlocal st
        #     self.vertex[Vn].Hit = True
        #     st.push(self.vertex[Vn])
        #     if self.m_adjacency[Vn][Vk] == 1:  # Из-за вот этой проверки
        #         st.push(self.vertex[Vk])
        #         return st.stack
        #     else:
        #         for i in range(self.max_vertex):
        #             if self.m_adjacency[Vn][i] == 1 and self.vertex[i].Hit is False:
        #                 dfs(i, Vk)
        #                 if st.stack[-1] == self.vertex[Vk]:
        #                     return st.stack
        #     st.pop()
        #     return st.stack

        return step(VFrom, VTo)
# узлы задаются позициями в списке vertex
# возвращается список узлов -- путь из VFrom в VTo
# или [] если пути нет
