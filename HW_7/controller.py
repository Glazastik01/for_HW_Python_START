import view
import model

def run():
    while True:
        view.menu()
        choice = input("➥  ")
        if choice == "1":
            model.search()
        if choice == "2":
            model.save()
        if choice == "3":
            model.show()
        if choice == "4":
            model.delete()
        if choice == "5":
            print("\nExiting\n")
            break
