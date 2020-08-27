from tkinter import *
import tkinter.font as tf
r = Tk()
r.title("My Calculator")
#---Size of the app---
#r.geometry("209x288")
r.maxsize(209,270)

#---Icon---
#r.iconbitmap("icon.ico")


#Global Menu Options
menus = Menu(r)

#---View option---
view = Menu(menus,tearoff=0)
menus.add_cascade(label="View", menu=view)
view.add_command(label="Standard", command=None)
view.add_command(label="Scientific",command=None)
view.add_command(label="Programmer",command=None)
view.add_command(label="Statistics",command=None)
view.add_command(label="History",command=None)
view.add_command(label="Digit grouping",command=None)
view.add_command(label="Basic",command=None)
view.add_command(label="Unit Conversation",command=None)
view.add_command(label="Date calculation",command=None)
view.add_command(label="Worksheets",command=None)

#---Edit---
edit = Menu(menus,tearoff=0)
menus.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_command(label="History",command=None)

#---Help---
helps = Menu(menus,tearoff=0)
menus.add_cascade(label="Help",menu=helps)
helps.add_command(label="View Help")
helps.add_command(label="About Calculator")

#---Input Section ---
fonts = tf.Font(family="Lucida",size=15)
main_input = Text(r,bg="seashell2",width="17",height=2,padx=5,font = fonts)

#main_input.pack(padx=10,pady=10)
main_input.grid(row=0,column=0,columnspan=4,padx=5,pady=10)

#--------------------------------------------FUNCTIONS--------------------------------------------------------
   
#Global Variables
number1 = 0
number2 = 0
math = ""

#Clicked any number
def click_number(numbers):
    main_input.insert(END,numbers)
    
#Addition
def add_equals():
    f_number1 = main_input.get("1.0","end-1c")
    global number1
    try:
        number1 = int(f_number1)
    except ValueError:
        print(end="")
    global math
    math ="add"
    main_input.delete("1.0",END)
    
#Subtraction        
def subtract_equals():
    f_number1 = main_input.get("1.0","end-1c")
    global number1
    try:
        number1 = int(f_number1)
    except ValueError:
        print(end="")
    global math
    math ="subtract"
    main_input.delete("1.0",END)
    
#Division
def division_equals():
    f_number1 = main_input.get("1.0","end-1c")
    global number1
    try:
        number1 = int(f_number1)
    except ValueError:
        print(end="")
    global math
    math ="divide"
    main_input.delete("1.0",END)   

#Equals
def equals():
    f_number2 = main_input.get("1.0","end-1c")
    global number2
    try:
        number2 = int(f_number2)
    except ValueError:
        print(end="")
    main_input.delete("1.0",END)
    if math=="add":
            main_input.insert("1.0",eval("number1+number2"))
    elif math=="subtract":
        main_input.insert("1.0",eval("number1-number2"))
    elif math=="divide":
        main_input.insert("1.0",eval("(number1/number2)"))

#Clear button function
def clear():
    main_input.delete("1.0",END)


#----------------------------------------------Numbers and Buttons ---------------------------------------

b1 = Button(r,width=3,height=2,bg="light blue",text="1",padx=5,relief=FLAT,command=lambda:click_number(1))
b2 = Button(r,width=3,height=2,bg="light blue",text="2",padx=5,relief=FLAT,command=lambda:click_number(2))
b3 = Button(r,width=3,height=2,bg="light blue",text="3",padx=5,relief=FLAT,command=lambda:click_number(3))
b4 = Button(r,width=3,height=2,bg="light blue",text="4",padx=5,relief=FLAT,command=lambda:click_number(4))
b5 = Button(r,width=3,height=2,bg="light blue",text="5",padx=5,relief=FLAT,command=lambda:click_number(5))
b6 = Button(r,width=3,height=2,bg="light blue",text="6",padx=5,relief=FLAT,command=lambda:click_number(6))
b7 = Button(r,width=3,height=2,bg="light blue",text="7",padx=5,relief=FLAT,command=lambda:click_number(7))
b8 = Button(r,width=3,height=2,bg="light blue",text="8",padx=5,relief=FLAT,command=lambda:click_number(8))
b9 = Button(r,width=3,height=2,bg="light blue",text="9",padx=5,relief=FLAT,command=lambda:click_number(9))
b0 = Button(r,width=3,height=2,bg="light blue",text="0",padx=5,relief=FLAT,command=lambda:click_number(0))


#Math
b10 = Button(r,width=3,height=2,bg="light blue",text="+",padx=5,relief=FLAT,command=add_equals)
b11 = Button(r,width=3,height=2,bg="light blue",text="-",padx=5,relief=FLAT,command=subtract_equals)
b12 = Button(r,width=3,height=2,bg="light blue",text="/",padx=5,relief=FLAT,command=division_equals)

#Clear button
b13 = Button(r,width=3,height=2,bg="light blue",text="Clear",padx=5,relief=FLAT,command=clear)
#Equal
b14 = Button(r,width=11,height=2,bg="light blue",text="=",padx=5,relief=FLAT,command=equals)


#-----------------------------Positioning Buttons-------------------------
b7.grid(row=1,column=0,padx=3,pady=5)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b10.grid(row=1,column=3)

b4.grid(row=2,column=0,pady=3)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b11.grid(row=2,column=3)

b1.grid(row=3,column=0,pady=3)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b12.grid(row=3,column=3)


b14.grid(row=4,column=0,pady=5,columnspan=2)
b0.grid(row=4,column=2)
b13.grid(row=4,column=3)



r.config(menu=menus)
r.mainloop()