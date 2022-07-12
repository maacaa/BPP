# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:48:36 2022

"""

import actividad_2
import unittest

class PruebasUnitarias (unittest.TestCase):
    def test_raiz(self):
        self.assertEqual(actividad_2.binomio_cuadrado(4, 16, 7, 144), -2)
    
    def test_if1(self):
        self.assertisNone(actividad_2.binomio_cuadrado(4, 2, 4, -1), 'None')
        
    def test_if2(self):
        self.assertTrue(actividad_2.binomio_cuadrado(2,16,2,0),-8)
        
    def test_if3(self):
        self.assertEqual(actividad_2.binomio_cuadrado(4, 16, 7, 144), -2,-14)
