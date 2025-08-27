class PersonCard:
    def __init__(self, name: str, age: int, occupation: str):
        self.__name = self.__check_name(name)
        self.__age = self.__check_age(age)
        self.__occupation = self.__check_occupation(occupation)

    def __check_name(self, name):
        if not isinstance(name, str):
            name = str(name)
            # Выполняется детальная проверка на соответствие name имени персоны в цикле while
        return name

    def __check_age(self, age):
        while not isinstance(age, int) and (14 > age or age > 90):
            print('Возраст персоны должен быть целым числом в интервале 14 - 90 лет')
            age = input('Введите возраст в интервале 14 - 90 лет')
            # Выполняется детальная проверка на соответствие age возрасту персоны в цикле while
        return int(age)

    def __check_occupation(self, occupation):
        if not isinstance(occupation, str):
            occupation = str(occupation)
            # Выполняется детальная проверка на соответствие occupation профессия персоны в цикле while
        return occupation

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def occupation(self):
        return self.__occupation


class PersonList:

    class Node:
        def __init__(self, data: PersonCard, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self):
        return self.__head is None

    def add_person(self, person: PersonCard) -> None:
        """
        Функция добавляет карточку class PersonCard в начало списка
        :param name: поле class PersonCard
        :param age: поле class PersonCard
        :param occupation: поле class PersonCard
        :return:
        """
        node = PersonList.Node(person)

        if self.is_empty():
            self.__tail = node

        else:
            node.next = self.__head

        self.__head = node
        self.__count += 1

    def append_person(self, person: PersonCard) -> None:
        """
        Функция добавляет карточку class PersonCard в конец списка
        :param name: поле class PersonCard
        :param age: поле class PersonCard
        :param occupation: поле class PersonCard
        :return:
        """
        node = PersonList.Node(person)

        if self.is_empty():
            self.__head = node

        else:
            self.__tail.next = node

        self.__tail = node
        self.__count += 1

    def insert_person_at(self, index: int, person: PersonCard) -> None:
        """
        Функция вставляет элемент по номеру в списке
        Пример: index = 3, data = A
        номера позиций в списке 1,2,3,4,5
        ответ:
        1,2,А,3,4,5
        :param index: номер позиции вставки
        :param name: поле класса PersonCard
        :param age: поле класса PersonCard
        :param occupation: поле класса PersonCard
        :return: None
        """
        assert isinstance(index, int), f'Ожидалось: <class int>, получили: {type(index)}'

        assert index <= self.__count and index >= 1, f'index позиции должен быть >= 1 или <= {self.__count}'

        node = PersonList.Node(person)
        real = self.__head

        if index == 1:
            node.next = self.__head
            self.__head = node

        else:
            for _ in range(1, index - 1):
                real = real.next

        node.next = real.next
        real.next = node
        self.__count += 1

    def remove_first_person(self) -> None | PersonCard:
        """
        Функция возвращает первую карточку из списка
        :return: объект класса PersonCard
        """
        if self.is_empty():
            return

        target = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return target

    def remove_last_person(self) -> None | PersonCard:
        """
        Функция возвращает последнюю карточку из списка
        :return: объект класса PersonCard
        """
        if self.is_empty():
            return

        real = self.__head
        target = self.__tail.data

        for _ in range(1, self.__count - 1):
            real = real.next

        self.__tail = real
        self.__tail.next = None
        self.__count -= 1
        return target

    def remove_person(self, person: PersonCard) -> None:
        """
        Функция удаляет курточку с указанными полями
        :param name: поле класса PersonCard
        :param age: поле класса PersonCard
        :param occupation: поле класса PersonCard
        :return: None
        """
        name, age, occupation = person.name, person.age, person.occupation
        if self.is_empty():
            return

        if (self.__head.data.name == name and self.__head.data.age == age and self.__head.data.occupation == occupation):
            self.__head = self.__head.next
            self.__count -= 1
            return

        real = self.__head

        for _ in range(1, self.__count):
            if (real.next.data.name == name and real.next.data.age == age and real.next.data.occupation == occupation):
                real.next = real.next.next
                self.__count -= 1
                return
            real = real.next

    def total_people(self) -> int:
        """
        Функция возвращает количество карточек в списке
        :return: количество карточек в списке
        """
        return self.__count

    def clear_all(self) -> None:
        """
        Функция удаляет все карточки
        :return: None
        """
        self.__head = None
        self.__tail = None
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail
