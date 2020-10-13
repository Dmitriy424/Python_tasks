a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
#The solution of the problem (Решение задачи): https://pythontutor.ru/lessons/lists/problems/same_sign_neighbours/
    
