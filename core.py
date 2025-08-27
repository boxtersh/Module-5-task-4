from package_class import Class_stack as cs
from package_class import Class_personlist as cp
from package_class import Class_printqueue as pq


def main():
    """
    Тело программы
    :return:
    """

# Задача №1. Разработайте односвязный список для управления карточками персон

    pList = cp.PersonList()
    person1 = cp.PersonCard('1',15,'1')
    person2 = cp.PersonCard('2', 25, '2')
    person3 = cp.PersonCard('3', 35, '3')
    print(f'Список пуст? - {'Да' if pList.is_empty()else 'Нет'}')
    pList.add_person(person1)
    print(f'Список пуст? - {'Да' if pList.is_empty() else 'Нет'}')
    print(pList.total_people())
    pList.add_person(person2)
    print(pList.total_people())
    pList.append_person(person3)
    print(pList.total_people())
    pList.remove_person(person3)
    print(pList.total_people())
    print(f'Последняя карточка списка {pList.remove_last_person()}')
    print(pList.total_people())
    print(f'Первая карточка списка {pList.remove_first_person()}')
    print(pList.total_people())
    pList.add_person(person1)
    pList.add_person(person2)
    print(pList.total_people())
    pList.clear_all()
    print(pList.total_people())
    input('Введите enter для продолжения >> ')

# Задача №2. Разработайте структуру данных "Стек" для управления задачами проекта

    tasks = cs.TasksStack()
    print(f'Список пуст? - {'Да' if tasks.is_empty()else 'Нет'}')
    print(f'Элементов в списке: {tasks.count}\n')
    tasks.push(tasks.Node(cs.ProjectTask('Выполнить ДЗ_1',1)))
    tasks.push(tasks.Node(cs.ProjectTask('Выполнить ДЗ_2',1)))
    tasks.push(tasks.Node(cs.ProjectTask('Выполнить ДЗ_3',1)))
    tasks.push(tasks.Node(cs.ProjectTask('Подготовка к контрольной',1)))
    print(tasks.peek())
    print(f'Список пуст? - {'Да' if tasks.is_empty()else 'Нет'}')
    print(f'Элементов в списке: {tasks.count}\n')
    print(tasks.pop())
    print(f'Список пуст? - {'Да' if tasks.is_empty()else 'Нет'}')
    print(f'Элементов в списке: {tasks.count}\n')
    print(tasks.pop())
    print(f'Элементов в списке: {tasks.count}\n')
    tasks.clean()
    print(f'Элементов в списке: {tasks.count}\n')

    input('Введите enter для продолжения >> ')

# Задача №3. Разработайте структуру данных "Очередь" для управления очередью печати документов

    queeu = pq.PrintQueue()
    doc1 = pq.PrintDocument('doc1', 10)
    doc2 = pq.PrintDocument('doc2', 20)
    doc3 = pq.PrintDocument('doc3', 30)
    doc4 = pq.PrintDocument('doc4', 40)

    print(f'Очередь пуста? Мне только спросить! {'Да'if queeu.is_empty() else 'нет'}, в очереди: {queeu.count}\n')
    print(f'Посмотреть первый в очереди {queeu.peek()}')
    queeu.enqueue(doc3), queeu.enqueue(doc2), queeu.enqueue(doc4), queeu.enqueue(doc1),
    print(f'Очередь пуста? {'Да'if queeu.is_empty() else 'нет'}, в очереди: {queeu.count}\n')
    print(queeu.dequeue(),'\n'), print(queeu.dequeue(),'\n')
    print(f'Очередь пуста? {'Да'if queeu.is_empty() else 'нет'}, в очереди: {queeu.count}\n')

    input('Введите enter для продолжения >> ')