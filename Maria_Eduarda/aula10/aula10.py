
"""import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colorbar
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.animation as animation

a=np.arange(12)**2
print(a)
j=np.array([[3,4],[9,7]])#selecionar vetores específicos
print(a[j])
pallete=np.array([[0,0,0],
                [255,0,0],[0,255,0],[0,0,255],[255,255,255]])
image=np.array([0,1,2,0],[0,3,4,0])
a=np.arange(12).reshape(3,4)
print(a)
i=np.array([[0,1],[1,2]])
j=np.array([[2,1],[3,3]])
print(a[i,j])
print(a[i,2])
print(a[2,j])
print(a[:,j])
print(a[i,:])
a=np.arange(12).reshape(3,4)
b=a>4
print(b)
print(a[b])#Pega as posições true
b1=np.array([False,True,True])
b2=np.array([True,False,True,False])
print(a[b1,b2])
print(a[:,b2])
print(a[b1,:])

## Álgebra Linear ##
a=np.array([[1.0,2.0],[3.0,4.0]])
y=np.array([[1.0,2.0],[3.0,4.0]])
print(a.transpose())#transposta
print(np.linalg.inv(a))#inversa
print(np.trace(a))#traço
print(np.linalg.solve(a,y))#linaer
print(np.linalg.eig(a))#autovalores"""

#1 grpafico
"""def plot (x,y):
    fig,ax=plt.subplots()
    ax.plot(x,y)
    plt.show()
t=np.arange(0.0,2.0,0.01)
s=1+np.sin(2*np.pi*t)
#plot(t,s)

#Multiplos gráficos
a=np.linspace(0,2*np.pi,100)
fig,axs=plt.subplots(2,2)#cada linha plotar um gráfico ou seja 4 gráficos
axs[0,0].plot(3*np.cos(a), 3*np.sin(a))
axs[0,0].set_title('Not equal, parece uma elipse',fontsize=10)
axs[0,0].axis('equal')
axs[0,1].plot(3*np.cos(a), 3*np.sin(a))
axs[0,1].set_title('circulo',fontsize=10)
axs[0,1].set_aspect('equal')
axs[1,0].plot(3*np.cos(a), 3*np.sin(a))
axs[1,0].set(xlim=(-3,3),ylim=(-3,3))
axs[1,0].set_title('limites de visualização',fontsize=10)
axs[1,0].set_aspect('equal','box')
axs[1,1].plot(3*np.cos(a), 3*np.sin(a))
axs[1,1].set(xlim=(-3,3),ylim=(-3,3))
axs[1,1].set_title('limites de visualização',fontsize=10)
axs[1,1].set_aspect('equal','box')

fig.tight_layout()
plt.show()
N=5
menMeans=(24,26,28,35,40)
womenMeans=(21,23,24,26,25)
menstd=(2,3,4,1,2)
womenstd=(3,5,2,3,3)
ind=np.arange(N) #The x locations for the groups
width=0.35
p1=plt.bar(ind,menMeans,width,yerr=menstd)
p2=plt.bar(ind,womenMeans,width,bottom=menMeans,yerr=womenstd)

plt.ylabel('scores')
plt.title('Scores by group and gender')
plt.xticks(ind,('G1','G2','G3','G4','G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]),('Men','women'))
plt.show()

#Pizza
labels='Frogs','Hogs','Dogs','Logs'
sizes=[15,30,45,10]
explode=(0,0.1,0,0)#Sair um pouco do gráfico
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

#Boxplott
np.random.seed(19680801)
all_data=[np.random.normal(0,size=100) for std in range(1,4)]
print(all_data)

labels=['x1','x2','x3']
fig,ax=plt.subplots(nrows=1,ncols=1,figsize=(9,4))
bplot=ax.boxplot(all_data,vert=True,patch_artist=True,labels=labels)
ax.set_title('Box plot')
colors=['pink','lightblue','green']
for patch, color in zip(bplot['boxes'],colors):
    patch.set_facecolor(color)

ax.yaxis.grid(True)
ax.set_xlabel('deffrfg')
ax.set_ylabel('dfhjukilmk')
plt.show()

#Histograma
np.random.seed(19680801)
N_points=100000
n_bins=20
x=np.random.randn(N_points)
fig, axs=plt.subplots(1,1,sharey=True,tight_layout=True)
axs.hist(x,bins=n_bins)
plt.show()
#Gráfico 3D

fig=plt.figure()
ax=fig.gca(projection='3d')
colors=('r','g','b','k')
np.random.seed(19680801)
x=np.random.sample(20*len(colors))
y=np.random.sample(20*len(colors))
z=np.random.sample(20*len(colors))
c_list=[]
for c in colors:
    c_list.extend([c]*20)
ax.scatter(x,y,z,c=c_list,label='points')
ax.view_init(elev=20,azim=-35)
plt.show()
#Color Map
fig=plt.figure()
ax=fig.gca(projection='3d')
x=np.arange(-5,5,0.25)
y=np.arange(-5,5,0.25)
x,y=np.meshgrid(x,y)
R=np.sqrt(x**2 + y**2)
z=np.sin(R)
surf=ax.plot_surface(x,y,z,cmap=cm.coolwarm, linewidth=0,antialiased=False)
plt.show()"""

#Animação

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig,ax = plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def init():
    line.set_ydata([np.nan]*len(x))
    return line,
def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, interval = 2, 
                            blit = True, save_count=50)
plt.show()

from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=15, metadata=dict(artist='ME'), bitrate=1800)
ani.save('D:\\movie.mp4',writer =writer)