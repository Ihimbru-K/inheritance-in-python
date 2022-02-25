# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:54:51 2022

@author: mon pc
"""


#hierarchical inheritance: a parent class is inherited by multiple classes; here the 2 childclasses
class ParentClass:
    def feature1(self):
        print("feature1 is from the ParentClass")
class ChildClass1(ParentClass):
    def feature2(self):
        print("feature2 is from ChildClass1")
class ChildClass2(ParentClass):
    def feature3(self):
        print("feature3 is from ChildClass2")

obj1 = ChildClass2()
obj1.feature1()

obj2 = ChildClass1()
obj1.feature1()
