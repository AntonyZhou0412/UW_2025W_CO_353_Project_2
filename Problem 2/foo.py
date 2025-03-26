import random

def RandomizedMaxCut(n, edges):
    S = set()
    for v in range(1, n + 1):
        if random.random() < 0.5:
            S.add(v)
    return S

def GreedyMaxCut(n, edges):
    S = set()
    neighbors = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    for v in range(1, n + 1):
        count_S = sum(1 for neighbor in neighbors[v] if neighbor in S)
        count_notS = sum(1 for neighbor in neighbors[v] if neighbor not in S)
        if count_S <= count_notS:
            S.add(v)

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
