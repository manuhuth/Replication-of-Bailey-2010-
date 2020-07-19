# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 09:55:00 2020

@author: Mhuth
"""




from causalgraphicalmodels import CausalGraphicalModel

nod = ['region', 'oral', 'sales bans', 'time', 'ideas about children', 'controls']

ed = [('region', 'oral'),
      ('region', 'sales bans'),
      ('region', 'ideas about children'),
      ('sales bans', 'oral'),
      ('time', 'oral'),
      ('time', 'ideas about children'),
      ('time', 'controls'),
      ('ideas about children', 'oral')
      ]
cg1 = CausalGraphicalModel(nodes = nod,edges = ed)

cg1.draw()