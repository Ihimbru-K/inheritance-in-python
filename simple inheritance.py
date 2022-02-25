# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:42:42 2022

@author: mon pc
"""
#example of simple inheritance 
class ParentClass:
    def feature_1(self):
        print("feature 1 from parent class is running")
    def feature_2(self):
        print("feature 2 from parent class is running")
        
class ChildClass(ParentClass):  #syntax of child class derivation from parent class
        def feature_3(self):
            print("feature 3 from child class is running")
            
obj = ChildClass()
obj.feature_1()
obj.feature_2()
obj.feature_3()
        