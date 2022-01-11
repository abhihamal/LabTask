h=int(input("Number of classes held"))
a=int(input("Number of class attended"))
p=a/h*100
print(f"Percentage of class attended is {p}%.")
if p>=75:
    print("Student is allowed to attend the examination .")
elif p<=75:
    print("Student is not allowed to attend the examination")