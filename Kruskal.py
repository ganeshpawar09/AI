class DisJointSet():
    def __init__(self, vertex):
        self.vertex=vertex
        self.parent=[i for i in range(vertex)]
        self.rank=[0]*vertex
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u_root=self.find(u)
        v_root=self.find(v)

        if u_root==v_root:
            return
        
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root]=u_root
        elif self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root]=v_root
        else:
            self.parent[v_root]=u_root
            self.rank[u_root]+=1
        
def kruskal_algo(graph, vertex):
    mini_span_tree=[]
    mst_cost=0

    graph=sorted(graph, key=lambda item:item[2])
    ds=DisJointSet(vertex)

    for u, v, w in graph:
        if ds.find(u)!=ds.find(v):
            mini_span_tree.append((u, v))
            mst_cost+=w
        ds.union(u, v)
    
    return mini_span_tree, mst_cost

if __name__=="__main__":
    # graph=[]
    # vertex=int(input("Enter the number of vertices: "))
    # edges=int(input("Enter the number of edges: "))
    # print
    # for i in range(edges):
    #     starting_vertex, ending_vertex, weight=map(int, input("Enter the edges starting, ending vertex and weight: ").split())
    #     graph.append((starting_vertex, ending_vertex, weight))
    vertex=5
    graph = [
        (0, 1, 2), 
        (0, 3, 4), 
        (1, 2, 3), 
        (1, 3, 1), 
        (1, 4, 5), 
        (2, 4, 6), 
        (3, 4, 7)  
    ]

    mini_span_tree, mst_cost=kruskal_algo(graph, vertex)

    print("Minimum cost to create MST is: ", mst_cost)

    print("Mininimum Spanning Tree :")

    for u, v in mini_span_tree:
        print(f"{u} -> {v}")