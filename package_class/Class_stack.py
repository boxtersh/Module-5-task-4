# Задача №2. Разработайте структуру данных "Стек" для управления задачами проекта

class ProjectTask:
    def __init__(self, description: str, datetime: int):
        self.__description = self.__check_type(description, str)
        self.__datetime = self.__check_type(datetime, int)

    def __check_type(self, value , types):
        assert isinstance(value, types), f'Ожидали:{types}, получили:{type(value)}'
        return value

    def __repr__(self):
        return f'Дела: {self.__description}\nВремя выполнения: {self.__datetime}ч.'

    @property
    def description(self):
        return self.__description

    @property
    def datetime(self):
        return self.__datetime


class TasksStack:

    class Node:
        def __init__(self, data: ProjectTask, prev = None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__top = None
        self.__count = 0

    def is_empty(self):
        return self.__count == 0

    def push(self, node: Node):
        node.prev = self.__top
        self.__top = node
        self.__count += 1

    def peek(self):
        if not self.is_empty():
            return self.__top.data

    def pop(self):
        if not self.is_empty():
            target = self.__top.data
            self.__top = self.__top.prev
            self.__count -= 1
            return target

    def clean(self):
        self.__top = None
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @property
    def top(self):
        return self.__top
