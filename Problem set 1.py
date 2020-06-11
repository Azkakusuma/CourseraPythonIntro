#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:02:30 2020

@author: azkakusumaedy
"""


#%%
def problem1_1():
   print("Problem Set 1")

    
#%%
#%%
def problem1_2(x,y):
    sum = x+y
    product = x*y
    print(sum)
    print(product)
    


#%% 
#%%
def problem1_3(n):
   my_sum = 0
   for i in range(1, n+1):
       my_sum += i
       
   print(my_sum)


    

#%%
#%%
def problem1_4(miles):
    feet = 5280*miles
    print("There are",feet ,"in", miles,"miles.")


    
#%%
#%%
def problem1_5(age):
    if age < 7:
        print ("Have a glass of milk.")
    elif age < 21:
        print ("Have a coke.")
    else:
        print ("Have a martini.")
   



    
#%%
#%%
def problem1_6():
    for i in range(1, 101, 2):
        print(i,end=" ")


    
#%% 
#%%
def problem1_7():
   b1 = float(input("Enter the length of one of the bases: "))
   b2 = float(input("Enter the length of the other base: "))
   h = float(input("Enter the height: "))
   
   formula = .5*(b1+b2)*h
   
   print("The area of a trapezoid with bases",b1, "and",b2, "and height",h, "is",formula)








#%%