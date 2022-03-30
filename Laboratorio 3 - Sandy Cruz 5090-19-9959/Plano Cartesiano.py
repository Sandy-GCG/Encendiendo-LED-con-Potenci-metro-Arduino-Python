import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np
from sympy import Interval, intervals

def getSerialData(self, samples, numData, serialConnection, lines):
    for i in range(numData):
        value = float(serialConnection.readline().strip())
        data[i].append(value)
        lines[i].set_data(range(samples),data[i])

serialPort = 'COM5'
serialN = 9600

try:
    serialConnection = serial.Serial(serialPort, serialN)
except:
    print('No se ha podido conectar al puerto')

samples = 200
sampleTime = 100
numData = 1

xmin = 0
xmax = samples
ymin = 0
ymax = 6

lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0]*samples, maxlen = samples))
    lines.append(Line2D([], [], color = 'blue'))

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, xlim = (xmin, xmax), ylim = (ymin, ymax))
ax1.title.set_text('MEDIDOR DE POTENCIOMETRO')
ax1.set_xlabel('Muestras')
ax1.set_ylabel('Voltios')
ax1.add_line(lines[0])

anim = animation.FuncAnimation(fig, getSerialData, fargs=(samples, numData, serialConnection, lines), interval=sampleTime)
plt.show()

serialConnection.close()