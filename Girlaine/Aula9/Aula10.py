

import numpy as np

palette =  np.array([[0, 0, 0], #Preto
                    [255, 0, 0], #Vermelho
                    [0, 255, 0], #Verde
                    [0, 0, 255], #Azul
                    [255, 255, 255]]) #branco

    image = np.array([[0,1,2,0], [0,3,4,0]])
    print(palette[image])

    import numpy as np
    a = np.arange(12)
    print(a)
    i = np.array([0,1],
                [1,2]])
    j = np.array([2,1],
                [3,3])
print(a[i,j])

print(a[i,2])
print(a[2,j])
print(a[:,j])
print(a[i,:])

import numpy as np
a = np.arange(12).reshape(3,4)
b = a > 4
print(b)
print(a[b])
print(a[a > 4])

b1 = np.arrey([False, True,True])
b2 = np.array([True,False,True,False])
print(a[b1,b2])

print(np.linalg.inv(a))
print(np.trace(a))
y = np.array([[5.],[7.]])
print(np.linal.solve(a,y))
print(np.linalg.eig(a))
print(np.linalg. )

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2 * np.pi *t)

def  plot(x,y)
fig, ax = plt 

fig,ax = plt.subplots ()
ax.plot(t,s)
plt.show()

Import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,2 * np.pi, 100)
figg,axs = plt.subplots(2,2)

axs[0,0].plot(3 * np. cos(a))
axs [0,0].set_title('not equal, parece uma elipse', fontsize = 10)

axs[0,1].plot(3* np.cos(a))
axs[0,1].set.axis('igual')
axs [0,0].set_title('circulo', fontsize = 10)

axs[0,0].plot(3* np.cos(a), 3* np.sin(a))
axs[0,1].set_title('circulo', fontsize = 10)


