# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:04:44 2020

@author: seidi
"""

# Criação de tuplas
tupla = (1,2,3,4)
print(tupla)

tupla(1,)
print(tupla)

tupla = ()
print(tupla)

# Acesso a elementos de tuplas
tupla = ('Maria', 'João', 'Carlos')
print(tupla[0])
print(tupla[0:2])
tupla[0] = 'Ana' # erro

# Fatiamento
p = 'python'
print(p[0:0]) # ''
print(p[0:1]) #'p'
print(p[1:2]) #'y'
print(p[2:3]) #'t'
print(p[3:4]) #'h'
print(p[4:5]) #'o'
print(p[5:6]) #'n'
print(p[6:6]) #''

print(p[:1])  #'p'
print(p[:2])  #'py'
print(p[:3])  #'pyt'
print(p[:4])  #'pyth'
print(p[:5])  #'pytho'
print(p[:6])  #'python'

print(p[0:1]) #'p'
print(p[0:2]) #'py'
print(p[0:3]) #'pyt'
print(p[0:4]) #'pyth'
print(p[0:5]) #'pytho'
print(p[0:6]) #'python'

print(p[:])   #'python'
print(p[1:])  #'ython'
print(p[2:])  #'thon'
print(p[3:])  #'hon'
print(p[4:])  #'on'
print(p[5:])  #'n'
print(p[5:])  #''
