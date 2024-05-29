class Student():
    def __init__(self, name):
        self.name = name
    def add_student(self, data=None):
        if data != None:

            self.date_of_birth = data[1]
            self.admission = data[2]
            self.faculty = data[3]
            self.department = data[4]
            self.group = data[5]
            self.nom = data[6]
            self.sex = data[7]
        else:
            data = []
            data.append(self.name)

            input_data = input('\nВведите дату рождения в формате dd.mm.yyyy\n')
            data.append(input_data)
            self.date_of_birth = data[1]

            input_data = input('\nВведите год поступления\n')
            data.append(input_data)
            self.admission = data[2]

            input_data = input('\nВведите факультет\n')
            data.append(input_data)
            self.faculty = data[3]

            input_data = input('\nВведите кафедру\n')
            data.append(input_data)
            self.department = data[4]

            input_data = input('\nВведите группу\n')
            data.append(input_data)
            self.group = data[5]

            input_data = input('\nВведите номер зачётки\n')
            data.append(input_data)
            self.nom = data[6]

            input_data = input('\nВведите пол \n1. Мужской\n2. Женский\n')
            data.append(input_data)
            self.sex = data[7]

    def add_note(self, data = None):
        #qt_of_sessions = input()
        qt_of_sessions = 2     # 0 < 9
        self.sessions = []
        for i in range(qt_of_sessions):
            session = {}
            qt_of_subjects = 2
            for j in range(qt_of_subjects):
                #subject = input('Введите предмет')
                #mark = input('Введите оценку')
                subject = 'Subject' + str(j+1)
                mark = '5'
                session.update({subject: mark})
            self.sessions.append(session)

    def info(self, choice):
        match choice:
            case 1:
                print(self.name, self.date_of_birth, self.admission, self.faculty, self.department, self.group, self.nom, self.sex)
                for i in range(len(self.sessions)):
                    print('Сессия ', i + 1)
                    for subject in self.sessions[i]:
                        for mark in self.sessions[i][subject]:
                            print(subject, mark)
            case 2:
                print(self.name, self.group)

    @staticmethod
    def search():
        pass

    @staticmethod
    def change():
        pass

    @staticmethod
    def var():
        pass

def open_file():
    pass

def save_file(self):
    pass

def delete_data():
        pass

def check_data(type_of_data, type):
    pass


sp_Students = []
file_check = False
base_text = ['Вернуться в меню', 'Введите номер выбранного пункта меню']
while True:
    choice = input('1. Показать данные\n2. Добавить студента\n3. Изменить данные\n4. Удалить студента\n5. Открыть файл\n6. Сохранить в файл\n7. Задание варианта\n8. Выход\n')
    match choice:
        case '1':
            if len(sp_Students) == 0:
                print('Данных нет\n')
            else:
                while True:
                    choice = input(f'Показать:\n1. Весь список студентов целиком\n2. Список из ФИО и группы\n3. {base_text[0]}\n')
                    if choice == '1':
                        for student in sp_Students:
                            student.info(1)
                    elif choice == '2':
                        for student in sp_Students:
                            student.info(2)
                    elif choice == '3':
                        break
                    else:
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
                pass
                #Student.change()

        case '4':
            if len(sp_Students) == 0:
                print('Введите данные прежде, чем удалить их\n')
            else:
                while True:
                    choice = input(f'Выберите действие:\n1. Удалить уже имеющийся список студентов\n2. Очистить файл \n3. {base_text[0]}\n')
                    if choice == '1':
                        for i in range(len(sp_Students)):
                            del sp_Students[i]
                            print(sp_Students[i])
                        sp_Students.clear()
                    elif choice == '2':
                        pass
                        #delete_data()
                    elif choice == '3':
                        break
                    else:
                        print(f'{base_text[1]}\n')

        case '5':
            while True:
                choice = input(f'Заменить уже имеющийся список студентов данными, полученными из файла?\n1. Да\n2. Нет\n3. {base_text[0]}\n')
                if choice == '1':
                    for i in range(len(sp_Students)):
                        del sp_Students[i]
                    sp_Students.clear()
                    #open_file()
                elif choice != '2':
                    pass
                    #open_file()
                elif choice == '3':
                    break
                else:
                    print(f'{base_text[1]}\n')

        case '6':
            if len(sp_Students) == 0:
                print('Введите данные прежде, чем сохранить их\n')
            else:
                for student in sp_Students:
                    save_file(student)

        case '7':
            if len(sp_Students) == 0:
                print('Для выполнения задания варианта необходимо ввести данные\n')
            else:
                Student.var()

        case '8':
            break
        case _:
            print(f'{base_text[1]}\n')
