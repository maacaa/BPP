# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:55:28 2022

"""
import math

def binomio_cuadrado (a,b,c, raiz):
    raiz = math.sqrt(b**2 -4*a*c)
    
    if raiz > 0 :
        resultado1 = (-b + raiz)/2
        resultado2 = (-b - raiz)/2
        
        return (resultado1, resultado2)
   
    elif raiz == 0:
        return  -b/2
    
    else : 
        resultado =  'None'
        return resultado

