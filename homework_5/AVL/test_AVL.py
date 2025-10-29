from AVL import AVL
import pytest


@pytest.mark.parametrize(
    "keys, search_key, expected",
    [
        ([10], 10, True),
        ([10], 5, False),
        ([10, 5, 15], 5, True),
        ([10, 5, 15], 15, True),
        ([10, 5, 15], 20, False),
        ([1, 2, 3, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 6, False),
        ([], 1, False),
    ],
)
def test_search(keys, search_key, expected):
    """Тест на поиск по дереву"""
    avl = AVL()
    for key in keys:
        avl.insert(key)
    assert avl.search(search_key) == expected


@pytest.mark.parametrize(
    "keys, expected_searches",
    [
        ([10], [10]),
        ([10, 5], [10, 5]),
        ([10, 5, 15], [10, 5, 15]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
    ],
)
def test_insert(keys, expected_searches):
    """Тест на вставку значения"""
    avl = AVL()
    for key in keys:
        avl.insert(key)

    for key in expected_searches:
        assert avl.search(key) == True


@pytest.mark.parametrize(
    "insert_keys, delete_key, remaining_keys",
    [
        ([10], 10, []),
        ([10, 5], 5, [10]),
        ([10, 5], 10, [5]),
        ([10, 5, 15], 10, [5, 15]),
        ([10, 5, 15, 3, 7], 5, [10, 15, 3, 7]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ],
)
def test_delete(insert_keys, delete_key, remaining_keys):
    """Тест на удаление значений"""
    avl = AVL()

    for key in insert_keys:
        avl.insert(key)

    avl.delete(delete_key)

    assert avl.search(delete_key) == False

    for key in remaining_keys:
        assert avl.search(key) == True


@pytest.mark.parametrize(
    "keys",
    [
        ([1, 2, 3, 4, 5, 6, 7]),
        ([7, 6, 5, 4, 3, 2, 1]),
        ([4, 2, 6, 1, 3, 5, 7]),
        ([10, 20, 30, 40, 50, 25]),
    ],
)
def test_balance_property(keys):
    """Тест что дерево остается сбалансированным"""
    avl = AVL()

    for key in keys:
        avl.insert(key)
        if avl.root:
            assert abs(avl.balance(avl.root)) <= 1


def test_duplicate_insert():
    """Тест что дубликаты не добавляются"""
    avl = AVL()
    avl.insert(10)
    avl.insert(10)
    avl.insert(5)
    avl.insert(5)

    assert avl.search(10) == True
    assert avl.search(5) == True


def test_delete_nonexistent():
    """Тест удаления несуществующего элемента"""
    avl = AVL()
    avl.insert(10)
    avl.insert(5)

    avl.delete(20)

    assert avl.search(10) == True
    assert avl.search(5) == True
    assert avl.search(20) == False
