import random
import math

def RandomizedMaxCut(n, edges):
    c = 2
    num_trials = max(1, int(c * math.log(n,2)))

    for _ in range(num_trials):
        S = set()
        for v in range(1, n + 1):
            if random.random() < 0.5:
                S.add(v)
    return S

def GreedyMaxCut(n, edges):
    adj = [[] for _ in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    in_set_S = [False] * (n+1)

    for v in range(1, n+1):
        count_in_S = 0
        count_not_in_S = 0

        for u in adj[v]:
            if u < v:
                if in_set_S[u]:
                    count_in_S += 1
                else:
                    count_not_in_S += 1
        
        in_set_S[v] = (count_in_S <= count_not_in_S)
        S = {v for v in range(1, n+1) if in_set_S[v]}
    return S

def calculate_cut_size(S, edges):
    cut_size = 0
    for u, v in edges:
        if (u in S and v not in S) or (u not in S and v in S):
            cut_size += 1
    return cut_size

def main():
    # Read input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Run both algorithms
    S_randomized = RandomizedMaxCut(n, edges)
    S_greedy = GreedyMaxCut(n, edges)

    # Calculate cut sizes
    cut_size_randomized = calculate_cut_size(S_randomized, edges)
    cut_size_greedy = calculate_cut_size(S_greedy, edges)

    # Choose the better result
    if cut_size_randomized >= cut_size_greedy:
        S = S_randomized
    else:
        S = S_greedy

    # Output the result
    print(len(S))
    print(' '.join(map(str, sorted(S))))

if __name__ == "__main__":
    main()
