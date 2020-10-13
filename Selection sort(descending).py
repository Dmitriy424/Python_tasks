old_list = list(map(int, input().split()))
sort_list = []

def selection_sort(old_list):
    for i in range(len(old_list)):
        max1 = max(old_list)
        sort_list.append(max1)
        old_list.remove(max1)
    return sort_list

print(selection_sort(old_list))
#Сортирует элементы спика по убыванию. На вход подавать числа через пробел. (Пример - 1 2 3 4 5)
