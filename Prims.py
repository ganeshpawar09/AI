import heapq

def prims_algo(graph):
    mini_span_tree=[]
    mst_cost=0
    min_heap=[]
    visited=set()

    heapq.heappush(min_heap, (0, 0, -1)) #weight, curr_vertex, parent

    while min_heap:
        weight, curr_vertex, parent=heapq.heappop(min_heap)

        if curr_vertex in visited:
            continue
        
        if parent != -1:
            mini_span_tree.append((parent, curr_vertex))
        
        mst_cost+=weight

        visited.add(curr_vertex)

        for vertex, weight in graph[curr_vertex]:
            if vertex not in visited:
                heapq.heappush(min_heap,(weight, vertex, curr_vertex))

    return mini_span_tree, mst_cost


if __name__=="__main__":
    # graph={}
    # vertex=int(input("Enter the number of vertices: "))
    # for i in range(vertex):
    #     adj_list=[]
    #     adj_vertex=int(input("Enter the number of adjacent vertex: "))
    #     for j in range(adj_vertex):
    #         curr_adj_vertex, curr_edge_weight=map(int, input("Enter the Adjacent Vertex and Weight of Edge (v, w): ").split())
    #         adj_list.append((curr_adj_vertex, curr_edge_weight))
    #     graph[i]=adj_list

    graph={
        0 :[(1, 1), (2, 3)],
        1 :[(0, 1), (2, 2), (3, 4)],
        2 :[(0, 3), (1, 2), (3, 5), (4, 6)],
        3 :[(1, 4), (2, 5), (4, 7)],
        4 :[(2, 6), (3, 7)]
    }

    mini_span_tree, mst_cost=prims_algo(graph)

    print("Minimum cost to create MST is: ", mst_cost)

    print("Mininimum Spanning Tree :")

    for u, v in mini_span_tree:
        print(f"{u} -> {v}")