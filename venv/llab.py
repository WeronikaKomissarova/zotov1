import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from tkinter import *
import func



class quad():
    def __init__(self,frame):
        self.enl(frame)
    def enl(self,frame):
        fgr = plt.figure()
        self.pl = fgr.add_subplot(1, 1, 1)
        gr = FigureCanvasTkAgg(fgr, frame)
        canvas = gr.get_tk_widget()
        canvas.pack()

    def draw_1(self):
        x,y=func.sin()
        y.tofile('functions.txt', sep='\n')
        pltt=self.pl
        pltt.plot(x,y)

class valeurs(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, width=600, height=200, bg="light grey")
        Label(self, text="sin(x)", bg="light grey").grid(row=0, column=0, padx=20)
        Button(self, text="Draw", command=can.draw_1).grid(row=1, column=0, pady=15, padx=20)

if __name__ == "__main__":
    root = Tk()
    f_graph=LabelFrame(text='График')
    can = quad(f_graph)
    f_graph.pack(padx=10,pady=10)
    #b=Button(text="clear zone", command=can.enl)
    #b.pack(side=BOTTOM)# .pack(padx=5, pady=5)
    #can.pack(side=BOTTOM)
    #can.pack(padx=5, pady=5)
    frame = valeurs(root)
    frame.pack(padx=5, pady=5)

    root.mainloop()

'''
root=Tk()
root.title('lab1')
fgr=plt.figure()
x,y= func.rectangular()
y.tofile('functions.txt', sep='\n')
plt.plot(x,y)
root.mainloop()
'''