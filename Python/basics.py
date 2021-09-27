""" for i in range(5):
    if i % 1==0:
        print(i)
        """
        

name=[]
physics=[]
maths=[]
chem=[]
pas=[]
fail=[]
fail1=[]
grade=[]

n=int(input("Enter no of studnets in class"))
for i in range(0,n):
    name.append(input("enter name"))
    physics.append(int(input("enter marks in physics")))
    maths.append(int(input("enter marks in maths")))
    chem.append(int(input("enter marks in chemistry")))
    if (physics[i]>=50 and maths[i]>=50) or (chem[i]>=50 and maths[i]>=50) or (physics[i]>=50 and chem[i]>=50):
        pas.append(name[i])
        per=((physics[i]+maths[i]+chem[i])/300)*100
        grade.append(per)
        if physics[i]<50 or maths[i]<50 or chem[i]<50:
            fail1.append(name[i])
    else:
        fail.append(name[i])

print("1. List of students failed in more than two subjects: \n",fail)
print("2. List of students failed in one subject: \n",fail1)
print("3. Overall class performance: \n")
for i in pas:
    if int(grade[pas.index(i)])>=80:
        print(i,"distinction",grade[pas.index(i)],"%")
    elif int(grade[pas.index(i)])>=60 and int(grade[pas.index(i)])<80:
        print(i,"First division",grade[pas.index(i)],"%")
    elif int(grade[pas.index(i)])>=50 and int(grade[pas.index(i)])<60:
        print(i,"Second division",grade[pas.index(i)],"%")