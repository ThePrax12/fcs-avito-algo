import pytest
from Dijkstra import dijkstra, restore_path


@pytest.mark.parametrize(
    "graph, start, expected_dist",
    [
        ({}, 1, {1: 0.0}),
        ({1: []}, 1, {1: 0.0}),
        ({1: [(2, 5)]}, 1, {1: 0.0, 2: 5.0}),
        (
            {1: [(2, 1)], 3: [(4, 2)]},
            1,
            {1: 0.0, 2: 1.0, 3: float("inf"), 4: float("inf")},
        ),
        ({1: [(2, 0)], 2: [(3, 0)]}, 1, {1: 0.0, 2: 0.0, 3: 0.0}),
        ({1: [(2, 10), (2, 3)]}, 1, {1: 0.0, 2: 3.0}),
        ({1: [(1, 0), (2, 2)], 2: []}, 1, {1: 0.0, 2: 2.0}),
        (
            {1: [(2, 100), (3, 1)], 3: [(2, 1)], 2: []},
            1,
            {1: 0.0, 3: 1.0, 2: 2.0},
        ),
        (
            {1: [(2, 1), (3, 5)], 2: [(3, 1)], 3: [(1, 1), (4, 2)], 4: []},
            1,
            {1: 0.0, 2: 1.0, 3: 2.0, 4: 4.0},
        ),
        (
            {1: [(2, 0), (3, 0)], 2: [(4, 1)], 3: [(4, 1)], 4: []},
            1,
            {1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0},
        ),
    ],
)
def test_dijkstra_distances(graph, start, expected_dist):
    dist, _ = dijkstra(graph, start)

    for v, d_exp in expected_dist.items():
        d_got = dist.get(v, float("inf"))
        if d_exp == float("inf"):
            assert d_got == float("inf")
        else:
            assert d_got == pytest.approx(d_exp)


def test_restore_path_exists():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }

    dist, prev = dijkstra(graph, "A")
    path = restore_path(prev, "A", "D")

    assert path == ["A", "B", "C", "D"]
    assert dist["D"] == pytest.approx(4.0)


def test_restore_path_no_path():
    graph = {
        1: [(2, 1)],
        2: [],
        10: [(11, 1)],
        11: [],
    }

    dist, prev = dijkstra(graph, 1)
    assert dist[11] == float("inf")
    assert restore_path(prev, 1, 11) == []


def test_start_not_in_keys():
    graph = {
        1: [(2, 1)],
        2: [],
    }
    dist, _ = dijkstra(graph, 999)
    assert dist[999] == pytest.approx(0.0)
    assert dist[1] == float("inf")
    assert dist[2] == float("inf")
