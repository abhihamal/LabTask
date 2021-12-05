#ts and display total WAP which accepts marks of four subjecmarks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail \
e=int(input("enter the first subject: "))
s=int(input("enter the seconnd subject: "))
m=int(input("enter the third subject: "))
h=int(input("enter the fourth subject"))
totalmark=e+s+m+h
print("the total mark is", totalmark )
percentage=(totalmark/400)*100
print("your percentage is", percentage, "%")
if percentage  > 70:
    print("congrets you got distinction ")
elif percentage > 60:
    print("you got first division")
elif percentage > 40:
    print("you got second division")
elif percentage < 40:
    print("sorry to say but you failed try again good luck")

    