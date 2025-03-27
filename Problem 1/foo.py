import sys

def find_mother_vertex(graph, n):
    # Mark all vertices as unvisited
    visited = [False] * n
    candidate = 0
    
    # First DFS to find a potential mother vertex
    for v in range(n):
        if not visited[v]:
            dfs(graph, v, visited)
            candidate = v
    
    # Verify if candidate can reach all vertices
    visited = [False] * n
    dfs(graph, candidate, visited)
    
    for v in range(n):
        if not visited[v]:
            return -1  # candidate is not a mother vertex
            
    return candidate

def dfs(graph, v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(graph, u, visited)

# Main program
def main():
    sys.setrecursionlimit(10**6)  # Increase recursion limit for large graphs
    
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
