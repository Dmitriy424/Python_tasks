a = list(map(int, input().split()))
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i])
#The solution of the problem (Решение задачи): https://pythontutor.ru/lessons/lists/problems/increasing_neighbours/
