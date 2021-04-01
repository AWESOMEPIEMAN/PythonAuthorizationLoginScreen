from tkinter import *
from tkinter import messagebox

def login_ok():
    usern = x.get()
    passw = y.get()

    if(usern == "" and passw == ""):
        messagebox.showinfo("", "Empty boxes not allowed")


    elif(usern == "usman" and passw == "123"):
        messagebox.showinfo("", "Successfully logged in")

    else:
        messagebox.showinfo("", "Incorrect credentials")



global x
global y
r = Tk()
r.title("Blahaj Login Screen")
r.geometry("400x400")

Label(r,text="Username").place(x=10,y=10)
Label(r,text="Password").place(x=10,y=40)
x = Entry(r)
x.place(x=120,y=10)

y = Entry(r)
y.place(x=120,y=40)
y.config(show="*")

Button(r, text="Submit", command = login_ok,height = 1, width = 5).place(x=10,y=100)
r.mainloop()



