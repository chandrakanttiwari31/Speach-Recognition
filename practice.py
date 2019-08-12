from datetime import datetime
current_date=str(datetime.now().date())

list1=current_date.split("-")
list1=list(map(int,list1))
list1=list1[::-1]

print("please enter your birthday")
b_date=input("Date of birth for example-16-05-1999 : ")
list2=b_date.split("-")
list2 = list(map(int, list2))

if(list2[1]>12 or list2[0]>31):
    print("Invalid Input")
else:
    if(list1[0]<list2[0]):
        list1[0]=list1[0]+30
        list1[1]=list1[1]-1

    if(list1[1]<list2[1]):
        list1[1]=list1[1]+12
        list1[2]=list1[2]-1

    day=list1[0]-list2[0]
    month=list1[1]-list2[1]
    year=list1[2]-list2[2]
    print(f"you are {year} year {month} month {day} day old")
