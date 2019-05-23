# -*- coding: utf-8 -*-
class ndict(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

a = dict(name='wiz')
b = ndict(name='wiz')
pass