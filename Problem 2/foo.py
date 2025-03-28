# CO 353 Project 2.1
# Python version: 3.13.2

import random
import math

def RandomizedMaxCut(n, edges):
    # Run one trial of randomized algorithm
    
    S = set() # Initialize empty set S
    for v in range(1, n + 1): # Iterate through all vertices from 1 to n
        if random.random() < 0.5: 
            S.add(v) # Randomly add vertex to S with 50% probability
    cut_size = calculate_cut_size(S, edges) # Calculate the size of the cut
    return S, cut_size

def GreedyMaxCut(n, edges):

    # Initialize adjacency list for each vertex
    adj = [[] for _ in range(n+1)] 
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    in_set_S = [False] * (n+1) # Track which vertices are in set S

    for v in range(1, n+1): # Iterate through all vertices
        count_in_S = 0 # Counter for neighbors in set S
        count_not_in_S = 0 # Counter for neighbor not in set S

        for u in adj[v]: # Check each neighbor of vertex v
            if u < v: # Avoid double counting
                if in_set_S[u]:
                    count_in_S += 1 
                else:
                    count_not_in_S += 1
        
        # Put v in S if it has fewer or equal neighbors in S
        in_set_S[v] = (count_in_S <= count_not_in_S) 
    
    S = {v for v in range(1, n+1) if in_set_S[v]} # S = in_set_S
    cut_size = calculate_cut_size(S, edges) # Calculate the size of the cut
    return S, cut_size

def calculate_cut_size(S, edges):
    cut_size = 0
    for u, v in edges: # Iterate through all edges
        if (u in S and v not in S) or (u not in S and v in S): # Check if edge crosses the cut
            cut_size += 1
    return cut_size # Return the total cut size

def main():

    # Read input
    n, m = map(int, input().split()) # Read number of vertices and edges
    edges = [] # Initialize empty list to store edges
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Run randomized algorithm once
    S_randomized, cut_size_randomized = RandomizedMaxCut(n, edges)

    # Check if randomized result satisfies the condition
    if cut_size_randomized >= len(edges) / 2:
        S = S_randomized
    else:
        # Run greedy algorithm if randomized result is insufficient
        S_greedy, cut_size_greedy = GreedyMaxCut(n, edges)
        S = S_greedy

    # Output the result
    print(len(S))
    print(' '.join(map(str, sorted(S))))

if __name__ == "__main__":
    main()
