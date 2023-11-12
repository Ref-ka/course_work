class Graph:

    # Иницилизируем объект класса Graph

    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    # Метод добавления ребра в граф

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append([v, w])
        self.graph[u] = sorted(self.graph[u])

    # Метод отображения ответа

    def print_spfa(self, dist):
        ans = 'Расстояние\n от выбранной вершины\n до остальных\n'
        for i in range(self.V):
            # if dist[i] == float('inf'):
            #     ans = 'В графе несколько\nкомпонент связности\nили\nесть вершины,\nдо которых не добраться\n' \
            #           'из заданной вершины!\nПерепроверьте\nвведенные связи!'
            #     return ans
            ans += "% d \t\t % d" % (i, dist[i]) + '\n'
        return ans

    def print_wfi(self, dist):
        ans = 'Матрица\nкратчайших расстояний\nмежду вершинами\n'
        ans += ' '.join([str(x) for x in range(self.V)])
        ans += '\n'
        ans += '\n'.join('\t'.join(map(str, row)) for row in dist)
        return ans

    # Метод получения ответа, алгоритм поиска кратчайших путей

    def spfa(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        q = list()
        q.append(src)
        counter = 0
        dist_history = list()
        dist_history.append(dist[:])
        length = {}
        while q:
            counter += 1
            u = q.pop(0)
            if u in self.graph:
                for v, w in self.graph[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        if v not in q:
                            q.append(v)
                            if v not in length:
                                length[v] = 1
                            else:
                                length[v] += 1
                            if length[v] == self.V:
                                return 'В графе есть\nотрицательный цикл!', dist_history
                            counter += 1
            dist_history.append(dist[:])
        return self.print_spfa(dist), dist_history

    def wfi(self):
        dist = []
        for i in range(self.V):
            dist.append([float('inf')] * self.V)
            dist[i][i] = 0
        for i in self.graph:
            for j, k in self.graph[i]:
                dist[i][j] = k
        for i in range(self.V):
            for j in range(self.V):
                for k in range(self.V):
                    dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
        return self.print_wfi(dist), None
