import heapq

# Arista: dlr[u][v]
dlr = {
    'A': {'A':0,   'B':1.8, 'C':2.5, 'D':2.8, 'E':4.5, 'F':5.0, 'G':3.0, 'H':5.5},
    'B': {'A':1.8, 'B':0,   'C':4.4, 'D':5.6, 'E':3.5, 'F':2.3, 'G':4.5, 'H':3.2},
    'C': {'A':2.5, 'B':4.4, 'C':0,   'D':3.8, 'E':3.4, 'F':8.0, 'G':6.3, 'H':7.7},
    'D': {'A':2.8, 'B':5.6, 'C':3.8, 'D':0,   'E':7.7, 'F':8.0, 'G':2.8, 'H':10.0},
    'E': {'A':4.5, 'B':3.5, 'C':3.4, 'D':7.7, 'E':0,   'F':6.7, 'G':8.6, 'H':4.0},
    'F': {'A':5.0, 'B':2.3, 'C':8.0, 'D':8.0, 'E':6.7, 'F':0,   'G':5.3, 'H':3.5},
    'G': {'A':3.0, 'B':4.5, 'C':6.3, 'D':2.8, 'E':8.6, 'F':5.3, 'G':0,   'H':6.6},
    'H': {'A':5.5, 'B':3.2, 'C':7.7, 'D':10.0,'E':4.0, 'F':3.5, 'G':6.6, 'H':0  },
}

graph = {
    "A": ["B", "G"],
    "B": ["A", "E", "F"],
    "C": ["D", "E"],
    "D": ["C", "G"],
    "E": ["B", "C", "H"],
    "F": ["B", "H", "G"],
    "G": ["A", "D", "F"],
    "H": ["E", "F"],
}


def best_first_search(start, goal):
    """Búsqueda preferente por lo mejor (Best-First Search usando sólo heurística h)."""
    # Frontier: (h, g, nodo, camino)
    frontier = [(dlr[start][goal], 0, start, [start])]
    visited = set()

    while frontier:
        _, g, u, path = heapq.heappop(frontier)
        if u in visited:
            continue
        visited.add(u)

        if u == goal:
            return path, g

        for v in graph[u]:
            if v not in visited:
                g2 = g + dlr[u][v]
                h2 = dlr[v][goal]
                heapq.heappush(frontier, (h2, g2, v, path + [v]))
    return None


def greedy_search(start, goal):
    frontier = [(0, start, [start])]  # (g, nodo, camino)
    best_g = {start: 0}

    while frontier:
        g, u, path = heapq.heappop(frontier)
        if u == goal:
            return path, g

        for v in graph[u]:
            g2 = g + dlr[u][v]
            if g2 < best_g.get(v, float("inf")):
                best_g[v] = g2
                heapq.heappush(frontier, (g2, v, path + [v]))
    return None


def astar_search(start, goal):
    frontier = [(dlr[start][goal], 0, start, [start])]  # (f, g, nodo, camino)
    best_g = {start: 0}

    while frontier:
        _, g, u, path = heapq.heappop(frontier)
        if u == goal:
            return path, g

        for v in graph[u]:
            g2 = g + dlr[u][v]
            if g2 < best_g.get(v, float("inf")):
                best_g[v] = g2
                f2 = g2 + dlr[v][goal]
                heapq.heappush(frontier, (f2, g2, v, path + [v]))
    return None


if __name__ == "__main__":
    print("Estados disponibles:\n", graph)

    start = input("Estado inicial: ").strip().upper()
    goal = input("Estado meta: ").strip().upper()

    print("\nPreferente por lo mejor:", best_first_search(start, goal))
    print("\nBúsqueda avara:", greedy_search(start, goal))
    print("\nA*:", astar_search(start, goal))
