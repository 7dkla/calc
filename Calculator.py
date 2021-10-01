#ارفاق المكتبة الخاصة ب gui 
from tkinter import *

#____________________________________________________
# اساس البرنامج حيث تنتقل قيمة الشاشة كاملة لاسم root
root = Tk()

#_______________________________
# العنوان في اعلى الشاشة
root.title("Calculator")

#________________________________________________
# الشريط المستطيل التي تظهر فيه الارقام بعد ضغطها
entry = Entry(root,width=60,borderwidth=7,bg="lightyellow")

#______________________________________
# وضع الشريط المستطيل على الشاشة
entry.grid(column=0,row=0,columnspan=3,)


#______________________________
#وظيفة زر الحذف (clear)
def clearing():
     entry.delete(0,END)

#___________________________________
# وظيفة ازرار الارقام فقط
def aclick(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(number) + str(current))

#_________________________
# وظيفة زر الجمع
def plus():
    first = entry.get()
    entry.delete(0, END)
    global fn
    fn = first
    global math
    math = "+"

#_______________________
# وظيفة زر الطرح
def takeaway():
    first = entry.get()
    entry.delete(0,END)
    global fn
    fn = first
    global math
    math = "-"

#___________________
# وظيفة زر اليساوي
def equal():
    second = entry.get()
    entry.delete(0,END)
    global sn
    sn = second
    if math == "-":
        entry.insert(0,int(fn) - int(sn ))
    elif math == "+":
        entry.insert(0,int(fn) + int(sn))



#________________________________________________
#صناعة الازرار بالاضافة الى ارفاق وظائفها اليها :
button1 = Button(root,text="1",pady=30,padx=65,bg="silver",command=lambda : aclick(1))
button2 = Button(root,text="2",pady=30,padx=57,bg="silver",command=lambda : aclick(2))
button3 = Button(root,text="3",pady=30,padx=55,bg="silver",command=lambda : aclick(3))
button4 = Button(root,text="4",pady=30,padx=65,bg="silver",command=lambda : aclick(4))
button5 = Button(root,text="5",pady=30,padx=57,bg="silver",command=lambda : aclick(5))
button6 = Button(root,text="6",pady=30,padx=55,bg="silver",command=lambda : aclick(6))
button7 = Button(root,text="7",pady=30,padx=65,bg="silver",command=lambda : aclick(7))
button8 = Button(root,text="8",pady=30,padx=57,bg="silver",command=lambda : aclick(8))
button9 = Button(root,text="9",pady=30,padx=55,bg="silver",command=lambda : aclick(9))
button0 = Button(root,text="0",pady=32,padx=65,bg="silver",command=lambda : aclick(0))
buttont = Button(root,text="--",pady=32,padx=55,bg="silver",command=takeaway)
buttonp = Button(root,text="++",pady=78,padx=50,bg="silver",command=plus)
buttonc = Button(root,text="CLEAR",pady=33,padx=51,bg="cyan",command=clearing)
buttone = Button(root,text="==",pady=33,padx=52,bg="silver",command=equal)

#________________________
# وضع الازرار على الشاشة
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button0.grid(row=5,column=0)
buttone.grid(row=5,column=1)
buttonp.grid(row=5,column=2,rowspan=2)
buttonc.grid(row=6,column=0)
buttont.grid(row=6,column=1,)













root.mainloop()