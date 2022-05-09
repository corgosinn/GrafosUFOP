from asyncio.windows_events import NULL
from dis import dis


class Grafo:

    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)]
                            for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj

    def add_aresta(self, u, v, w=1):
        """Adiciona aresta de u a v com peso w"""
        self.num_arestas += 1
        if u < self.num_vert and v < self.num_vert:
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta invalida!")

    def remove_aresta(self, u, v):
        """Remove aresta de u a v, se houver"""
        if u < self.num_vert and v < self.num_vert:
            if self.mat_adj[u][v] != 0:
                self.num_arestas += 1
                self.mat_adj[u][v] = 0
                for (v2, w2) in self.lista_adj[u]:
                    if v2 == v:
                        self.lista_adj[u].remove((v2, w2))
                        break
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)]
                            for i in range(self.num_vert)]
            # Le cada aresta do arquivo
            for i in range(0, cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])  # Vertice origem
                v = int(str[1])  # Vertice destino
                w = int(str[2])  # Peso da aresta
                self.add_aresta(u, v, w)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def busca_largura(self, s, destino):
        desc = [float("inf") for v in range(self.num_vert)]
        pred = [NULL for v in range(self.num_vert)]
        Q = [s]
        desc[s] = 0
        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == float("inf"):
                    Q.append(v)
                    desc[v] = desc[u] + 1
                    pred[v] = u
        caminho = self.print_caminho(pred, s, destino)
        self.soma_custo(caminho, 0, 1)

        return desc

    def minDist(self, dist, Q):
        min = float('inf')
        for v in range(self.num_vert):
            if dist[v] < min and Q.__contains__(v):
                min = dist[v]
                u = v
                return u

    def DIJKSTRA(self, s, destino):

        dist = [float('inf') for v in range(self.num_vert)]
        pred = [NULL for v in range(self.num_vert)]
        dist[s] = 0
        u = 0
        Q = [v for v in range(self.num_vert)]

        while(len(Q) != 0):
            u = self.minDist(dist, Q)
            Q.remove(u)

            for v in range(len(self.lista_adj[u])):
                for i in range(len(self.lista_adj[u][v])):
                    if dist[self.lista_adj[u][v][0]] > dist[u] + self.lista_adj[u][v][1]:
                        dist[self.lista_adj[u][v][0]] = dist[u] + \
                            self.lista_adj[u][v][1]
                        pred[self.lista_adj[u][v][0]] = u
        caminho = self.print_caminho(pred, s, destino)
        self.soma_custo(caminho, dist)
        return dist

    def BELLMAN_FORD(self, s, destino):
        dist = [float('inf') for v in range(self.num_vert)]
        pred = [NULL for v in range(self.num_vert)]
        dist[s] = 0
        for j in range(self.num_vert - 1):
            for u in range(len(self.lista_adj)):
                for v in range(len(self.lista_adj[u])):
                    for i in range(len(self.lista_adj[u][v])):

                        if dist[self.lista_adj[u][v][0]] > dist[u] + self.lista_adj[u][v][1]:
                            dist[self.lista_adj[u][v][0]] = dist[u] + \
                                self.lista_adj[u][v][1]
                            pred[self.lista_adj[u][v][0]] = u
        caminho = self.print_caminho(pred, s, destino)
        self.soma_custo(caminho, dist)
        return dist

    def soma_custo(self, caminho, dist, busca=0):
        custo = 0
        if (busca != 1):
            custo = dist[len(caminho)-1]
        else:
            for v in caminho:
                custo = custo + 1
        print(f"Custo: {custo}")

    def print_caminho(self, pred, origem, destino):
        x = destino
        caminho = []
        while(x != origem):
            caminho.append(x)
            x = pred[x]
        caminho.append(origem)
        caminho.reverse()

        print(f"Caminho: {caminho}")
        return caminho

    def definir_algoritmo(self, s, destino):
        busca_largura = True
        valor_negativo = False
        for x in range(len(self.lista_adj)):
            for y in range(len(self.lista_adj[x])):
                if self.lista_adj[x][y][1] != 1:
                    busca_largura = False
                if self.lista_adj[x][y][1] < 0:
                    valor_negativo = True
        if busca_largura == True:
            print("Busca largura")
            caminho = self.busca_largura(s, destino)
        elif valor_negativo == False:
            print("Dijkstra")
            caminho = self.DIJKSTRA(s, destino)
        else:
            print("Bellman Ford")
            caminho = self.BELLMAN_FORD(s, destino)
        return caminho
