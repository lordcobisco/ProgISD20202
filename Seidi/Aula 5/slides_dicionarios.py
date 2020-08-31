# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:11:48 2020

@author: seidi
"""
# Manipulação de Dicionários
agenda = {}
print(agenda)

agenda = {'Maria': [99887766, 99887755]}
print(agenda)

agenda = {'Maria': [99887766, 99887755], 'Pedro': [92345678], 'Joaquim':[99887711,99665533]}
print(agenda)

print(agenda['Maria'])

agenda['Perdo'] = [87654433]
print(agenda)

agenda = {}
print(agenda)
agenda['Teresa'] = [65443322]
print(agenda) 