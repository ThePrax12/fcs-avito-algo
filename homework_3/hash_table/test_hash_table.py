import pytest
from hash_table import HashTable


@pytest.mark.parametrize(
    "key,value",
    [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        (42, "int key"),
        ((1, 2), "tuple key"),
    ],
)
def test_add_and_get(key, value):
    ht = HashTable()
    ht.add(key, value)
    assert ht.get(key) == value
    assert ht.get("nonexistent") is None


@pytest.mark.parametrize(
    "initial,updated",
    [
        (100, 200),
        ("old", "new"),
        ((1, 2), (3, 4)),
    ],
)
def test_update_value(initial, updated):
    ht = HashTable()
    ht.add("key", initial)
    assert ht.get("key") == initial
    ht.add("key", updated)
    assert ht.get("key") == updated


@pytest.mark.parametrize(
    "keys,values", [(["x", "y"], [10, 20]), (["a", "b", "c"], [1, 2, 3])]
)
def test_delete(keys, values):
    ht = HashTable()
    for k, v in zip(keys, values):
        ht.add(k, v)

    for k, v in zip(keys, values):
        deleted = ht.delete(k)
        assert deleted == v
        assert ht.get(k) is None

    assert ht.delete("nonexistent") is None


def test_len_and_count():
    ht = HashTable()
    assert len(ht) == 0
    ht.add("a", 1)
    ht.add("b", 2)
    assert len(ht) == 2
    ht.delete("a")
    assert len(ht) == 1


def test_rehash():
    ht = HashTable(size=2)
    keys = ["k1", "k2", "k3", "k4"]
    values = [1, 2, 3, 4]
    for k, v in zip(keys, values):
        ht.add(k, v)

    for k, v in zip(keys, values):
        assert ht.get(k) == v

    assert ht.size >= 4


def test_collision_handling():
    ht = HashTable(size=1)
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    for k, v in zip(keys, values):
        ht.add(k, v)
    for k, v in zip(keys, values):
        assert ht.get(k) == v


@pytest.mark.parametrize("bad_key", [[1, 2, 3], {"a": 1}, {1, 2, 3}])
def test_unhashable_key(bad_key):
    ht = HashTable()
    with pytest.raises(TypeError):
        ht.add(bad_key, "value")
