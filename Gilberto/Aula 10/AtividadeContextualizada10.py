#!/usr/bin/env python
# coding: utf-8

# # Atividade Contextualizada 10
# ### Autor: Gilberto Martins 
# #### E-mail: gilberto.filho@edu.isd.org.br

# Este código irá utilizar a biblioteca Pymatgen, uma bilbioteca voltada para análise dos materiais em sua totalidade (Estruturas, . Realizando a importação de arquivos e contendo bibliotecas como numpy, matplotlib, pandas, SciPy e entre outras.

# ### Importando o pymatgen 

# In[1]:


import pymatgen


# In[2]:


print(pymatgen.__version__)
print(pymatgen.__file__)


# In[3]:


import sys
print (sys.version)


# ### Trabalhando com moléculas

# In[4]:


from pymatgen import Molecule


# In[5]:


water = Molecule.from_file("water.xyz")
print(water)


# In[6]:


print(water[0])


# In[7]:


print(water[1])


# In[8]:


print(water[2])


# In[9]:


example = Molecule(["H","H"], [[0.0, 0.0, 0.0], [0.1,0.0,0.0]], validate_proximity=False)
example


# In[10]:


water.cart_coords


# ### Importando Elementos, Composição, Estrutura e Sistema Cristalino

# In[11]:


from pymatgen import Element, Specie, Composition
from pymatgen import Structure
from pymatgen import Lattice


# In[12]:


nacl = Structure.from_spacegroup("Fm-3m", Lattice.cubic(5.692), ["Na+", "Cl-"], [[0,0,0],[0.5,0.5,0.5]])


# In[13]:


print(nacl)


# ### Importando Estruturas de arquivos .CIF

# In[14]:


Cu = Structure.from_file("Cu.cif")


# In[15]:


from pymatgen.core.surface import SlabGenerator


# In[16]:


slabgen = SlabGenerator(Cu, (1, 1, 1), 10, 10)


# In[17]:


slabs = slabgen.get_slabs()


# In[18]:


print(len(slabs))


# In[19]:


Cu_111 = slabs[0]


# ### Verificando o Plano Gerado e a Estrutra

# In[20]:


Cu_111


# In[21]:


print(Cu_111.miller_index, Cu_111.shift)


# ### Gerando Imagem da Estrutura e do Plano

# In[22]:


from pymatgen.analysis.adsorption import plot_slab
from matplotlib import pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plot_slab(Cu_111, ax, adsorption_sites=False)
ax.set_title("Cu (1, 1, 1) surface")
ax.set_xticks([])
ax.set_yticks([])
plt.show()


# ### Verificando os locais de adsorção no plano e entre as camadas

# In[24]:


from pymatgen.analysis.adsorption import AdsorbateSiteFinder


# In[25]:


asf = AdsorbateSiteFinder(Cu_111)


# In[26]:


add_sites = asf.find_adsorption_sites()
add_sites


# In[27]:


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plot_slab(Cu_111, ax, adsorption_sites=True)
ax.set_title("Cu (1, 1, 1) adsorption points")
ax.set_xticks([])
ax.set_yticks([])
plt.show()


# ### Importar moléculas para colocar nos sítios de adsorção

# In[38]:


from pymatgen import Molecule


# In[39]:


adsorbate = Molecule("H", [[0,0,0]])


# In[40]:


ads_sructs = asf.generate_adsorption_structures(adsorbate, repeat=[1, 1, 1], 
find_args={"distance":1.6})


# In[41]:


fig = plt.figure(figsize=[15,60])
for n, ads_struct in enumerate(ads_sructs):
    ax = fig.add_subplot(1, 4, n+1)
    plot_slab(ads_struct, ax, adsorption_sites=False)
    ax.set_title(n+1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0.5)
    ax.set_ylim(-1,4)
plt.show()


# In[42]:


adsorbate_1 = Molecule("C", [[0,0,0]])


# In[43]:


ads_sructs = asf.generate_adsorption_structures(adsorbate_1, repeat=[1, 1, 1], 
find_args={"distance":1.6})


# In[44]:


fig = plt.figure(figsize=[15,60])
for n, ads_struct in enumerate(ads_sructs):
    ax = fig.add_subplot(1, 4, n+1)
    plot_slab(ads_struct, ax, adsorption_sites=False)
    ax.set_title(n+1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0.5)
    ax.set_ylim(-1,4)
plt.show()


# ### Verificar a possibilidade de adsorção do CO2

# In[45]:


CO2_x = Molecule(["O","C","O"],[[-1.16, 0, 0], [0, 0, 0], [1.16, 0, 0]])
CO2_y = Molecule(["O","C","O"],[[0, -1.16, 0], [0, 0, 0], [0, 1.16, 0]])
CO2_z = Molecule(["O","C","O"],[[0, 0, -1.16], [0, 0, 0], [0, 0, 1.16]])


# In[46]:


ads_sites = asf.find_adsorption_sites()
ads_coords = ads_sites['ontop'][0]


# In[47]:


x_struct = asf.add_adsorbate(CO2_x, ads_coords, repeat=[2, 2, 1])
y_struct = asf.add_adsorbate(CO2_y, ads_coords, repeat=[2, 2, 1])
z_struct = asf.add_adsorbate(CO2_z, ads_coords, repeat=[2, 2, 1])


# In[48]:


for struc, ax, title in zip([x_struct, y_struct, z_struct], plt.subplots(1, 3, figsize=[15, 45])[1], ["x", "y", "z"]):
    plot_slab(struc, ax, adsorption_sites=False)
    ax.set_title(r"CO$_2$ in the %s direction" % title)
    ax.set_xlim(-1, 10)
    ax.set_ylim(-3, 8)
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()


# In[50]:


ads_sites = asf.find_adsorption_sites()
ads_coords_1 = ads_sites['hollow'][0]


# In[52]:


x_struct = asf.add_adsorbate(CO2_x, ads_coords_1, repeat=[2, 2, 1])
y_struct = asf.add_adsorbate(CO2_y, ads_coords_1, repeat=[2, 2, 1])
z_struct = asf.add_adsorbate(CO2_z, ads_coords_1, repeat=[2, 2, 1])


# In[53]:


for struc, ax, title in zip([x_struct, y_struct, z_struct], plt.subplots(1, 3, figsize=[15, 45])[1], ["x", "y", "z"]):
    plot_slab(struc, ax, adsorption_sites=False)
    ax.set_title(r"CO$_2$ in the %s direction" % title)
    ax.set_xlim(-1, 10)
    ax.set_ylim(-3, 8)
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()


# ### Salvando arquivos em formato .CIF 

# In[54]:


x_struct.to(fmt="cif", filename="Cu_CO2_x.cif")
y_struct.to(fmt="cif", filename="Cu_CO2_y.cif")
z_struct.to(fmt="cif", filename="Cu_CO2_z.cif")


# In[ ]:




