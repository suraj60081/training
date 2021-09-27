# Grading System

Name = []
Physics = []
Chem = []
Maths = []
Passed = []
Fail = []
Reappear = []
Percentage = []

students = int(input("Enter strenth of class: "))

for i in range(0,students):
    print("Enter details of ",i+1,": student in following format- Name, Physics marks, Chemistry marks, Maths marks")
    Name.append(input("Enter Name: "))
    Physics.append(int(input("Enter marks in Physics: ")))
    Chem.append(int(input("Enter marks in Chemistry")))
    Maths.append(int(input("Enter marks in Maths")))
    Percentage.append(((Physics[i]+Chem[i]+Maths[i])/300)*100)
    if(Physics[i]>=50 and Chem[i]>=50 or Chem[i]>=50 and Maths[i]>=50 and Physics[i]>=50 or Maths[i]>=50):
        Passed.append(Name[i])
    elif(Physics[i]<50 or Chem[i]<50 or Maths[i]<50):
        Reappear.append(Name[i])
    else :
        Fail.append(Name[i])

print("Output 1 : Failed students ")
for i in Fail:
    print(Fail[i])

print("Output 2 : Failed in one subject")
print(Reappear)
print("output 3: overall class performance")
for i in Name:
    print(i,Percentage[Name.index[i]])
print("Output 4 : Grades")
for i in Percentage:
    if Percentage[i]<=80 or Percentage[i]>=60:
        print(Percentage[i]," : First Division")
    elif Percentage[i]<=60 or Percentage[i]>=50:
        print(Percentage[i]," : second Division")
    elif Percentage[i]>=80:
        print(Percentage[i]," : Distinction")
    else :
        continue
    

