import view

def line():
    print("————————————————————————————————————————————————————————")

def search():
    view.search_start()
    while True:
        isthere = input("\nКого искать?\n\n")
        with open("phoneBook.txt", "r") as file:
            for line in file:
                count = 1
                if isthere in line:
                    print(f"\n{count}. {line}")
                    count += 1
        view.search_controls()
        choice = input("\n➥  ")
        if choice == "1":
            pass
        if choice == "2":
            break

def info():
    name = input("\nВведите имя:  ").replace(" ", "-")
    phone = input("Введите телефон:  ").replace(" ", "-")
    full_info = f"{name} {phone}\n"
    return full_info

def save():
    view.save_start()
    with open("phoneBook.txt", "a") as file:
        file.write(info())
    print("\nВаша информация сохранена!")

def show_edit(fileName, toedit, sorted):
    sorted[toedit] = info()
    with open(fileName, "w") as file:
        file.writelines(sorted)

def show():
    view.show_start()
    with open("phoneBook.txt", "r") as file:
        curPage = 0
        lines = file.readlines()
        size = len(lines)
        while True:
            print(f"\nСтрока №{curPage + 1} из всего {size}\n")
            print(lines[curPage])
            view.show_controls()
            choice = input("\n➥  ")
            if choice == "1":
                curPage += 1
            if choice == "2":
                curPage -= 1
            if choice == "3":
                show_edit("phoneBook.txt", curPage, lines)
            if choice == "4":
                break

def deletion(fileName, todel, sorted):
    sorted[todel] = ""
    with open(fileName, "w") as file:
        file.writelines(sorted)

def delete():
    view.delete_start()
    with open("phoneBook.txt", "r") as file:
        curPage = 0
        lines = file.readlines()
        size = len(lines)
        while True:
            print(f"\nСтрока №{curPage + 1} из всего {size}\n")
            print(lines[curPage])
            view.delete_controls()
            choice = input("\n➥  ")
            if choice == "1":

                deletion("phoneBook.txt", curPage, lines)
                print("\nУдаление прошло успешно!")
                break

            if choice == "2":
                curPage += 1
            if choice == "3":
                curPage -= 1
            if choice == "4":
                break