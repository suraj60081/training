n = int(input("Enter number of elements: "))
S = list(map(int,input("Enter numbers separated by ',' : ").split(',')))
l =[]
for i in range(1,max(S)) :
    if i not in S :
        l.append(i)
print(l)