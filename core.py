from package_class import Class_stack as cs

def main():
    """
    Тело программы
    :return:
    """
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