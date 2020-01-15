# -*- coding: utf-8 -*-

class Base(object):
    name = 'Base'
    def __init__(self, *args, **kwargs):
        print(args, kwargs)

class Foo(Base):
    name = 'Foo'
    def __init__(self, *args, **kwargs):
        # super(Foo, self, )
        pass

    def get(self):
        print(isinstance(self, Foo))
        print(isinstance(self, Base))

if __name__ == '__main__':
    Foo().get()
