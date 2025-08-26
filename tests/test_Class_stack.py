import pytest
from package_class.Class_stack import *


@pytest.fixture
def data():
    return TasksStack.Node(ProjectTask('Дела', 5))


@pytest.fixture
def stack():
    return TasksStack()


def test_stack_is_empty():
    expected = True

    res = TasksStack().is_empty()

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_push_1(stack, data):
    expected = 1

    stack.push(data)

    res = stack.count

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_push_2(stack, data):
    expected = 3

    stack.push(data), stack.push(data), stack.push(data)

    res = stack.count

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_peek_1(stack):
    expected = None

    res = stack.peek()

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'


def test_stack_peek_2(stack, data):
    expected = 'Дела'

    res = stack.peek()

    assert expected == res, f'Ожидалось: {expected} Получили: {res}'


def test_stack_pop_1(stack, data):
    expected = 2

    stack.push(data), stack.push(data), stack.push(data)
    stack.pop()

    res = stack.count

    assert expected == res, f'Ожидалось{expected}: Получили:{res}'
