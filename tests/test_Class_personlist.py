import pytest
from package_class.Class_personlist import *


@pytest.fixture
def pList():
    return PersonList()


def test_list_is_empty(pList):

    expected_1 = None
    expected_2 = 0

    res_1 = pList.head
    res_2 = pList.count

    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'


def test_add_person(pList):
    expected = 15

    pList.add_person('1', 15, '1')

    res = pList.head.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'


def test_append_append_person(pList):
    expected = 2
    expected_1 = 15
    expected_2 = 25

    pList.add_person('1', 15, '1')
    pList.append_person('2', 25, '2')

    res = pList.count
    res_1 = pList.head.data.age
    res_2 = pList.tail.data.age

    assert res == expected, f'Ожидали: {expected}, получили: {res}'
    assert res_1 == expected_1, f'Ожидали: {expected_1}, получили: {res_1}'
    assert res_2 == expected_2, f'Ожидали: {expected_2}, получили: {res_2}'

