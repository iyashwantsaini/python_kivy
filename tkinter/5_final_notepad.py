import  tkinter as tk
from tkinter import *
import tkinter.filedialog
root=tk.Tk()
root.title('Notepad')

w, h = root.winfo_screenwidth()/2, root.winfo_screenheight()/2
root.geometry("%dx%d+0+0" % (w, h))

menu=Menu(root)
root.config(menu=menu)

def donothing():
    pass

def fileSelector():
    c=tk.filedialog.askopenfile()
    f=open(c.name)
    textArea.insert(INSERT,f.read())

def fileSaver():
    c=tk.filedialog.asksavefile()
    f=open(c.name)
    c.save()

def exit():
    root.destroy()


filemenu=Menu(menu,tearoff=0)
editmenu=Menu(menu,tearoff=0)
formatmenu=Menu(menu,tearoff=0)
viewmenu=Menu(menu,tearoff=0)
helpmenu=Menu(menu,tearoff=0)

menu.add_cascade(label='File',menu=filemenu)
menu.add_cascade(label='Edit',menu=editmenu)
menu.add_cascade(label='Format',menu=formatmenu)
menu.add_cascade(label='View',menu=viewmenu)
menu.add_cascade(label='Help',menu=helpmenu)

filemenu.add_command(label='New',command=fileSelector)
filemenu.add_command(label='Open',command=donothing)
filemenu.add_command(label='Save',command=fileSaver)
filemenu.add_command(label='Save As..',command=fileSaver)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit)

editmenu.add_cascade(label='Undo',command=donothing)
editmenu.add_separator()
editmenu.add_cascade(label='Cut',command=donothing)
editmenu.add_cascade(label='Copy',command=donothing)
editmenu.add_cascade(label='Paste',command=donothing)
editmenu.add_cascade(label='Delete',command=donothing)

textArea=tk.Text(root)

def resize(event):
    pixelX=root.winfo_width()
    pixelY=root.winfo_height()
    textArea["width"]=int(round(pixelX)) 
    textArea["height"]=int(round(pixelY))

textArea.bind("<Configure>", resize)
textArea.pack()

root.mainloop()