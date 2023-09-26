library = {}

while True:
    print("\nБібліотека:")
    print("1. Додати новий запис")
    print("2. Показати всі записи")
    print("3. Сортувати за автором")
    print("4. Сортувати за твором")

    op = input()

    if op == "1":
        author = input("Додайте автора: ")
        writing = input("Додайте твір: ")
        library[author] = writing

    elif op == "2":
        for author, writing in library.items():
            print(f"{author}: {writing}")

    elif op == "3":
        for author in sorted(library.keys()):
            print(f"{author}: {library[author]}")

    elif op == "4":
        for author, writing in sorted(library.items(), key=lambda item: item[1]):
            print(f"{author}: {writing}")

    else:
        print("Немає такої опції.")