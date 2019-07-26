# __all__作用

__all__的一般是一个list，用来定义模块中对于from xxx import * 的情况，即要暴露的接口，但它只对import * 起作用，对 from xxx import xxx 不起作用
