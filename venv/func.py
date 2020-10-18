import numpy as np
import math
import sys
import matplotlib.pyplot as plt
from scipy import signal
sys.setrecursionlimit(1000)
from matplotlib.figure import Figure
import tkinter as tk

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

class func():

    def sin(self,A=1, N=1024):
        x = np.arange(0, 1024, 1)
        y = np.array([A * np.sin(2 * np.pi * i / N) for i in x])

        return x, y

    def dirac(self, gr=10, k=0, N=1024):
        delta_n = 2 * gr / N
        x = np.arange(-gr, gr, delta_n)
        y = np.array([(i == k) for i in x])

        return x, y

    def heaviside(self,gr=10, k=0, N=1024):
        delta_n = 2 * gr / N
        x = np.arange(-gr, gr, delta_n)
        y = np.array([(i >= k) for i in x])

        return x, y

    def rand_signal():
        x = np.arange(0, 1024, 1)
        y = np.random.sample(1024)

        return x, y

    def rectangular(self,S=2, N=1024):
        x = np.arange(0, 1024, 1)
        y = np.array([(i < (N / S)) for i in x])

        return x, y

    def random_signal(self,N=1024):
        x = np.arange(0, 1024, 1)
        y = np.array([np.random.randint(0, 2, 1) for i in x])

        return x, y

    def noise(self,fun):
        ns = np.random.normal(0, 0.1, 1024)
        x, y = fun

        return x, ns + y

    def radio_impulse(self,N=1024, A=1):
        k = int(1024 / 3)
        x = np.arange(0, 1024, 1)
        y = np.where(x > k, A * np.sin(5 * 2 * np.pi * x / k), 0) + np.where(x > 2 * k,
                                                                             -A * np.sin(2 * 5 * np.pi * x / k), 0)

        return x, y

    def expon(self,q=5, N=1024, alpha=0.005):
        x = np.arange(0, 1024, 1)
        # y=np.array([q*np.exp(-alpha*i) for i in x])
        y = np.array([q * np.exp(-alpha * i) * np.sin(10 * 2 * np.pi * i / N) for i in x])

        return x, y

    def predel(self,N=1024, A=1, k=7):
        x = np.arange(-512, 512, 1)
        y = np.array([(A * np.sin(2 * k * np.pi * i / N) * N) / (k * 2 * np.pi * i) for i in x])

        return x, y



