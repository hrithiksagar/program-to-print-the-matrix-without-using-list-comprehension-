l=[]
n=int(input("enter the number of rows: "))
m=int(input("enter number of columns: "))
for i in range(n):
    l1=[]
    for j in range(m):
        x=int(input("enter the list element: "))
        l1.append(x)
        print(l1)
    l.append(l1)
print(l)    
