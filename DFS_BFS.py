import queue
def dfs(graph, currVertex, visited=set()):
    print(currVertex, end="  ")
    visited.add(currVertex)
    for adjVertex in graph[currVertex]:
        if adjVertex not in visited:
            dfs(graph, adjVertex, visited)

def bfs(graph, currVertex):
    visited=set()
    que= queue.Queue()
    que.put(currVertex)
    visited.add(currVertex)

    while que:
        frontVertex=que.get()
        print(frontVertex, end="  ")
        for adjVertex in graph[frontVertex]:
            if adjVertex not in visited:
                que.put(adjVertex)
                visited.add(adjVertex)

if __name__=="__main__":
    graph={}
    vertex=int(input("Enter the number of vertex: "))
    for i in range (vertex):
        adjacent_list=list(map(int, input(f"Enter the adjacent vertices of vertex {i} :")))
        graph[i]=adjacent_list

    print("\nDFS of given graph: ")
    dfs(graph, 0)
    print("\nBFS of given graph: ")
    bfs(graph, 0)