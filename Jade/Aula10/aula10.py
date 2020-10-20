import matplotlib
import matplotlib.pyplot as plt
import numpy as np
'''
t= np.arange(0.0, 2.0, 0.01)
s= 1 + np.sin(2 * np.pi * t)

fig,ax= plt.subplots()
ax.plot(t,s)
plt.show()

# Plot circle of radius 3.

an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)

axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)

axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)

axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('circulo auto ajustado aos limites', fontsize=10)

fig.tight_layout()

plt.show()


N=5
menMeans= (20, 35, 30, 35, 27)
womenMeans= (25,32,34,20,25)
menStd= (2,3,4,1,2)
womenStd= (3,4,2,3,3)

ind= np.arange(N)
width= 0.35
p1=plt.bar(ind, menMeans, width, yerr= menStd)
p2=plt.bar(ind, womenMeans, width, bottom= menMeans, yerr= womenStd)
plt.ylabel('Scores')
plt.title('Scores por grupo e idade')
plt.xticks(ind, ('G1', 'G2','G3', 'G4', 'G5'))
plt.yticks(np.arange(0,81,10))
plt.legend((p1[0],p2[0]),('Men', 'Women'))

plt.show()
'''

np.random.seed(1968081)
all_data= [np.random.normal(0,std,size=100) for std in range(1,4)]
print(all_data)

labels= ['x1', 'x2', 'x3']

fig,ax= plt.subplots(nrows=1, ncols=1,figsize=(9,4))

bplot= ax.boxplot(all_data, vert = True, patch_artist = True, labels= labels)

ax.set_title('Box plot retangular')

colors =['pink', 'lightblue', 'lightgreen']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

ax.yaxis.grid(True)
ax.set_xlabel('qqr coisa')
ax.set_ylabel('sei la')

plt.show()
