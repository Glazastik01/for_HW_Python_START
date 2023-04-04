import model

def menu():
    print("\nТелефонный справочник")
    model.line()
    print("Что делать?\n")
    print("1. Поисковик")
    print("2. Ввести новую информацию")
    print("3. Просмотр справочника")
    print("4. Удаление информации")
    print("5. Выйти из программы\n")


def search_start():
    print("\nПоисковик")
    model.line()

def search_controls():
    print("Продолжить искать?")
    print("1. Да")
    print("2. Нет")

def save_start():
    print("\nВвод информации")
    model.line()

def show_start():
    print("\nПросмотр справочника")
    model.line()

def show_controls():
    print("1. Следующая строчка")
    print("2. Предыдущая строчка")
    print("3. Изменить информацию")
    print("4. Выйти из просмотра")

def delete_start():
    print("\nУдаление информации")
    model.line()

def delete_controls():
    print("1. Удалить данную строку")
    print("2. Следующая строчка")
    print("3. Предыдущая строчка")
    print("4. Выйти из просмотра")