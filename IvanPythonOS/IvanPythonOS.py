import random
############################# ����� ���������� ����� � ��������
rows=int(input('Num of rows: '))
cols=int(input('Num of cols: '))
############################# ����������� ������ ��������� �������
edge=int(input("Input treshold: "))
r=random.randint(1,100)
mas = []
for i in range(rows):
    mas.append([])
    for j in range(cols):
        mas[i].append(r)
        r = random.randint(1,100)  
sum=0
masn=1 
output=1
print("Show us a randomized array")
for i in range(rows):
    print(mas[i], "\n")
print("Let's start to view necessary arrays")
for i in range(rows):
     for j in range(cols):
        if(output==1): 
            print("Array #",masn,": ", end='')
        if(sum<edge or sum==edge):
            output=0
            sum=sum+mas[i][j]
            print(mas[i][j],", ", end='' )
        else: 
            print("\nSum: ", sum);
            print("====================")
            masn=masn+1
            sum=0
            output=1
 