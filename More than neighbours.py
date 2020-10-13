a = list(map(int,input().split()))
counter = 0
for i in range(1,len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        counter += 1
print("Количество элементов, больше своих соседей: ", counter)
#The solution of the problem (Решение задачи): https://pythontutor.ru/lessons/lists/problems/more_than_neighbours/

        
