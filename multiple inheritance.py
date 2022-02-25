# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 23:12:12 2022

@author: mon pc
"""


#example of multiple inheritance
class ParentClass1:
    def feature1(self):
        print("feature 1 from ParentClass1 is running")
class ParentClass2:
    def feature2(self):
        print("feature 2 from ParentClass2 is running")
class ChildClass(ParentClass1, ParentClass2):
    def feature3(self):
        print("feature 3 from ChildClass is running")


obj = ChildClass()
obj.feature1()
obj.feature2()
obj.feature3()