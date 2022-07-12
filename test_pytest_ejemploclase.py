# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 19:45:46 2022

@author: Usuario
"""
#Misma ubicación
import pytest
import operaciones

def test_suma ():
   
    x= 4
    y=5
    
    resultado = 9
    assert resultado == operaciones.suma(x, y)


def test_resta():
    
    x= 10
    y=5
    
    resultado = 5
    assert resultado == operaciones.resta(x, y)
    
    
def test_mult():
    
    x= 2
    y = 5
    
    resultado = 10
    assert resultado == operaciones.multiplicacion(x, y)


def test_div():
    
    x= 100
    y=2
    
    resultado = 50
    assert resultado == operaciones.division(x, y)
    
    
