Dict = {'hello':2,'Python':1,'world':3}

l = []
for i in Dict.values() :
    l.append(i)
print("Noraml values: ",l)
l.sort()
print(l)
Dict1 = {}
for i in l :
    for k,v in Dict.items():
        if v==i:
            Dict1[i]=k
print(Dict1)
