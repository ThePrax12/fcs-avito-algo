def cycle_or_toposort(graph):
    nodes = []
    seen = set()

    def add(x):
        if x not in seen:
            seen.add(x)
            nodes.append(x)

    for u, vs in graph.items():
        add(u)
        for v in vs:
            add(v)

    adj = {u: list(graph.get(u, [])) for u in nodes}

    color = {u: 0 for u in nodes}  # 0-не были, 1-в стеке, 2-вышли
    parent = {}
    topo = []
    cycle = None

    def dfs(u):
        nonlocal cycle
        color[u] = 1
        for v in adj[u]:
            if cycle is not None:
                return
            if color[v] == 0:
                parent[v] = u
                dfs(v)
            elif color[v] == 1:
                path = [v]
                cur = u
                while cur != v:
                    path.append(cur)
                    cur = parent[cur]
                path.append(v)
                path.reverse()
                cycle = path
                return
        color[u] = 2
        topo.append(u)

    for u in nodes:
        if color[u] == 0:
            parent[u] = u
            dfs(u)
            if cycle is not None:
                return "cycle", cycle

    topo.reverse()
    return "topo", topo
