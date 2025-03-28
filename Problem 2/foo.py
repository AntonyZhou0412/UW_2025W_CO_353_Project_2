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

def GreedyImproveCut(n, edges, S):
    # Create adjacency list
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)  
        adj[v].append(u)  

    improved = True  # Flag to check if improvement was made

    # Continue loop until no improvement can be made
    while improved:
        improved = False  # Initially assume no improvement

        # Check each vertex to see if flipping its set membership improves the cut
        for v in range(1, n+1):
            cnt_in = 0  # Number of neighbors of v currently in set S

            # Count how many neighbors of v are in set S
            for u in adj[v]:
                if u in S:
                    cnt_in += 1

            cnt_total = len(adj[v])  # Total number of neighbors of v
            cnt_not = cnt_total - cnt_in  # Number of neighbors of v not in set S

            # Calculate the potential gain of flipping vertex v's set membership
            if v in S:
                # If v is currently in S, flipping it moves it out of S
                # Current contribution is number of neighbors outside S (cnt_not)
                # After flipping, contribution becomes number of neighbors inside S (cnt_in)
                gain = cnt_in - cnt_not
            else:
                # If v is currently not in S, flipping it moves it into S
                # Current contribution is number of neighbors inside S (cnt_in)
                # After flipping, contribution becomes number of neighbors outside S (cnt_not)
                gain = cnt_not - cnt_in

            # Flip vertex v if gain is positive (improves the cut size)
            if gain > 0:
                if v in S:
                    S.remove(v)  # Remove v from set S
                else:
                    S.add(v)     # Add v to set S

                improved = True  # Mark that we made an improvement in this iteration

    # Return improved set S and its corresponding cut size
    return S, calculate_cut_size(S, edges)

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
        S, improved_cut_size = GreedyImproveCut(n, edges, S_randomized)

    # Output the result
    print(len(S))
    print(' '.join(map(str, sorted(S))))

if __name__ == "__main__":
    main()
