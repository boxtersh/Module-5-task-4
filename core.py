from package_class import Class_stack as cs
from package_class import Class_personlist as cp
def main():
    """
    Тело программы
    :return:
    """

# Задача №1. Разработайте односвязный список для управления карточками персон

    pList = cp.PersonList()
    print(f'Список пуст? - {'Да' if pList.is_empty()else 'Нет'}')
    pList.add_person('1',1,'1')
    print(f'Список пуст? - {'Да' if pList.is_empty() else 'Нет'}')
    pList.add_person('2', 2, '2')
    print(pList.total_people())
    pList.add_person('3', 3, '3')
    print(pList.total_people())
    pList.remove_person('3',3,'3')
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