import pytest
from package_class.Class_personlist import *


@pytest.fixture
def pList():
    return PersonList


@pytest.fixture
def node():
    return PersonList.Node


@pytest.fixture
def data():
    return PersonCard


# Тест class PersonCard
def test_data_init(data):
    expected_1 = '1'
    expected_2 = 2
    expected_3 = '3'

    data = data('1',2,'3')

    res_1 = data.name
    res_2 = data.age
    res_3 = data.occupation

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'
    assert res_3 == expected_3, f'Ожидали: {expected_3}, получили: {res_3}'


# Тест class Node
def test_node_init(node, data):
    expected_1 = None
    expected_2 = 13

    data = data('1', 13, '1')
    node = node(data)

    res_1 = node.next
    res_2 = node.data.age

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


# Тест class PersonList
def test_list_is_empty(pList):

    expected_1 = None
    expected_2 = 0
    pList = pList()
    res_1 = pList.head
    res_2 = pList.count

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_add_person(pList, node, data):
    expected = '1'

    data = data('1', 15, '1')
    pList = pList()
    pList.add_person(data)

    res = pList.head.data.name

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_append_isempty_list(pList, data):
    expected = 1
    expected_1 = 13

    data1 = data('1', 13, '1')
    pList = pList()
    pList.append_person(data1)

    res = pList.count
    res_1 = pList.head.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'
    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'


def test_append(pList, data):
    expected = 2
    expected_1 = 25
    expected_2 = 15

    data1 = data('1', 15, '1')
    data2 = data('2', 25, '2')
    pList = pList()
    pList.add_person(data2)
    pList.append_person(data1)

    res = pList.count
    res_1 = pList.head.data.age
    res_2 = pList.tail.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'
    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_insert_last(pList, data):
    expected = 5
    expected_1 = 13
    expected_2 = 43

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data5 = data('5', 53, '5')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.insert_person_at(4, data5)

    res = pList.count
    res_1 = pList.head.data.age
    res_2 = pList.tail.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'
    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_insert_first(pList, data):
    expected = 5
    expected_1 = 53
    expected_2 = 43

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data5 = data('5', 53, '5')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.insert_person_at(1, data5)

    res = pList.count
    res_1 = pList.head.data.age
    res_2 = pList.tail.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'
    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_insert_out_range_1(pList, data):
    expected = 5
    expected_1 = 53
    expected_2 = 43

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data5 = data('5', 53, '5')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)

    with pytest.raises(AssertionError):
        pList.insert_person_at(-5, data5)


def test_insert_out_range_2(pList, data):
    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data5 = data('5', 53, '5')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)

    with pytest.raises(AssertionError):
        pList.insert_person_at(5, data5)


def test_remove_first_person(pList, data):
    expected = 13

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)

    res = pList.remove_first_person().age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_first_person_isempty_list(pList):
    expected = None

    pList = pList()

    res = pList.remove_first_person()

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_last_person(pList, data):
    expected = 43

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)

    res = pList.remove_last_person().age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_last_person_isempty_list(pList):
    expected = None

    pList = pList()

    res = pList.remove_last_person()

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_person_positive_isempty_list(pList, data):
    expected = None

    data_del = data('2', 23, '2')
    pList = pList()

    res = pList.remove_person(data_del)

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_person_positive(pList, data):
    expected = 3

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data_del = data('2', 23, '2')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.remove_person(data_del)

    res = pList.count

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_person_negative(pList, data):
    expected = 4

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data_del = data('2', 27, '2')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.remove_person(data_del)

    res = pList.count

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_remove_person_negative_first_position(pList, data):
    expected = 3

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    data_del = data('1', 13, '1')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.remove_person(data_del)

    res = pList.count

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_total_people(pList, data):
    expected = 4

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)

    res = pList.total_people()

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_clear_all(pList, data):
    expected = 0

    data1 = data('1', 13, '1')
    data2 = data('2', 23, '2')
    data3 = data('3', 35, '3')
    data4 = data('4', 43, '4')
    pList = pList()
    pList.add_person(data4), pList.add_person(data3), pList.add_person(data2), pList.add_person(data1)
    pList.clear_all()

    res = pList.count

    assert res == expected, f'Ожидали: {expected}, получили: {res}'