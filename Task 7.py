employees = {}

while True:
    print("\nОблік кадрів:")
    print("1. Додати співробітника")
    print("2. Показати співробітників")
    print("3. Найефективніший співробітник")
    print("4. Вийти")

    op = input("Введіть ваш вибір: ")

    if op == "1":
        surname = input("Прізвище: ")
        position = input("Посада: ")
        experience = input("Досвід роботи: ")
        portfolio = input("Портфоліо: ")
        efficiency = float(input("Коефіцієнт ефективності: "))
        tech_stack = input("Стек технологій: ")
        salary = float(input("Зарплата: "))

        employees[surname] = {
            'Посада': position,
            'Досвід роботи': experience,
            'Портфоліо': portfolio,
            'Коефіцієнт ефективності': efficiency,
            'Стек технологій': tech_stack,
            'Зарплата': salary
        }

    elif op == "2":
        for surname, details in sorted(employees.items()):
            print(f"{surname}:")
            for key, value in details.items():
                print(f"  {key}: {value}")

    elif op == "3":
        max_efficiency = max(employees, key=lambda x: employees[x]['Коефіцієнт ефективності'])
        print(f"Найефективніший співробітник: {max_efficiency}")

    elif op == "4":
        break
