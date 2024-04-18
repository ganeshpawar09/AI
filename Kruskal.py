def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal_mst(graph):
    result = []
    graph = sorted(graph, key=lambda item: item[2])
    parent = [i for i in range(len(graph))]
    rank = [0] * len(graph)

    for u, v, w in graph:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result

def main():
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))

    graph = []
    print("Enter edges in the format 'u v w', where u and v are vertices and w is weight:")
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    mst = kruskal_mst(graph)
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

if __name__ == "__main__":
    main()
