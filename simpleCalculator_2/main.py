from tkinter import *


root = Tk()

root.geometry("600x610")
root.title("Simple Calculator")


blank = Entry(root,font=("Arial","40","bold"))
blank.place(x=0,y=0,
            width=600,height=100)


def delete():
    global number_list
    number_list = []
    global operation_list
    operation_list = []
    global all_list
    all_list = []
    blank.delete(0,"end")

def click_num (NO):
    blank.insert(END,NO)

def dot(text):
    blank.insert(END,text)

def sum(text):
    global number_list
    number_list = []
    number_list.append("+")
    blank.insert(END,text)

def min(text):
    global number_list
    number_list = []
    number_list.append("-")
    blank.insert(END,text)

def multi(text):
    global number_list
    number_list = []
    number_list.append("*")
    blank.insert(END,text)

def div(text):
    global number_list
    number_list = []
    number_list.append("/")
    blank.insert(END,text)


def eq():
    all_list = []
    for i in blank.get():
        all_list.append(blank.get())
        for i in all_list:
            if number_list [0] == "+":
                numbers = (i.split("+"))
                number_1 = float(numbers[0])
                if len(numbers) == 1:
                    continue
                number_2 = float(numbers[1])
                result = number_1 + number_2
                blank.delete(0, "end")
                result = str(result)
                blank.insert(END,result)
            if number_list [0] == "-":
                numbers = (i.split("-"))
                if numbers[0] == "":
                    continue
                number_1 = float(numbers[0])
                if len(numbers) == 1:
                    continue
                number_2 = float(numbers[1])
                result = number_1 - number_2
                blank.delete(0, "end")
                result = str(result)
                blank.insert(END,result)
            if number_list [0] == "*":
                numbers = (i.split("*"))
                number_1 = float(numbers[0])
                if len(numbers) == 1:
                    continue
                number_2 = float(numbers[1])
                result = number_1 * number_2
                blank.delete(0, "end")
                result = str(result)
                blank.insert(END,result)
            if number_list [0] == "/":
                numbers = (i.split("/"))
                number_1 = float(numbers[0])
                if len(numbers) == 1:
                    continue
                number_2 = float(numbers[1])
                result = number_1 / number_2
                blank.delete(0, "end")
                result = str(result)
                blank.insert(END,result)


c_button = Button(root,text="C",font=("Arial","30","bold"),fg="green",command=delete)
c_button.place(x=1,y=110,
              width=450 , height=100)

button_0 = Button(root,text=int(0),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(0))
button_0.place(x=0,y=510,
              width=150 ,height=100)

button_1 = Button(root,text=int(1),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(1))
button_1.place(x=0,y=410,
              width=150 ,height=100)

button_2 = Button(root,text=int(2),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(2))
button_2.place(x=150,y=410,
              width=150 ,height=100)

buton_3 = Button(root,text=int(3),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(3))
buton_3.place(x=300,y=410,
              width=150 ,height=100)

button_4 = Button(root,text=int(4),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(4))
button_4.place(x=0,y=310,
              width=150 ,height=100)

button_5 = Button(root,text=int(5),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(5))
button_5.place(x=150,y=310,
              width=150 ,height=100)

button_6 = Button(root,text=int(6),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(6))
button_6.place(x=300,y=310,
              width=150 ,height=100)

button_7 = Button(root,text=int(7),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(7))
button_7.place(x=0,y=210,
              width=150 ,height=100)

button_8 = Button(root,text=int(8),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(8))
button_8.place(x=150,y=210,
              width=150 ,height=100)

button_9 = Button(root,text=int(9),font=("Arial","30","bold"),fg="blue",command= lambda: click_num(9))
button_9.place(x=300,y=210,
              width=150 ,height=100)

button_eq = Button(root,text="=",font=("Arial","30","bold"),fg="purple",command=eq)
button_eq.place(x=300,y=510,
              width=300 ,height=100)

button_dot = Button(root,text=".",font=("Arial","30","bold"),fg="purple",command=lambda: dot ("."))
button_dot.place(x=150,y=510,
              width=150,height=100)

button_sum = Button(root,text="+",font=("Arial","30","bold",),fg="red",command=lambda: sum ("+"))
button_sum.place(x=450,y=110,
              width=150 ,height=100)

button_min = Button(root,text="-",font=("Arial","30","bold"),fg="red",command=lambda: min ("-"))
button_min.place(x=450,y=210,
              width=150 ,height=100)

button_multi = Button(root,text="*",font=("Arial","30","bold"),fg="red",command=lambda: multi ("*"))
button_multi.place(x=450,y=310,
              width=150 ,height=100)

button_div = Button(root,text="/",font=("Arial","30","bold"),fg="red",command=lambda: div ("/"))
button_div.place(x=450,y=410,
              width=150 ,height=100)


root.mainloop()