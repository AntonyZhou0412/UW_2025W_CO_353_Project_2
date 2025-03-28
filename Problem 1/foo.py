# CO 353 Project 2.1
# Python version: 3.13.2

## Reference:
## https://stackoverflow.com/questions/20955709/algorithm-to-test-whether-g-contains-an-arborescence

from collections import deque

def find_root_node(graph, n):
    # Function to find a (potential) root node of 
    # a arborescence in a directed graph

    # Initialize all nodes as unvisited
    visited = [False] * n
    candidate = 0 # Assume 0 as the first candidate for root node
    
    # First: find a potential root node
    # Note: If a root node, the last node to finsh BFS will be a root node.
    for v in range(n):
        if not visited[v]: # If current node is not visited
            bfs(graph, v, visited) # Perform BFS starting from this node
            candidate = v # Update candidate root node to the current
    
    # Second: verify if the candidate can reach all vertices
    visited = [False] * n # Reset all nodes to unvisited
    bfs(graph, candidate, visited) # Perform BFS from the candidate
    
    # Check if all nodes are reachable from the candidate
    for v in range(n):
        if not visited[v]: # If any node remains unvisited
            return -1  # The candidate is not a root node
            
    return candidate

def bfs(graph, start, visited):
    # Implement Breadth-First Search to traverse the digraph

    queue = deque([start]) # Initialize queue with starting node
    visited[start] = True # Mark starting node as visited
    
    while queue: 
        v = queue.popleft() # Remove and get the front node
        for u in graph[v]: # For each adjacent node of v
            if not visited[u]: # If the adjacent node is not visited
                visited[u] = True # Mark it as visited
                queue.append(u) # Add it to the queue 

# Main program
def main():

    # Read the number of nodes(n) and edges (m) from input
    n, m = map(int, input().split())
    
    # Initialize the graph as an adjacent list
    graph = [[] for _ in range(n)]

    # Read m edges and construct the digraph
    for _ in range(m):
        a, b = map(int, input().split()) # Read edge
        graph[a].append(b) # Add arc from a to b
    
    # Find root node in the digraph
    r = find_root_node(graph, n)
    
    # Output the result (as request)
    if r != -1:
        print("yes")
    else:
        print("no")

# Execute the main function
if __name__ == "__main__":
    main()

