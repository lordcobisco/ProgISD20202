# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:33:52 2020

@author: seidi
"""

movies_dict = {}
movies_dict['Stanley Kubrick'] = ['2001: A Space Odissey', 'The Shining', 'A Clockwork Orange']
movies_dict['Akira Kurosawa'] = ['Ran', 'Seven Samurai', 'Yojimbo']
movies_dict['Andrei Tarkovski'] = ['Solaris', 'Nostalghia', 'Ivan"s Childhood']
movies_dict['François Truffaut'] = ['Les Quatre Cents Coups', 'Jules et Jim', 'Farenheit 451']


for director in movies_dict.keys():
  print(director)
  print(movies_dict[director])
  
  
  