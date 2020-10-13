line = list(map(int, input().split()))
height = int(input())
line.append(height)
sort_list = []

def selection_sort(line):
    for i in range(len(line)):
        max1 = max(line)
        sort_list.append(max1)
        line.remove(max1)
    return sort_list
    
print(selection_sort(line).index(height)+1)
#The solution of the problem(Решение задачи): https://pythontutor.ru/lessons/lists/problems/lineup/
