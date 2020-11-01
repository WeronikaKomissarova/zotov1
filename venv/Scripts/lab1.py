import pylab
import math
M1 = list(range(0, 1000, 1))
M2 = []
i = 0
M3 = []
k =int(input("Введите число отрезков разбиения: "))
n = len(M1)
dn = int(len(M1)/k)
def U(n:int):
    if n < 0:
        return 0
    else:
        return 1

while i < 1000:
    x = ((1/(400*math.sqrt(2*math.pi)))*math.exp((-(M1[i]-500)*(M1[i]-500))/(2*400*400)))*10**7
    M2.append(x)
    i += 1

for x in M1:
    s=M2[0]*U(x)
    for j in range(1, k):
        s+=(M2[j*dn]-M2[(j-1)*dn])*U(x-j*dn)
    M3.append(s)

pylab.title('График Гауссового распределения', fontsize=20, fontname='Times New Roman')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.grid(True)
pylab.plot(M1, M2, markersize=0.5, marker='o', c='r', linewidth=0.5)
pylab.plot(M1, M3, markersize=0.5, marker='o', c='b', linewidth=0.5)
pylab.show()