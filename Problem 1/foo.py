from collections import deque

def find_mother_vertex(graph, n):
    # Mark all vertices as unvisited
    visited = [False] * n
    candidate = 0
    
    # First pass to find a potential mother vertex
    for v in range(n):
        if not visited[v]:
            bfs(graph, v, visited)
            candidate = v
    
    # Verify if candidate can reach all vertices
    visited = [False] * n
    bfs(graph, candidate, visited)
    
    for v in range(n):
        if not visited[v]:
            return -1  # candidate is not a mother vertex
            
    return candidate

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)

# Main program
def main():
    n, m = map(int, input().split())
    
    # Construct graph
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    r = find_mother_vertex(graph, n)
    
    if r != -1:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
