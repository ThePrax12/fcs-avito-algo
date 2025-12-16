import pytest
from Graph import connected_components


def _as_sets(components):
    return set(frozenset(c) for c in components)


def _all_vertices(graph):
    verts = set(graph.keys())
    for v, neigh in graph.items():
        verts.update(neigh)
    return verts


@pytest.mark.parametrize(
    "graph, expected",
    [
        ({}, []),
        ({1: []}, [{1}]),
        ({1: [], 2: [], 3: [], 4: []}, [{1}, {2}, {3}, {4}]),
        ({1: [2]}, [{1, 2}]),
        ({1: [1], 2: [2], 3: [3]}, [{1}, {2}, {3}]),
        ({1: [1, 2, 2, 2], 2: [1]}, [{1, 2}]),
        ({1: [2], 2: []}, [{1, 2}]),
    ],
)
def test_small_cases(graph, expected):
    comps = connected_components(graph)
    assert _as_sets(comps) == set(frozenset(x) for x in expected)


def test_all_vertices_are_separate_components():
    n = 10
    graph = {i: [] for i in range(n)}

    comps = connected_components(graph)
    assert len(comps) == n
    assert _as_sets(comps) == set(frozenset({i}) for i in range(n))


def test_whole_graph_is_one_component_chain():
    n = 20
    graph = {i: [] for i in range(n)}

    for i in range(n - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)

    comps = connected_components(graph)
    assert len(comps) == 1
    assert set(comps[0]) == set(range(n))


def test_whole_graph_is_one_component_star():
    center = 0
    leaves = list(range(1, 51))
    graph = {center: leaves[:]}

    for v in leaves:
        graph[v] = [center]

    comps = connected_components(graph)
    assert len(comps) == 1
    assert set(comps[0]) == {center, *leaves}


def test_all_vertices_covered_even_if_some_are_only_neighbors():
    graph = {
        0: [100, 101],
        1: [102],
        2: [],
        3: [103, 104, 105],
        10: [106],
    }

    comps = connected_components(graph)
    union = set()
    for c in comps:
        union.update(c)

    assert union == _all_vertices(graph)


def test_no_vertex_repeats_between_components():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
        10: [],
        20: [30],
        30: [20],
    }

    comps = connected_components(graph)

    seen = set()
    for c in comps:
        for v in c:
            assert v not in seen
            seen.add(v)

    assert seen == _all_vertices(graph)
