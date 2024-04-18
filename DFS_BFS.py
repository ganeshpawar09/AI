def DFS(currEle, graph, visited=set()):
    print(currEle, end=' ')
    visited.add(currEle)
    for neighbour in graph[currEle]:
        if neighbour not in visited:
            DFS(neighbour, graph, visited)

def BFS(currEle, graph):
    visited = set()
    queue = []
    visited.add(currEle)
    queue.append(currEle)
    
    while queue:
        s = queue.pop(0)
        print(s, end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

if __name__ == "__main__":
    graph = {}
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency list for each vertex (vertex neighbours separated by space), one vertex per line:")
    for i in range(n):
        adjacency_list = list(map(int, input(f"Enter neighbours for vertex {i}: ").split()))
        graph[i] = adjacency_list

    print("DFS traversal:")
    DFS(0, graph)
    print("\nBFS traversal:")
    BFS(0, graph)
