# Задача №2. Разработайте структуру данных "Стек" для управления задачами проекта

class ProjectTask:
    def __init__(self, description: str, datetime: int):
        self.__string_description = description
        self.__datetime = datetime

    def __repr__(self):
        return f'Дела: {self.__string_description}\nВремя выполнения: {self.__datetime}ч.'

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
        if not self.is_empty():
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

    def count(self):
        return self.__count

    count = property(count)

