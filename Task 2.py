shortening = {}

while True:
    print("\nСервіс скорочення посилань:")
    print("1. Скоротити посилання")
    print("2. Довге посилання за короткою назвою")
    user_i = input("Введіть ваш вибір (1/2): ")

    if user_i == "1":
        long_url = input("Введіть довге посилання: ")
        short_url = input("Введіть коротку назву: ")
        shortening[short_url] = long_url
        print(f"Посилання {long_url} тепер можна отримати за назвою {short_url}")

    elif user_i == "2":
        short_url1 = input("Введіть коротку назву: ")
        long_url1 = shortening.get(short_url1, "Не знайдено")
        print(f"Посилання за назвою {short_url1}: {long_url1}")
