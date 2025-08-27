import pytest
from package_class.Class_stack import *

@pytest.fixture
def stack():
    return TasksStack


@pytest.fixture
def node():
    return TasksStack.Node


@pytest.fixture
def data():
    return ProjectTask


# тесты clacc ProjectTask
def test_project_task_init(data):
    expected1 = "Задача"
    expected2 = 7

    data = data("Задача", 7)
    res1 = data.description
    res2 = data.datetime

    assert expected1 == res1, f'Ожидалось: {expected1} Получили:{res1}'
    assert expected2 == res2, f'Ожидалось: {expected2} Получили:{res2}'


def test_project_task_repr(data):
    expected = 'Дела: ДЗ\nВремя выполнения: 3ч.'

    data = data("ДЗ", 3)

    res = repr(data)

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_project_task_invalid_datetime(data):
    with pytest.raises(AssertionError):
        data(5,5)


# тесты clacc Node
def test_create_node(node, data):
    expected_data = 'ДЗ'
    expected_prev = None


    node = node(data('ДЗ',5))

    res_data = node.data.description
    res_prev = node.prev

    assert expected_data == res_data, f'Ожидалось: {expected_data} Получили: {res_data}'
    assert expected_prev == res_prev, f'Ожидалось: {expected_prev} Получили: {res_prev}'

# тесты clacc TasksStack
def test_steck_stack_isempty(stack):
    expected = 0
    expected_true = True

    res_true = stack().is_empty()
    res = stack().count

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'
    assert expected_true == res_true, f'Ожидалось{expected_true}: Получили:{res_true}'


def test_stack_push_1(stack, node, data):
    expected1 = 1
    expected2 = 'Контрольная'

    node = node(data('Контрольная',5))
    stack = stack()
    stack.push(node)

    res1 = stack.count
    res2 = stack.top.data.description

    assert expected1 == res1, f'Ожидалось{expected1}: Получили:{res1}'
    assert expected2 == res2, f'Ожидалось{expected2}: Получили:{res2}'


def test_stack_push_2(stack, node, data):
    expected1 = 2
    expected2 = 'ДЗ'

    node1 = node(data('Контрольная', 5))
    node2 = node(data('ДЗ',3))
    stack = stack()
    stack.push(node1), stack.push(node2)

    res1 = stack.count
    res2 = stack.top.data.description

    assert expected1 == res1, f'Ожидалось{expected1}: Получили:{res1}'
    assert expected2 == res2, f'Ожидалось{expected2}: Получили:{res2}'


def test_stack_isempty_peek(stack):
    expected = None

    res = stack().peek()

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_peek(stack, node, data):
    expected = 'Контрольная'

    node = node(data('Контрольная',5))
    stack = stack()
    stack.push(node)

    res = stack.peek().description

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_pop(stack, node, data ):
    expected1 = 'Контрольная'
    expected2 = 2

    node1 = node(data('Новая тема',2))
    node2 = node(data('Контрольная', 5))
    node3 = node(data('ДЗ',3))
    stack = stack()
    stack.push(node1), stack.push(node3), stack.push(node2)

    res1 = stack.pop().description
    res2 = stack.count

    assert expected1 == res1, f'Ожидалось{expected1}: Получили:{res1}'
    assert expected2 == res2, f'Ожидалось{expected2}: Получили:{res2}'


def test_stack_clean(stack, node, data ):
    expected1 = None
    expected2 = 0

    node1 = node(data('Новая тема',2))
    node2 = node(data('Контрольная', 5))
    node3 = node(data('ДЗ',3))
    stack = stack()
    stack.push(node1), stack.push(node3), stack.push(node2), stack.clean()

    res1 = stack.top
    res2 = stack.count

    assert expected1 == res1, f'Ожидалось{expected1}: Получили:{res1}'
    assert expected2 == res2, f'Ожидалось{expected2}: Получили:{res2}'