import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Ученики  (Добавить, редактировать, удалить)
        2  Предметы (Добавить, редактировать, удалить)
        3  Оценки   (Добавить, редактировать, удалить)
        ----------------------------------------------
        4. Все оценки по всем ученикам
        5  Все оценки всех учеников по конкретному предмету
        ----------------------------------------------
        6. Средний балл по конкретному предмету каждого ученика
        7. Средний балл по конкретному предмету всех учеников
        8. Рейтинг (Средний балл по всем предметам по всем ученикам)
        9. Общий средний балл по всем предметам по всем ученикам
        ----------------------------------------------
        10. Все оценки для конкретного ученика
        11. Оценки по конкретному предмету конкретного ученика
        ----------------------------------------------
        12. Средний балл по каждому предмету по конкретному ученику
        13. Средний балл по конкретному предмету по конкретному ученику
        14. Рейтинг (Средний балл по всем предметам по конкретному ученику)
        ----------------------------------------------
              
        0. Выход из программы
        ''')
print(" ")

while True:
    command = int(input('Введите команду: '))
    if command == 1:
#действия по ученикам
        print('''
                Список команд ученики:
                1. Добавить
                2  Редактировать
                3  Удалить
                         ''')
        command1 = int(input('Введите следующую команду: '))
        print(" ")
        if command1 == 1:
            #Добавляем нового ученика
            student_ = input("Введите имя ученика, которого хотите добавить: ")
            if student_ not in students:
                students.append(student_)
                # сгенерируем данные по оценкам:
                # цикл по ученикам
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:
                       students_marks[student][class_] = marks

                print(f'новый ученик "{student_}" добавлен')
                print(" ")
            else:
                print("Ученик уже существует")
                print(" ")

        elif command1 == 2:
            # Редактируем имя ученика - создаем новый ключь и удаляем тот который надо изменить
            sn = input('Введите имя ученика, имя которого хотите исправить: ')
            if sn in students:
                snn = input('Введите новое имя: ')
                students.append(snn)
                students.remove(sn)
                print(f'Имя ученика "{sn}" изменено на "{snn}"')
                print(' ')
                # сгенерируем данные по оценкам:
                # цикл по ученикам
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:

                        students_marks[student][class_] = marks


            else:
                print("Такого ученика нет")
                print(" ")
        elif command1 == 3:
            # Удаляем ученика - удаляем ключь
            sdel = input('Введите имя ученика, которого хотите удалить: ')
            if sdel in students_marks.keys():
                students.remove(sdel)
                print(f'Имя ученика "{sdel}" удаленно')
                print(" ")
            else:
                    print("Такого ученика нет")
                    print(" ")
    # ----------------------------------------------------------------------------------------------------
# действия по предметам
    elif command == 2:
    # действия по предметам
        print('''
                    Список команд предметы:
                    1. Добавить
                    2  Редактировать
                    3  Удалить
                             ''')
        command2 = int(input('Введите следующую команду: '))
        print(" ")
        if command2 == 1:
                    #Добавляем нового предмета
            classes_ = input("Введите название предмета, который хотите добавить: ")
            if classes_ not in classes:
                classes.append(classes_)
                # сгенерируем данные по оценкам:
                # цикл по ученикам
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:
                        students_marks[student][class_] = marks

                print(f'новый предмет "{classes_}" добавлен')
                print(" ")
            else:
                print("предмет уже существует")
                print(" ")
        elif command2 == 2:
            # Редактируем пердмет - создаем новый ключь и удаляем тот который надо изменить
            pn = input('Введите название предмета, который хотите изменить: ')
            if pn in classes:
                pnn = input('Введите новое название: ')
                classes.append(pnn)
                classes.remove(pn)
                print(f'Название предмета "{pn}" изменено на "{pnn}"')
                print(" ")
                # сгенерируем данные по оценкам:
                # цикл по ученикам
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:
                        students_marks[student][class_] = marks


            else:
                    print("Такого предмета нет")
                    print(" ")
        elif command2 == 3:
            # Удаляем предмет - удаляем ключь
            сd = input('Введите название предмета, который хотите удалить: ')
            if сd in classes:
                classes.remove(сd)
                print(f'Предмет "{сd}" удален')
                print(" ")
                # сгенерируем данные по оценкам:
                # цикл по ученикам
                for student in students:
                    students_marks[student] = {}
                    for class_ in classes:
                        marks = [random.randint(1, 5) for i in range(3)]
                        students_marks[student][class_] = marks

            else:
                print("Такого предмета нет")
                print(" ")
#----------------------------------------------------------------------------------------------
#Действия по оценкам
    elif command == 3:
        print('''
                        Список команд оценки:
                        1. Добавить
                        2  Редактировать
                        3  Удалить
                                 ''')
        command3 = int(input('Введите следующую команду: '))
        print(" ")
        if command3 == 1:

            # считываем имя ученика
            student = input('Введите имя ученика, оценку которого хотите добавить: ')
            # считываем название предмета
            class_ = input('Введите предмет, по которому хотите добавить оценку: ')
                     # считываем оценку
            mark = int(input('Введите оценку, которую хотите добавить: '))
            # если данные введены верно
            if student in students and class_ in classes:
                # добавляем новую оценку для ученика по предмету
                    students_marks[student][class_].append(mark)
                    print(f'Для ученика "{student}" по предмету "{class_}" добавлена оценка "{mark}"')
                    print(" ")
            # неверно введены название предмета или имя ученика
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')
                print(" ")
        if command3 == 2:

            # считываем имя ученика
            student = input('Введите имя ученика, оценку которого хотите изменить: ')
            # считываем название предмета
            class_ = input('Введите предмет, оценку по которому хотите изменить: ')
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                print(f'{student} - {students_marks[student][class_]}')
                     # считываем оценку
                mark1 = int(input('Введите номер оценки, которую надо поменять: '))
                mark1 -= 1
                print(f'Выбранна оценка: {students_marks[student][class_][mark1]}')
               # удаляем оценку по индексу
                de = students_marks[student][class_].pop(mark1)
                # добовляем новую оценку по индексу
                students_marks[student][class_].insert(mark1,input('Введите новую оценку: '))
                print(f'{student} - {students_marks[student][class_]}')
                print(" ")
            else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
                    print(" ")
        if command3 == 3:

            # считываем имя ученика
            student = input('Введите имя ученика у которого хотите удалить оценку: ')
            # считываем название предмета
            class_ = input('Введите предмет, по которому хотите удалить оценку: ')
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                print(f'{student} - {students_marks[student][class_]}')
                     # считываем оценку
                mark1 = int(input('Введите номер оценки, которую хотите удалить: '))
                mark1 -= 1
                print(f'Оценка удаленна: {students_marks[student][class_][mark1]}')
                # удаляем оценку по индексу
                de = students_marks[student][class_].pop(mark1)
                print(f'{student} - {students_marks[student][class_]}')
                print(" ")
            else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
                    print(" ")
#----------------------------------------------------------------------------------------------------------------

    elif command == 0:
        print('4. Выход из программы')
    elif command == 4:
        print(' ')
# все оценки по всем ученикам
        for student in students:
            print(f'''{student}
                   {students_marks[student]}''')
    elif command == 5:
        print(' ')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            for student in students:
               print(f'{student} - {students_marks[student][class_]}')
               print(" ")
        else:
            print('такого предмета нет')
            print(" ")


    elif command == 7:
        print(' ')
       #средний балл по всем предметам по всем ученикам')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
                print(" ")
    elif command == 6:
        # средний балл по всем предметам по каждому ученику')
        print(' ')
        stud = input('Введите имя ученика: ')
        if stud in students:
            for class_ in classes:
                marks_sum = sum(students_marks[stud][class_])

                # находим количество оценок по предмету
                marks_count = len(students_marks[stud][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
                print(" ")
        else:
            print('такого ученика нет')
            print(" ")

