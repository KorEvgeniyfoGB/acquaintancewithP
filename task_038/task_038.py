import os

filename = "phone.csv"


def load():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="UTF-8") as f:
            lstphone = f.readlines()
        return lstphone


def safe(lstphone):
    with open(filename, "w", encoding="UTF-8") as f:
        for line in lstphone:
            if line != "\n":
                f.write(line)
            elif line == "\n":
                continue


def add_phone(lstphone):
    name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите телефон: ")
    lstphone1 = [last_name, name, surname, phone]
    lstphone.append(",".join(lstphone1) + "\n")
    safe(lstphone)
    return "Запись добавлена"


def search_phone(lstphone, object):
    d = []
    for line in lstphone:
        if object in line.split(",") or object.capitalize() in line.split(","):
            d.append(line)
    if len(d) != 0:
        d = [i.split(",") for i in d]
        return [" ".join(i) for i in d]
    else:
        return "Записи не найдено"


def del_phone(lstphone, object):
    object = search_phone(load(), object)
    if object == "Записи не найдено":
        return "Нечего удалять"
    elif len(object) == 1:
        lstphone.remove(",".join(object[0].split()) + "\n")
        safe(lstphone)
        return "Запись удалена"
    else:
        print(*object, sep="")
        lstphone.remove(",".join(object[int(input("Введите номер записи")) - 1].split()) + "\n")
        safe(lstphone)
        return "Запись удалена"


def show_tell(lstphone):
    for line in lstphone:
        print(" ".join(line.split(",")), end="")


def rename_phone():
    del_phone(load(), input("Кого заренеймить"))
    add_phone(load())


if __name__ == "__main__":
    load()
    while True:
        action = input(
            "1 - Добавить данные \n2 - Искать данные \n3 - Посмотреть \n4 - Удалить запись \n5 - Переименовать \n6 - Выход \n")
        if action == "1":
            s = add_phone(load())
        elif action == "2":
            print(*search_phone(load(), input("Введите искомое: ")))
        elif action == "3":
            show_tell(load())
        elif action == "4":
            print(del_phone(load(), input("Кого желаете удалить?: ")))
        elif action == "5":
            rename_phone()
        elif action == "6":
            print("Good bye!")
            break
        else:
            print("Подумай!!!")