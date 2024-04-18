import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = []
    mst_cost = 0
    mst = []

    # Start from vertex 0
    heapq.heappush(min_heap, (0, 0))  # (weight, vertex)

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        mst_cost += weight
        visited[u] = True

        if len(mst) < n - 1:
            mst.append((u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst_cost, mst

def build_graph():
    graph = []
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency list for each vertex (vertex weight), one vertex per line:")
    for i in range(n):
        adjacency_list = []
        edges = input(f"Enter edges for vertex {i}: ").split()
        for edge in edges:
            vertex, weight = map(int, edge.split())
            adjacency_list.append((vertex, weight))
        graph.append(adjacency_list)
    return graph

graph = build_graph()
mst_cost, mst = prim(graph)
print("Minimum Spanning Tree Cost:", mst_cost)
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)
