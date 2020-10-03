import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt
import time

    def grafico()

fileObject = open('fes_arduino.csv', 'r')

#colocar uma variavel para comando ligado ou desligado

corrente = []

for i in range 80 
    t1 = time.time()
    if t1< 10: 
        corrente = corrente + 1 #passos da corrente em 1mA
    else:
        corrente = 0
    


if var == 1: 
    fun1 = 

#dados para plotar gráfico
t = np.arange(0.0, 10.0, 0.01) #vai de 0 a 10, intervalo de 0.01
s = 1 + np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t,s)
plt.show
