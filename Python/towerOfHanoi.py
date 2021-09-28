n=int(input("enter no of tower"))
l=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        
        if j==(n-i+1):
            s=str(i)+" "
            print(s*(i),end='')
        else:
            print(" ",end='')
    print()
    l.append(i*i)
    
for i in l :
    print("row",str(l.index(i)+1),": ",i)