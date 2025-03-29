import tkinter as tk
from tkinter.constants import CENTER
import datetime

dday=0
count=0
d2=0
d1=0
sh=0
tsday=15
year=2025
month=0
def gett():
    global dday
    global d1
    global d2
    global year
    global count
    global tsday
    global month
    count=0
    today = datetime.date.today()
    d1 = datetime.date(today.year, today.month, today.day)
    d2 = datetime.date(year, 1, tsday)
    month=today.month
    dday=(d2-d1).days
    while dday<0:
        year+=1
        d2 = datetime.date(year, 1, tsday)
        dday=(d2-d1).days
    while d2.weekday()!=5:
        tsday+=1
        d2 = datetime.date(year, 1, tsday)
        dday=(d2-d1).days

def cht():
    global count
    global sh
    global year
    global dday
    global month
    dday+=365
    count+=1
    if count<3:
        sh=dday
    elif count>=3 and count<10:
        sh="包一包"
    elif count>=10 and count<15:
        sh="回家睡"
    elif count>=15 and count<20:
        sh="零級分"
    elif count>=20 and count<25:
        sh="不用看"
    elif count>=25 and count<30:
        sh="還不讀"
    elif count>=30 and count<35:
        sh="沒救了"
    elif count>=35 and count<40:
        sh="好了嗎"
    elif count>=40 and count<45:
        sh="我不讀"
    elif count>=45 and count<50:
        sh="我就爛"
    else:
        if year>2026:
            sh="Wadis"
        elif year==2026 and month>6:
            sh="Wadis"
        else:
            sh=""
        count=100
def push():
    global c
    global sh
    c.destroy()
    cht()
    c = tk.Label(text=sh,font=('Arial',80,'bold'),fg='#000')
    c.grid(column=0, row=2, ipadx=0, ipady=16, columnspan=2)

def reset():
    gett()
    global c
    c.destroy()
    c = tk.Label(text=dday,font=('Arial',80,'bold'),fg='#000')
    c.grid(column=0, row=2, ipadx=0, ipady=16, columnspan=2)

window = tk.Tk()
window.title('學測倒數')
window.geometry('400x300')
window.resizable(0,0)
gett()
a = tk.Label(text='距離學測',font=('Arial',40,'bold'),fg='#000')
b = tk.Label(text='剩下',font=('Arial',20,'bold'),fg='#000')
c = tk.Label(text=dday,font=('Arial',80,'bold'),fg='#000')
d = tk.Button(text="Reset",command=reset,font=('Arial',12,'bold'),fg='#000')
e = tk.Button(text="先加個365",command=push,font=('Arial',12,'bold'),fg='#000')
a.grid(column=0, row=0, ipadx=83, columnspan=2)
b.grid(column=0, row=1, ipadx=0, columnspan=2)
d.grid(column=0, row=3, ipadx=70)
e.grid(column=1, row=3, ipadx=54)
c.grid(column=0, row=2, ipadx=0, ipady=16, columnspan=2)
window.mainloop()
