import pytest
from package_class import Class_stack as cs

@pytest.fixture
def data():
    return cs.TasksStack.Node(cs.ProjectTask('Дела', 5))

@pytest.fixture
def stack():
    return cs.TasksStack()


def test_stack_is_empty():
    expected = True

    res = cs.TasksStack().is_empty()

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