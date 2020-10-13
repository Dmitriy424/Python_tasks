old_list = list(map(int, input("Введите список для сортировки").split())) 
sort_list = []

def selection_sort(old_list):
    for i in range(len(old_list)):
        min1 = min(old_list)
        sort_list.append(min1)
        old_list.remove(min1)
    return sort_list

print("Сортированный список по возрастанию: ", selection_sort(old_list))
#Сортирует элементы спика по возрастанию. На вход подавать числа через пробел. (Пример - 1 2 3 4 5)
