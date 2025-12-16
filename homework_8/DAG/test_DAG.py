import pytest

from DAG import cycle_or_toposort


def is_valid_toposort(graph, order):
    pos = {v: i for i, v in enumerate(order)}

    nodes = set(graph.keys())
    for u, vs in graph.items():
        for v in vs:
            nodes.add(v)

    if set(order) != nodes:
        return False

    for u, vs in graph.items():
        for v in vs:
            if pos[u] > pos[v]:
                return False
    return True


def is_cycle_in_graph(graph, cycle):
    if not cycle or len(cycle) < 2 or cycle[0] != cycle[-1]:
        return False

    for a, b in zip(cycle, cycle[1:]):
        if b not in graph.get(a, []):
            return False
    return True


@pytest.mark.parametrize(
    "graph",
    [
        {},
        {1: []},
        {1: [2], 2: []},
        {1: [2, 3], 2: [4], 3: [4], 4: []},
        {1: [2], 2: [3], 3: [], 10: []},
        {1: [2], 2: [], 3: [4]},
    ],
)
def test_toposort_when_no_cycle(graph):
    kind, res = cycle_or_toposort(graph)
    assert kind == "topo"
    assert is_valid_toposort(graph, res)


@pytest.mark.parametrize(
    "graph",
    [
        {1: [1]},
        {1: [2], 2: [1]},
        {10: [11], 11: [12], 12: [10]},
        {1: [2], 2: [3], 3: [2]},
        {1: [2], 2: [], 3: [4], 4: [3]},
        {1: [2], 2: [3], 3: [], 10: [11], 11: [10]},
        {1: [2], 2: [3], 3: [4], 4: [2]},
        {1: [2], 2: [3], 3: [1], 3: [1, 4], 4: []},
        {1: [2, 3], 2: [4], 4: [2], 3: []},
    ],
)
def test_cycle_when_exists(graph):
    kind, cycle = cycle_or_toposort(graph)
    assert kind == "cycle"
    assert is_cycle_in_graph(graph, cycle)


def test_cycle_preferred_over_toposort():
    graph = {1: [2], 2: [3], 3: [1], 10: []}
    kind, res = cycle_or_toposort(graph)
    assert kind == "cycle"
    assert is_cycle_in_graph(graph, res)


def test_vertices_only_in_neighbors_are_included_in_topo():
    graph = {1: [2]}
    kind, res = cycle_or_toposort(graph)
    assert kind == "topo"
    assert set(res) == {1, 2}
    assert is_valid_toposort(graph, res)


def test_non_int_vertices_work():
    graph = {"A": ["B"], "B": ["C"], "C": []}
    kind, res = cycle_or_toposort(graph)
    assert kind == "topo"
    assert is_valid_toposort(graph, res)
