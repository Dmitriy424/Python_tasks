a = list(map(int, input().split()))
for i in range(0, len(a)-1, 2):
    a[i+1], a[i] = a[i], a[i+1]
print(a)
#Solve problem: https://pythontutor.ru/lessons/lists/problems/swap_neighbours/
