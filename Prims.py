import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = []
    mst_cost = 0
    mst = []

    # Start from vertex 0
    heapq.heappush(min_heap, (0, 0, -1))  # (weight, vertex, parent)

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)
        if visited[vertex]:
            continue
        if parent != -1:
            mst.append((parent, vertex))
        
        mst_cost += weight
        visited[vertex] = True

        for neighbour, weight in graph[vertex]:
            if not visited[neighbour]:
                heapq.heappush(min_heap, (weight, neighbour, vertex))

    return mst_cost, mst

def build_graph():
    graph = {}
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency list for each vertex (vertex weight), one vertex per line:")
    for i in range(n):
        adjacency_list = []
        adjacency_vertex = int(input(f"Enter the number of adjacent vertices for vertex {i}: "))
        for edge in range(adjacency_vertex):
            vertex = int(input("Enter the adjacent vertex: "))
            weight = int(input(f"Enter the weight from {i} to {vertex}: "))
            adjacency_list.append((vertex, weight))
        graph[i] = adjacency_list
    return graph

if __name__=="__main__":
    # graph = build_graph()
    graph = {
        0: [(1, 2), (2, 1)],
        1: [(0, 2), (2, 1)],
        2: [(0, 1), (1, 1)]
    }
    mst_cost, mst = prim(graph)
    print("Minimum Spanning Tree Cost:", mst_cost)
    print("Minimum Spanning Tree Edges:")
    for edge in mst:
        print(edge)
