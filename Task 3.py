list1 = list(map(int, input("Введіть значення для першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть значення для другого списку через пробіл: ").split()))

set1 = set(list1)
set2 = set(list2)

only_in_list1 = set1 - set2
only_in_list2 = set2 - set1

print(f"Значення, які є тільки в першому списку: {list(only_in_list1)}")
print(f"Значення, які є тільки в другому списку: {list(only_in_list2)}")
