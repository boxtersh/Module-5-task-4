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
        while not isinstance(age, int) and (14 <= age or age <= 90):
            print('Возраст персоны должен быть целым числом в интервале 14 - 90 лет')
            age = input('Введите возраст в интервале 14 - 90 лет')
            # Выполняется детальная проверка на соответствие age возрасту персоны в цикле while
            return age

    def __check_occupation(self, occupation):
        if not isinstance(occupation, str):
            occupation = str(occupation)
            # Выполняется детальная проверка на соответствие name имени персоны в цикле while
            return occupation


class PesonList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    class Node:
        def __init__(self, data: PersonCard, next=None):
            self.data = data
            self.next = next

    def add_person(self, name, age, occupation):
        person = PersonCard(name, age, occupation)
        node = PesonList.Node(person)

        if not self.__count==0:
            self.__head.next = node

        self.__head = node
        self.__count += 1
