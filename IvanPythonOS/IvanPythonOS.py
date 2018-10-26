import random
############################# Введём размер матрицы
rows=int(input('Size of matrix: '))
############################# Введем пороговое значение для суммы
treshold=int(input("Input treshold: "))
 
mas = []
necmas=[]
############################# Сгенерируем массив
for i in range(rows):
    mas.append([])
    for j in range(rows):
        r = random.randint(1,100)  
        mas[i].append(r)
     
sum=0
x=0
############################# Выведем сгенерированный массив
print("Show us a randomized array")
for i in range(rows):
    print(mas[i], "\n")
############################# Приступим к сортировке
print("Let's start to view necessary arrays")
necmas.append([])
for i in range(rows):
     for j in range(rows):
        if(sum<treshold or sum==treshold):
            necmas[x].append(mas[i][j])
            sum=sum+mas[i][j]
        else:
            necmas.append([])
            x=x+1
            print("Array #", x,": ", necmas[x-1])
            print("Sum: ", sum)
            print("=====================")
            sum=mas[i][j]
            necmas[x].append(mas[i][j])