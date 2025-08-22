from package_class import Class_stack as cs

tasks = cs.TasksStack()
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
print(tasks.peek())