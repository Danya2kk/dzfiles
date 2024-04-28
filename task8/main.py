import json
import csv


def json_to_csv(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    with open('employees.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(data[0].keys())

        for item in data:
            writer.writerow(item.values())
    print("JSON файл успешно преобразован в CSV файл!")


def add_person_to_json(json_file):
    name = input("Введите Имя и Фамилию: ")
    birthday = input("Введите дату рождения (дд.мм.гггг): ")
    height = input("Введите рост: ")
    weight = float(input("Введите вес: "))
    car = input("Введите есть ли у сотрудника машина(0 - нет|1 - есть): ")
    if car == '0':
        car = False
    elif car == '1':
        car = True

    languages = input("Введите языки которые знаете (через пробел): ")
    languages_list = [lang for lang in languages.split(' ')]

    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages_list
    }

    with open(json_file, 'r') as f:
        data = json.load(f)

    data.append(new_employee)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

    print("Сотрудник успешно добавлен")


def add_person_to_csv(csv_file):
    name = input("Введите Имя и Фамилию: ")
    birthday = input("Введите дату рождения (дд.мм.гггг): ")
    height = input("Введите рост: ")
    weight = float(input("Введите вес: "))
    car = input("Введите есть ли у сотрудника машина(0 - нет|1 - есть): ")
    if car == '0':
        car = False
    elif car == '1':
        car = True

    languages = input("Введите языки которые знаете (через пробел): ")
    languages_list = [lang for lang in languages.split(' ')]

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, birthday, height, weight, car, languages_list])

    print("Сотрудник успешно добавлен")


def find_by_name(json_file, name):
    with open(json_file, 'r') as file:
        data = json.load(file)

    flag = False
    for employee in data:
        if employee['name'] == name:
            flag = True
            print("Информация о сотруднике:")
            print("Имя:", employee['name'])
            print("Дата рождения:", employee['birthday'])
            print("Рост:", employee['height'])
            print("Вес:", employee['weight'])
            print("Есть ли машина:", employee['car'])
            print("Языки программирования:", employee['languages'])
            break

    if not flag:
        print("Такого сотрудника нет!")


def find_by_language(json_file, language):
    with open(json_file, 'r') as file:
        data = json.load(file)

    found_employees = []
    for employee in data:
        if language in employee['languages']:
            found_employees.append(employee)

    if found_employees:
        print(f"Сотрудник владеющий {language}:")
        for emp in found_employees:
            print("Имя:", emp['name'])
            print("Языки программирования:", emp['languages'])
            print()
    else:
        print("Таких сотрудников нет!")


def filter_by_year(json_file, year):
    with open(json_file, 'r') as file:
        data = json.load(file)

    total_height = 0
    count = 0
    for employee in data:
        if int(employee['birthday'].split('.')[2]) < year:
            total_height += employee['height']
            count += 1
    avg_height = total_height/count

    print(f"Средний рост всех сотрудников у которых год рождения меньше {year}: {avg_height}")


def print_employees(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for emp in data:
        print("----------------------------")
        print("Информация о сотруднике:")
        print("Имя:", emp['name'])
        print("Дата рождения:", emp['birthday'])
        print("Рост:", emp['height'])
        print("Вес:", emp['weight'])
        print("Есть ли машина:", emp['car'])
        print("Языки программирования:", emp['languages'])

# print(json_to_csv('employees.json'))
# add_person_to_json('employees.json')
# add_person_to_csv('employees.csv')


# find_by_language('employees.json', 'C++')

# find_by_name('employees.json', '')
# filter_by_year('employees.json', 1994)
menu = ("------------MENU------------\n"
        "1. Просмотр всех сотрудников\n"
        "2. Преобразовать JSON в CSV\n"
        "3. Добавить сотрудника в JSON файл\n"
        "4. Добавить сотрудника в CSV файл\n"
        "5. Поиск сотрудника по имени\n"
        "6. Поиск сотрудников владеющих определенным ЯП\n"
        "7. Средний рост сотрудников, дата рождения которых меньшу определенного года\n"
        "0. Выход\n")
flag = True

while flag:
    print(menu)

    choice = int(input("Выберите действие: "))
    match choice:
        case 1:
            print_employees('employees.json')
        case 2:
            json_to_csv('employees.json')

        case 3:
            add_person_to_json('employees.json')

        case 4:
            add_person_to_csv('employees.csv')

        case 5:
            name = input("Введите имя и фамилию для поиска: ")
            find_by_name('employees.json', name)

        case 6:
            language = input("Введите ЯП для поиска: ")
            find_by_language('employees.json', language)
        case 7:
            year = int(input("Введите год для рассчета среднего роста: "))
            filter_by_year('employees.json', year)
        case 0:
            flag = False
            print("Программа успешно завершена")
        case _:
            print("Неверный ввод! Попробуйте еще раз")



