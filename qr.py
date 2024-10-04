import qrcode
import tkinter as tk
from tkinter import messagebox




def new():
    e.delete(1.0, 'end-1c')


w = tk.Tk()
menu = tk.Menu(w)
w.config(menu=menu)
w['background']='#856ff8'
file_menu = tk.Menu(menu)

menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open...", command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=w.quit)

edit = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='copy', command=None)
edit.add_command(label='paste', command=None)

help = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=help)
help.add_command(label='About', command=None)
help.add_command(label='Guide', cmand=None)


def new_file():
    x = ""
    y = ""


def create():
    x = e.get()
    a = qrcode.make(x)
    y = e1.get()
    a.save(y + ".png")
    messagebox.showinfo('Info ', 'qr generated successfully  ')


w.geometry('600x400')
w.title('QR Generator')
w.resizable(width='false',height='false')
'''
img=tk.PhotoImage(file=" /storage/emulated/0/Download/panda.jpeg")
bimg=tk.Label(w,imgage=img)
bimg.pack()
'''

l = tk.Label(text="Q R   C O D E   G E N E R A T O R ", bg='#4584b6', fg='black',font=30)
l.place(x=0,y=20,width=600,height=30)

l3 = tk.Label(text=" Data:", bg="#4584b6",font=40)
l3.place(x=40, y=90,width=70,height=50)

e = tk.Entry(w, bg='rosybrown', fg='black',font=50)
e.place(x=160, y=90,width=350,height=50)



l2 = tk.Label(text="File : ", bg="rosybrown",font=40)
l2.place(x=40, y=190,width=70,height=50)

e1 = tk.Entry(w, bg='#4584b6', fg='black',font=50)
e1.place(x=160, y=190, width=350, height=50)


b = tk.Button(text="G e n e r a t e",font=150, bg='#856ff8', fg='black', command=create)
b.place(x=60, y=280, width=450, height=80)

w.mainloop()
