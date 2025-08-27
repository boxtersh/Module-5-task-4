from typing import Any

class PrintDocument:
    def __init__(self,document: str, number_page: int):
        self.__document = self.__check_type(document, str)
        self.__number_page = self.__check_type(number_page, int)

    def __check_type(self, value , types):
        assert isinstance(value, types), f'Ожидали:{types}, получили:{type(value)}'
        return value

    @property
    def document(self):
        return self.__document

    @property
    def number_page(self):
        return self.__number_page


class PrintQueue:

    class Node:

        def __init__(self, data, prev=None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self) -> bool:
        return self.__head == None

    def enqueue(self, data) -> None:
        node = PrintQueue.Node(data)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1

    def dequeue(self) -> Any:

        if self.is_empty(): return

        data = self.__head.data

        self.__head = self.__head.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1

        return data

    def peek(self) -> Any:

        if not self.is_empty():
            return self.__head.data

        return None

    @property
    def count(self):
        return self.__count

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail