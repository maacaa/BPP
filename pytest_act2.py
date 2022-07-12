# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:06:52 2022

"""
import pytest
import actividad_2

def test_raiz():
    
    a = 4
    b = 16
    c = 7
    
    raiz = 144
    assert raiz == actividad_2.binomio_cuadrado (a,b,c, raiz)
    
def test_if1():
    
    a = 4
    b = 2
    c = 4
    raiz = -1
    
    resultado = 'None'
    assert resultado == actividad_2.binomio_cuadrado (a,b,c, raiz)
    
def test_if2():
    
    raiz = 0
    a = 2
    b= 16
    c = 2
    
    resultado = -8
    assert resultado == actividad_2.binomio_cuadrado (a,b,c, raiz)
    
def test_if3():
    
    raiz = 16
    a= 1
    b= 6
    c= 5
    
    resultado1 = -1
    resultado2 = -10
    assert resultado1 == actividad_2.binomio_cuadrado (a,b,c, raiz)
    assert resultado2 == actividad_2.binomio_cuadrado (a,b,c, raiz)