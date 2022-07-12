# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:18:23 2022

@author: Macarena Coloma
"""
#Definimos la clase
class Calculadora:  

  #Definimos constructor  
    def __init___(self, number1, number2):
        self.number1 = number1
        self.number2 = number2    
    #Definimos los atributos
    def suma (self):
        self.suma = self.number1 + self.number2
        print('La suma es ', self.suma)
        
    def resta (self):
         self.rest = self.number1 - self.number2
         print('La resta es ', self.resta)
     
    def multiplicacion (self):
        self.multiplication = self.number1*self.number2
        print('La multiplicacion es ', self.multiplication)
    
    def division (self):
        
        if self.number2!=0:
            try:
                self.divis = self.number1 / self.number2
                print('La division es ', self.divis)
            
            except:
                'Error tiene que ser distinto de cero'

#introducimos los numeros por teclado
num1= int(input('Introduce el primer numero: '))
num2= int(input('Introduce el segundo numero: '))
#Creamos el objeto
Calculadora1 = Calculadora(num1,num2)
#Asignamos los valores a las variables en funcion de la operacion
a= Calculadora.suma()
b= Calculadora.resta()
c= Calculadora.multiplicacion()
d= Calculadora.division()
     
#mostramos los resultados por pantalla
print ('Los resultados de la calculadora son: ')

print('Suma: ', a)
print('Resta: ',b)
print('Multiplicacion: ', c)
print('Division: ', d)