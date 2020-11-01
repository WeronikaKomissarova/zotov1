import numpy as np
import math
import sys
import matplotlib.pyplot as plt
from scipy import signal
sys.setrecursionlimit(1000)
from matplotlib.figure import Figure
import tkinter as tk

N=1024
'''
    def drawing(self):
        self.title("Graph")
        fig = Figure(figsize=(6, 4), dpi=96)
        ax = fig.add_subplot(111)
        #x, y = self.data(self.n.get(), self.mu.get())
        self.line1, = ax.plot(self.x, self.y)

        self.graph = FigureCanvasTkAgg(fig, master=self)
        canvas = self.graph.get_tk_widget()
        canvas.grid(row=0, column=2)

    def on_change(self):
        x, y = self.f()
        self.line1.set_data(x, y)  # update data

        # set plot limit
        # ax = self.graph.figure.axes[0]
        # ax.set_xlim(min(x), max(x))
        # ax.set_ylim(min(y), max(y))

        # update graph
        self.graph.draw()
'''



def sin(sl=1):
    x = np.arange(0, N, 1)
    y = np.array([sl * np.sin(2 * np.pi * i / N) for i in x])
    y.tofile('sin',sep='\n')
    return x, y

def dirac(gr=10, sl=0):
    delta_n = 2 * gr / N
    x = np.arange(-gr, gr, delta_n)
    y = np.array([(i == sl) for i in x])
    y.tofile('dirac',sep='\n')
    return x, y

def heaviside(gr=10, sl=0):
    delta_n = 2 * gr / N
    x = np.arange(-gr, gr, delta_n)
    y = np.array([(i >= sl) for i in x])
    y.tofile('heav',sep='\n')
    return x, y

def rand_signal(sl=0):
    x = np.arange(0, N, 1)
    y = np.array([np.random.sample(N)])
    y.tofile('rand_sig',sep='\n')
    return x, y

def rectangular(sl=2):
    x = np.arange(0, N, 1)
    y = np.array([(i < (N / sl)) for i in x])
    y.tofile('rect',sep='\n')
    return x, y

def random_signal(sl=0):
    x = np.arange(0, N, 1)
    y = np.array([np.random.randint(0, 2, 1) for i in x])
    y.tofile('random',sep='\n')
    return x, y

def noise(fun=sin(),sl=1):
    ns = np.random.normal(0, 0.1, N)
    x, y = fun
    y+=sl*ns
    y.tofile('noise',sep='\n')
    return x, y

def radio_impulse(sl=1):
    k = int(N / 3)
    x = np.arange(0, N, 1)
    y = np.where(x > k, sl * np.sin(5 * 2 * np.pi * x / k), 0) + np.where(x > 2 * k,
                                                                             -sl * np.sin(2 * 5 * np.pi * x / k), 0)

    return x, y

def expon(q=5,  sl=0.005):
    x = np.arange(0, N, 1)
        # y=np.array([q*np.exp(-alpha*i) for i in x])
    y = np.array([q * np.exp(-sl * i) * np.sin(10 * 2 * np.pi * i / N) for i in x])
    y.tofile('exp',sep='\n')
    return x, y

def predel(sl=1, k=7):
    x = np.arange(-512, 512, 1)
    y = np.array([(sl * np.sin(2 * k * np.pi * i / N) * N) / (k * 2 * np.pi * i) for i in x])
    y.tofile('pder',sep='\n')
    return x, y



