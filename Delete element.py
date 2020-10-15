a = list(map(int, input().split()))
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(a)
#Solve problem: https://pythontutor.ru/lessons/lists/problems/remove_element/
