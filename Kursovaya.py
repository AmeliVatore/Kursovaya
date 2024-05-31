from tkinter.filedialog import asksaveasfilename, askopenfilename
class Student():
    def __init__(self, name):
        self.name = name
    def add_student(self, data=None):
        if data != None:
            self.data = data
            self.group = data[5]
        else:
            #data = []
            data = ['Name MiddleName Surname', '23.5.2000', '2018', 'idk', 'idk', 'group-13123', 'nom23123',
                    'male']
            data[0] = self.name
            #data.append(self.name)

            #input_data = input('\nВведите дату рождения в формате dd.mm.yyyy\n')
            #data.append(input_data)

            #input_data = input('\nВведите год поступления\n')
            #data.append(input_data)

            #input_data = input('\nВведите факультет\n')
            #data.append(input_data)

            #input_data = input('\nВведите кафедру\n')
            #data.append(input_data)

            #input_data = input('\nВведите группу\n')
            #data.append(input_data)
            self.group = data[5]

            #input_data = input('\nВведите номер зачётки\n')
            #data.append(input_data)

            #input_data = input('\nВведите пол \n1. Мужской\n2. Женский\n')
            #data.append(input_data)

            self.data = data

    def add_note(self):

        #while True:
        #   self.qt_of_sessions = input('Введите количество сессий')
        #    if qt_of_sessions < 0 or qt_of_sessions > 8:
        #        print('Введите число от 0 до 9')
        #    else:
        #        break

        self.qt_of_sessions = 2

        self.sessions = []
        for i in range(self.qt_of_sessions):
            session = {}
            #qt_of_subjects = input('Введите количество предметов в сессии')
            qt_of_subjects = 2
            for j in range(qt_of_subjects):
                #subject = input('Введите предмет')
                #mark = input('Введите оценку')
                subject = 'Subject' + str(j+1)
                mark = '5'
                session.update({subject: mark})
            self.sessions.append(session)

    @staticmethod
    def info(choice):
        match choice:
                case '1':
                    for student in sp_Students:
                        ##print(student.name, student.date_of_birth, student.admission, student.faculty, student.department, student.group, student.nom, student.sex)
                        print(', '.join(student.data))
                        if hasattr(student, 'sessions'):
                            for i in range(len(student.sessions)):
                                print('Сессия ', i + 1)
                                for subject in student.sessions[i]:
                                    for mark in student.sessions[i][subject]:
                                        print(subject, mark)
                case '2':
                    for student in sp_Students:
                        print(student.name, student.group)

    @staticmethod
    def search():
        while True:
            choice = input('\nДанные, по которым следует осуществлять поиск:\n1. ФИО\n2. Дата рождения\n3. Год поступления\n4. Факультет\n5. Кафеедра\n6. Группа\n7. Номер зачётки\n8. Пол\n')
            # check for nums
            if True and len(choice) < 10 and not ('0' in choice) and not ('9' in choice):
                choice = ''.join(set(choice))
                results = []
                for i in range(len(choice)):
                    match choice[i]:
                        case '1':
                            data = input('\nВведите фамилию и/или имя и/или отчество для поиска\n')
                            # check_data('str', data)
                        case '2':
                            data = input('\nВведите дату рождение в формате dd.mm.yyyy или год рождения\n')
                        case '3':
                            data = input('\nВведите год поступления\n')
                        case '4':
                            data = input('\nВведите факультет\n')
                        case '5':
                            data = input('\nВведите кафедру\n')
                        case '6':
                            data = input('\nВведите группу\n')
                        case '7':
                            data = input('\nВведите номер зачётки\n')
                        case '8':
                            data = input('\nВыберите пол\n1. Мужской\n2. Женский\n')
                        case '9':
                            data = input('\nВыберите вариант поиска\n')
                        case _:
                            print('\nТы как сюда попал??\n')

                    if len(choice) > 1:
                        results.append([])
                    for student in sp_Students:
                        if data in student.data[int(choice[i])-1]:
                            #print(student.name)
                            if len(choice) > 1:
                                results[i].append(student)
                            else:
                                results.append(student)
                    if results[i] == []:
                        print('Данные не найдены')
                        return

                print(results)
                if len(choice) > 1:
                    final_results = list(set(results[0]).intersection(*results[1:]))
                    #print(final_results)
                else:
                    final_results = results

                print('\nВведите номер искомого студента')
                for i in range(len(final_results)):
                    st_data = ', '.join(final_results[i].data)
                    print(f'{str(i+1)}. {st_data}')
                print('0. Тут нет искомого студента')
                while True:
                    required = input()
                    #check
                    required = int(required)
                    if required > 0 and required <= len(final_results):
                        print(final_results[required - 1])
                        return final_results[required - 1]
                    elif required == 0:
                        return
                    else:
                        print(f'{base_text[1]}\n')
                break
            elif choice == '0':
                break
            else:
                print(f'{base_text[1]}\n')

    @staticmethod
    def change(student):
        while True:
            choice = input(
                '\nДанные, которые нужно изменить:\n1. ФИО\n2. Дата рождения\n3. Год поступления\n4. Факультет\n5. Кафеедра\n6. Группа\n7. Номер зачётки\n8. Пол\n9. Вернуться в меню\n')
            match choice:
                case '1':
                    print('\nТекущее ФИО: ' + student.name)
                    data = input('\nВведите новые ФИО\n')
                    # check_data('str', data)
                    student.name = data
                    student.data[0] = data
                case '2':
                    data = input('\nВведите новую дату рождение в формате dd.mm.yyyy или год рождения\n')
                    # check_data(, data)
                    student.data[1] = data
                case '3':
                    data = input('\nВведите год поступления\n')
                    # check_data(, data)
                    student.data[2] = data
                case '4':
                    data = input('\nВведите факультет\n')
                    # check_data(, data)
                    student.data[3] = data
                case '5':
                    data = input('\nВведите кафедру\n')
                    # check_data(, data)
                    student.data[4] = data
                case '6':
                    data = input('\nВведите группу\n')
                    # check_data(, data)
                    student.group = data
                    student.data[5] = data
                case '7':
                    data = input('\nВведите номер зачётки\n')
                    # check_data(, data)
                    student.data[6] = data
                case '8':
                    data = input('\nВыберите пол\n1. Мужской\n2. Женский\n')
                    # check_data(, data)
                    student.data[7] = data
                case '9':
                    break
                case _:
                    print(f'{base_text[1]}\n')

    @staticmethod
    def var():
        pass


def open_file():
    files = [('Любой', '*'), ('TXT files', '*.txt*')]
    try:
        filepath = askopenfilename(filetype = files)
    except:
        print('Файл не выбран')
    else:
        if filepath != '':
            with open(filepath, 'r') as F:
                while True:
                    line = F.readline()
                    if not line:
                        break

                    if line[0] != '[':
                        data = line.split('\n')
                        data = data[0].split(',')

                        #for element in data:
                        #checks

                        current_st = Student(data[0])
                        current_st.add_student(data)
                        sp_Students.append(current_st)

                    else:
                        data = line.split('\n')
                        data = eval(data[0])

                        #for element in data:
                        #checks

                        current_st = sp_Students[len(sp_Students) - 1]
                        current_st.sessions = data
                print('\nДанные успешно загружены\n')

def save_file():
    files = [('Любой', '*'), ('TXT files', '*.txt*')]
    filepath = asksaveasfilename(filetypes=files, defaultextension='')
    try:
        with open(filepath, 'wt') as F:
            for student in sp_Students:
                st_data = ', '.join(student.data)
                F.write(st_data + '\n')
                if hasattr(student, 'sessions'):
                    session_data = str(student.sessions)
                    F.write(session_data + '\n')
    except:
        print('Файл не выбран')
        return True

def check_data(kind_of_data, data):
    pass


sp_Students = []
file_check = False
base_text = ['Вернуться в меню', 'Введите номер выбранного пункта меню']
while True:
    choice = input('1. Показать данные\n2. Добавить студента\n3. Изменить данные\n4. Удалить данные\n5. Открыть файл\n6. Сохранить в файл\n7. Задание варианта\n8. Выход\n')
    match choice:
        case '1':
            if len(sp_Students) == 0:
                print('Данных нет\n')
            else:
                while True:
                    choice = input(
                        f'Показать:\n1. Весь список студентов целиком\n2. Список из ФИО и группы\n3. {base_text[0]}\n')
                    match choice:
                        case '1':
                            Student.info(1)
                            break
                        case '2':
                            Student.info(2)
                            break
                        case '3':
                            break
                        case _:
                            print(f'{base_text[1]}\n')

        case '2':
            name = input('Введите ФИО студента\n')
            current_st = Student(name)
            current_st.add_student()
            sp_Students.append(current_st)
            current_st.add_note()

        case '3':
            if len(sp_Students) == 0:
                print('Введите данные прежде, чем менять их\n')
            else:
                result = Student.search()
                if result:
                    print(result.name)
                Student.change(result)

        case '4':
            if len(sp_Students) == 0:
                print('Введите данные прежде, чем удалить их\n')
            else:
                while True:
                    choice = input(f'Выберите действие:\n1. Поиск студента для удаления\n2. Очистить весь список студентов\n3. {base_text[0]}\n')
                    if choice == '1':
                        result = Student.search()
                        if result:
                            print(result.name)
                            sp_Students.remove(result)
                            del result
                    elif choice == '2':
                        while len(sp_Students) != 0:
                            del sp_Students[0]
                        sp_Students.clear()
                        break
                    elif choice == '3':
                        break
                    else:
                        print(f'{base_text[1]}\n')

        case '5':
            if len(sp_Students) == 0:
                open_file()
            else:
                while True:
                    choice = input(f'Заменить уже имеющийся список студентов данными, полученными из файла?\n1. Да\n2. Нет\n3. {base_text[0]}\n')
                    if choice == '1':
                        while len(sp_Students) != 0:
                            del sp_Students[0]
                        open_file()
                        break
                    elif choice == '2':
                        open_file()
                        break
                    elif choice == '3':
                        break
                    else:
                        print(f'{base_text[1]}\n')

        case '6':
            if len(sp_Students) == 0:
                print('Введите данные прежде, чем сохранить их\n')
            else:
                save_file()

        case '7':
            if len(sp_Students) == 0:
                print('Для выполнения задания варианта необходимо ввести данные\n')
            else:
                Student.var()

        case '8':
            break
        case _:
            print(f'{base_text[1]}\n')
