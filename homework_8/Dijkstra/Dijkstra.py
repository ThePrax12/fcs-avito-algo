import heapq


def dijkstra(graph, start):
    # ищем кратчайший путь
    vertices = set(graph.keys())
    for v, edges in graph.items():
        for to, w in edges:
            vertices.add(to)

    vertices.add(start)

    dist = {v: float("inf") for v in vertices}
    prev = {v: None for v in vertices}

    dist[start] = 0.0
    pq = [(0.0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        if d != dist[v]:
            continue

        for to, w in graph.get(v, []):
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                prev[to] = v
                heapq.heappush(pq, (nd, to))

    return dist, prev


def restore_path(prev, start, end):
    # восстанавливаем сам путь
    if start == end:
        return [start]

    if end not in prev:
        return []

    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    if path[-1] != start:
        return []

    path.reverse()
    return path
