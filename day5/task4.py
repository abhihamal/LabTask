from tkinter import*
root=Tk()
root.geometry("300x200")
root.title("Login Page")
def submit():
    print("Successfully logged in!")
label_1=Label(root,text="Log In",font='times 15 bold').grid(row=0,column=3)
name= Label(root,text="Username or Email").grid(row =1, column=2)
e1= Entry(root).grid(row=1,column=3)
password= Label(root, text ="Password").grid(row=2, column=2)
e2= Entry(root).grid(row=2,column=3)
sub=Button(root,text="Submit",command=submit()).grid(row=3,column=3)
root.mainloop()