import pytest
from stack_vs_queue import LinkedList


def test_queue_basic_operations():
    q = LinkedList()

    assert q.is_empty()
    assert len(q) == 0
    assert q.peek_left() is None

    q.append_right(1)
    q.append_right(2)
    q.append_right(3)

    assert not q.is_empty()
    assert len(q) == 3

    assert q.peek_left() == 1

    assert q.pop_left() == 1
    assert len(q) == 2
    assert q.pop_left() == 2
    assert q.pop_left() == 3

    assert q.is_empty()
    assert len(q) == 0

    assert q.pop_left() is None
    assert q.peek_left() is None


def test_stack_basic_operations():

    s = LinkedList()

    assert s.is_empty()
    s.append_left("a")
    s.append_left("b")
    s.append_left("c")

    assert len(s) == 3
    assert s.peek_left() == "c"

    assert s.pop_left() == "c"
    assert s.pop_left() == "b"
    assert s.pop_left() == "a"

    assert s.is_empty()
    assert s.pop_left() is None


def test_len_and_internal_size_consistency():
    ll = LinkedList()
    assert len(ll) == 0

    for i in range(5):
        ll.append_right(i)
        assert len(ll) == i + 1

    for i in range(5):
        ll.pop_left()
        assert len(ll) == 4 - i

    assert len(ll) == 0


def test_mixed_operations_consistency():
    ll = LinkedList()

    ll.append_right(10)
    ll.append_left(20)
    ll.append_right(30)

    assert len(ll) == 3
    assert ll.pop_left() == 20
    assert ll.peek_left() == 10
    assert ll.pop_left() == 10
    assert ll.pop_left() == 30
    assert ll.pop_left() is None
    assert ll.is_empty()
