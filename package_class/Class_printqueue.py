class Queue:

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
        node = Queue.Node(data)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node
        self.__count += 1

    def dequeue(self) -> any:

        if self.is_empty(): return

        data = self.__head.data

        self.__head = self.__head.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1

        return data

    def peek(self) -> any:

        if not self.is_empty():
            return self.__head.data

        return None