import random
############################# ����� ���������� ����� � ��������
rows=int(input('Size of matrix: '))
############################# ����������� ������ ��������� �������
treshold=int(input("Input treshold: "))
#r=random.randint(1,100)
mas = []
nec_mas=[]
for i in range(rows):
    mas.append([])
    for j in range(rows):
        r = random.randint(1,100)  
        mas[i].append(r)
       
sum=0
masn=1
output=0
x=0
print("Show us a randomized array")
for i in range(rows):
    print(mas[i], "\n")
print("Let's start to view necessary arrays")
for i in range(rows):
     nec_mas.append([])
     for j in range(rows):
        if(output==1):
            print("Array #",nec_mas,": ", end='')
        if(sum<treshold or sum==treshold):
            nec_mas[x].append(mas[i][j])
            output=0
            sum=sum+mas[i][j]
            print(mas[i][j]," ", end='' )
        else:
            x=x+1
            print("\nSum: ", sum);
            print("====================")
            #masn=masn+1
            sum=0
            output=1