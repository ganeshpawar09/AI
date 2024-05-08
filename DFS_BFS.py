import queue
def DFS(currEle, graph, visited=set()):
    print(currEle, end=' ')
    visited.add(currEle)
    for neighbour in graph[currEle]:
        if neighbour not in visited:
            DFS(neighbour, graph, visited)

def BFS(currEle, graph):
    visited = set()
    que = queue.Queue()
    visited.add(currEle)
    que.put(currEle)
    
    while queue:
        s = que.get()
        print(s, end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                que.put(neighbour)
                visited.add(neighbour)

if __name__ == "__main__":
    # graph = {}
    
    # n = int(input("Enter the number of vertices: "))
    # print("Enter the adjacency list for each vertex (vertex neighbours separated by space), one vertex per line:")
    # for i in range(n):
    #     adjacency_list = list(map(int, input(f"Enter neighbours for vertex {i}: ").split()))
    #     graph[i] = adjacency_list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("DFS traversal:")
    DFS('A', graph)
    print("\nBFS traversal:")
    BFS('A', graph)
   
    
