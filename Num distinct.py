a = list(map(int, input().split()))
counter = 1

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        counter += 1

print(counter)
#The solution of the problem (Решение задачи): https://pythontutor.ru/lessons/lists/problems/num_distinct/
