import pytest
from package_class.Class_printqueue import *


@pytest.fixture
def pq():
    return PrintQueue


@pytest.fixture
def node():
    return PrintQueue.Node


@pytest.fixture
def data():
    return PrintDocument


# Тест class PrintDocument
def test_data_init(data):
    expected_1 = 'PEP484'
    expected_2 = 500

    data = data('PEP484',500)

    res_1 = data.document
    res_2 = data.number_page

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


# Тест class PrintQueue.Node
def test_node_init(node, data):
    expected_1 = 'PEP484'
    expected_2 = None

    data = data('PEP484', 500)
    node = node(data)

    res_1 = node.data.document
    res_2 = node.prev

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


# Тест class PrintQueue
def test_queue_isempty(pq):
    expected = True

    pq = pq()

    res = pq.is_empty()

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_enqueue_isempty(pq, data):
    expected_1 = 1
    expected_2 = 'PEP484'

    data = data('PEP484', 500)
    pq = pq()
    pq.enqueue(data)

    res_1 = pq.count
    res_2 = pq.head.data.document

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_enqueue(pq, data):
    expected_1 = 2
    expected_2 = 'Рекурсия'

    data1 = data('PEP484', 500)
    data2 = data('Рекурсия', 75)
    pq = pq()
    pq.enqueue(data1), pq.enqueue(data2)

    res_1 = pq.count
    res_2 = pq.tail.data.document

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_dequeue(pq, data):
    expected_1 = 'PEP484'
    expected_2 = 1

    data1 = data('PEP484', 500)
    data2 = data('Рекурсия', 75)
    pq = pq()
    pq.enqueue(data1), pq.enqueue(data2),

    res_1 = pq.dequeue().document
    res_2 = pq.count

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_dequeue_one_position(pq, data):
    expected_1 = 'Рекурсия'
    expected_2 = 0

    data = data('Рекурсия', 75)
    pq = pq()
    pq.enqueue(data)

    res_1 = pq.dequeue().document
    res_2 = pq.count

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_peek(pq, data):
    expected_1 = 'doc3'
    expected_2 = 30

    data1 = data('doc1', 10)
    data2 = data('doc2', 20)
    data3 = data('doc3', 30)
    data4 = data('doc4', 40)
    pq = pq()
    pq.enqueue(data3), pq.enqueue(data1), pq.enqueue(data4), pq.enqueue(data2)
    doc = pq.peek()

    res_1 = doc.document
    res_2 = doc.number_page

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_peek_queue_isempty(pq):
    expected_1 = None

    pq = pq()

    res_1 = pq.peek()

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
