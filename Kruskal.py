class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def kruskal_mst(graph):
    result = []
    graph = sorted(graph, key=lambda item: item[2])
    ds = DisjointSet(len(graph))

    for u, v, w in graph:
        if ds.find(u) != ds.find(v):
            result.append([u, v, w])
            ds.union(u, v)

    return result

def main():
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))

    graph = []
    for i in range(m):
        u=int(input(f"Enter the starting Index of edge {i} :"))
        v=int(input(f"Enter the ending Index of edge {i} :"))
        w=int(input(f"Enter the weight of edge {i} :"))
        graph.append((u, v, w))

    mst = kruskal_mst(graph)
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

if __name__ == "__main__":
    main()
