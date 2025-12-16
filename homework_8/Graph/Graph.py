from collections import deque


def connected_components(graph):
    visited = set()
    comps = []

    all_v = set(graph.keys())
    for v, neigh in graph.items():
        all_v.update(neigh)

    # обходим все вершины. запускаем BFS из непосещённых
    for start in all_v:
        if start in visited:
            continue

        q = deque([start])
        visited.add(start)
        comp = []

        while q:
            v = q.popleft()
            comp.append(v)

            for to in graph.get(v, []):
                if to not in visited:
                    visited.add(to)
                    q.append(to)

        comps.append(comp)

    return comps
