from .data import departments, people_of_departments  #     *    импорт всех функций

def show_departments():
    for department in departments:
        print(department)

def show_people_of_departments():
    for people in people_of_departments:
        print(people)

def enter_id_of_departments_and_people():
    department_id = int(input("Введите id oтдела:"))
    #TODO : обработка случая, если id отдела некорректный
    department = [d for d in departments if d["id"] == department_id][0]
    print("people_of_departments ids:", department["people_of_departments"])


def add_department():
    name = input("Введите название отдела: ")
    # TODO : найти максимальный номер отдела и увееличить на 1
    departments.append(
        {"id": departments[-1]["id"] +1,
         "name":name,
         "people_of_departments ":[]
         })
def ad_people_of_departments():
    fio = input("Введите имя и фамилию латинскими буквами: ")
    people_of_departments.append(
        {"id": people_of_departments[-1]["id"] +1,
         "fio":fio,
         "salary":[]
         })
def change_of_department_for_people():
    id_change_of_department = int(input("Введите новый id отдела для сотрудника: "))
    people_id= int(input("Введите id сoтрудника"))
    department_name = input("Введите название отдела латинскими буквами: ")
    departments.append(
        { "id":id_change_of_department,
          "name":department_name,
          "people_of_departments":people_id
        })

def quit_of_people_of_departments():
    quit_id = int(input("Введите id увольняемого сотрудника: "))
    people_id = [p for p in people_of_departments if p["id"] == quit_id][0]
    people_of_departments.remove(people_id)

def the_end():
    choice = input("Выйти из списка: да или нет ? ")
    if choice == "нет":
       return options_choiсe
    else:
        exit()

OPTIONS = {
           1: ['Вывести список отделов',show_departments],                #cсылка на функцию
           2: ['Вывести список всех сотрудников',show_people_of_departments],
           3: ['Вывести список сотрудников отдела по номеру',enter_id_of_departments_and_people],
           4: ['Добавить отдел',add_department],
           5: ['Добавить сотрудника',ad_people_of_departments],
           6: ['Поместить сотрудника в другой отдел',change_of_department_for_people],
           7: ['Уволить сотрудника',quit_of_people_of_departments],
           8: ['Выход',the_end]
}

def options_choiсe():
    for key, item in OPTIONS.items(): #метод items() возвр,список пар кортежей словаря-ключ,значение[(1, "..."),    ]
        print(key, item[0])

    return int(input('Выберите нужный пункт:'))
