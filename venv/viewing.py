from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from func import func

root=Tk()
root.title('ЦОС')

def clicked():
    func(selected.get())
    
    #function=getattr(func,selected.get())
    #x,y=function()
    pass

selected=StringVar()
selected.set('sin')
rad1=Radiobutton(root,text='sin',value='sin',variable=selected).grid(column=0,row=0)
rad2=Radiobutton(root,text='heaviside',value='heaviside',variable=selected).grid(column=1,row=0)
rad3=Radiobutton(root,text='dirac',value='dirac',variable=selected).grid(column=2,row=0)
rad4=Radiobutton(root,text='rand_signal',value='rand_signal',variable=selected).grid(column=3,row=0)
rad5=Radiobutton(root,text='rectangular',value='rectangular',variable=selected).grid(column=4,row=0)
rad6=Radiobutton(root,text='random_signal',value='random_signal',variable=selected).grid(column=5,row=0)
rad7=Radiobutton(root,text='noise',value='noise',variable=selected).grid(column=6,row=0)
rad8=Radiobutton(root,text='radio_impulse',value='radio_impulse',variable=selected).grid(column=7,row=0)
rad9=Radiobutton(root,text='expon',value='expon',variable=selected).grid(column=8,row=0)
rad10=Radiobutton(root,text='predel',value='predel',variable=selected).grid(column=9,row=0)
but=Button(root,text='Draw',command=clicked() ).grid(column=4,row=1)


root.mainloop()