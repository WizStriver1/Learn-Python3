# -*- coding: utf-8 -*-
class A(object):

    def __init__(self):
        self.name = 'A'

    def fun(self):
        print("I'm fun, my name is:" + self.name)

    @classmethod
    def fun2(cls):
        print("I'm fun2, my name is:" + cls().name)

A.fun2()