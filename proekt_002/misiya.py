from tkinter import *
from PIL import Image, ImageTk
a=Tk()
a.geometry("180x270")
a.resizable(0,0)
a.title("kankulator birmartariy")
rasm = Image.open('Без.jpg').resize((1370,800))
s = ImageTk.PhotoImage(rasm)
label = Label(a, image=s)
label.place(x=0, y=0)
y=""
def h():
    d=Label(a,text=y,bg="white")
    d.place(x=5,y=50)

def g():
    global y
    y+="1"
    h()


s=Button(a,text="1",width=5,height=2,command=g)
s.place(x=0,y=100)
def g1():
    global y
    y+="2"
    h()


s1=Button(a,text="2",width=5,height=2,command=g1)
s1.place(x=45,y=100)
def g2():
    global y
    y+="3"
    h()
s2=Button(a,text="3",width=5,height=2,command=g2)
s2.place(x=90,y=100)
def g3():
    global y
    y+="4"
    h()
s3=Button(a,text="4",width=5,height=2,command=g3)
s3.place(x=0,y=145)
def g4():
    global y
    y+="5"
    h()
s4=Button(a,text="5",width=5,height=2,command=g4)
s4.place(x=45,y=145)
def g5():
    global y
    y+="6"
    h()
s5=Button(a,text="6",width=5,height=2,command=g5)
s5.place(x=90,y=145)
def g6():
    global y
    y+="7"
    h()
s6=Button(a,text="7",width=5,height=2,command=g6)
s6.place(x=0,y=190)
def g7():
    global y
    y+="8"
    h()
s7=Button(a,text="8",width=5,height=2,command=g7)
s7.place(x=45,y=190)
def g8():
    global y
    y+="9"
    h()
s8=Button(a,text="9",width=5,height=2,command=g8)
s8.place(x=90,y=190)



def g12():
    global y
    y+="0"
    h()
s12=Button(a,text="0",width=5,height=2,command=g12)
s12.place(x=45,y=230)
def g13():
    global y
    y1=eval(y)
    y=""
    if y1 ==2+2:
        y1="5"
    d=Label(a,text=y1,bg="white",fg="black",width=25)
    d.place(x=5,y=50)


    
s12=Button(a,text="=",width=5,height=2,command=g13,bg="blue")
s12.place(x=90,y=230)

def g14():
    global y
    y=""

    d1=Label(a,bg="white",width=100)
    d1.place(x=5,y=50)
def g9():
    global y
    y+="-"
    h()
s9=Button(a,text="-",width=5,height=2,command=g9,bg="green")
s9.place(x=135,y=100)
def g10():
    global y
    y+="+"
    h()
s10=Button(a,text="+",width=5,height=2,command=g10,bg="green")
s10.place(x=135,y=145)
def g11():
    global y
    y+="*"
    h()
s11=Button(a,text="*",width=5,height=2,command=g11,bg="green")
s11.place(x=135,y=190)    
    
s12=Button(a,text="C",width=5,height=2,command=g14,bg="red")
s12.place(x=0,y=230)


a.mainloop()