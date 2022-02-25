# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:35:05 2022

@author: mon pc
"""

#example of multilevel inheritance
class ParentClass:
    def feature1(self):
        print("feature 1 from ParentClass")
class ChildClass1(ParentClass):
    def feature2(self):
        print("feature 2 from ChildClass1")
class ChildClass2(ChildClass1):
    def feature3(self):
        print("feature 3 from ChildClass2")
obj = ChildClass2()
obj.feature1()
obj.feature2()
obj.feature3()