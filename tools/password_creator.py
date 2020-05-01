# -*- coding: utf-8 -*-
# 密码生成器
import string, random

length = 10

signs = '@~_'

psw_list = []

psw_list.append(str([ random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.randint(0,9), random.choice(signs)][0]))

psw_list.append(str([ random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.randint(0,9), random.choice(signs)][1]))

psw_list.append(str([ random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.randint(0,9), random.choice(signs)][2]))

psw_list.append(str([ random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.randint(0,9), random.choice(signs)][3]))

psw_list += [str([ random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase), random.randint(0,9), random.choice(signs)][random.randint(0, 2)]) for i in range(length - 3)]

random.shuffle(psw_list)

print(''.join(psw_list))