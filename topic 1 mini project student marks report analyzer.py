"""A user enters a student’s marks in 5 subjects

The program calculates:

Total marks

Average marks

Percentage

Grade (based on average)

Whether the student passed or failed
Plan
----------------------------------------
-->to know how many students detail they are going to add
-->get them as input in int then you can get the much information alone
-->first student name
--> they have to enter their mark one by one
--> simantenously adding them
--> then taking average for them with help of counting the marks the enter and
add the elements
--> then taking percentagge (marks obtain/500)*100
-->then assign the grade with average
--> whether student passed or failed
Convert-to-code
n=int(input("how many student detials you want to enter"))
for i in range(1,n+1):
    name=int(input("enter the name of student"))
    marks=[]
    total=0
    for j in range(1,6):
        mark=int(input("enter the number"))
        marks.append[mark]
    for m in marks:
        if m==0:
            print("subject 1 mark is :",marks[m])
        elif m==1:
            print("subject 2 mark is :",marks[m])
        elif m==2:
            print("subject 3 mark is :",marks[m])
        elif m==3:
            print("subject 4 mark is :",marks[m])
        elif m==4:
            print("subject 5 mark is :",marks[m])
    total=total+marks
    print("total mark :",total)
    average=total/5
    print("Average Mark : ",average)
    percentage=(total/500)*100
    print("Percentage is :",percentage)
    if average>90:
        print("A+ grade")
    elif average>70:
        print("A grade")
    elif average>60:
        print("B+grade")
    elif average>50:
        print("c grade")
    else:
        print("fail")
    status="Pass"
    for mark in marks:
        if mark<35:
            status="fail"
    print("status :",status)

        
"""
n=int(input("How many student detail you want to enter "))
for i in range(1,n+1):
    name=input("enter the name of student ")
    marks=[]
    total=0
    for j in range(1,6):
        mark=int(input(f"enter the mark for subject {j} (0-100) :"))
        marks.append(mark)
        total=total+mark
    print("------student report----------")
    print("name : ",name)
    print("Marks :",marks)
    print("total mark : ",total)
    average=total/5
    print("Average Mark : ",average)
    percentage=(total/500)*100
    print("Percentage is :",percentage)
    status="Pass"
    if average>90:
        print("grade is : A+ grade")
    elif average>70:
        print("grade is : A grade")
    elif average>60:
        print("grade is : B+ grade")
    elif average>50:
        print("grade is : c grade")
    else:
        print("grade is : d grade")
    
    for mark in marks:
        if mark<35:
            status="fail"
    print("status :",status)
