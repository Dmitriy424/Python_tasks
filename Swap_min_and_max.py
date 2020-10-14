a = list(map(int, input().split()))
nindex = a.index(min(a))
xindex = a.index(max(a))
a[nindex], a[xindex] = a[xindex], a[nindex]
print(a)
#Solve the problem: https://pythontutor.ru/lessons/lists/problems/swap_min_and_max/
