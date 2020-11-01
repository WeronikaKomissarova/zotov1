from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import func

root=Tk()
root.title('ЦОС')

def clicked():
    def on_change(value):
        x, y = function(sl=mu.get())
        line1.set_data(x, y)  # update data

        # set plot limit
        # ax = self.graph.figure.axes[0]
        # ax.set_xlim(min(x), max(x))
        # ax.set_ylim(min(y), max(y))

        # update graph
        graph.draw()
    function=getattr(func,selected.get())
    x,y = function()
    root=Tk()
    fig = Figure(figsize=(6, 4), dpi=96)
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y)
    graph = FigureCanvasTkAgg(fig, root)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=2)
    if (selected.get()=='noise'):
        mu = DoubleVar(root)
        mu.set(1.0)  # default value for parameter "mu"
        slider_mu = Scale(root,
                          from_=10, to=0, resolution=0.001,
                          label='mu', variable=mu,
                          command=on_change
                          )
        slider_mu.grid(row=0, column=0)
    if (selected.get()=='rectangular'):
        mu = DoubleVar(root)
        mu.set(2.0)  # default value for parameter "mu"
        slider_mu = Scale(root,
                          from_=10, to=0, resolution=0.1,
                          label='mu', variable=mu,
                          command=on_change
                          )
        slider_mu.grid(row=0, column=0)

selected=StringVar()
selected.set('heaviside')
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

but=Button(root,text='Draw',command=clicked ).grid(column=4,row=1)


root.mainloop()