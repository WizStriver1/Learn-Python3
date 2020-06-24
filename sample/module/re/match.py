# -*- coding: utf-8 -*-
import re

line = 'a    /cloudlearn_hnlgdx / DB f'

matchObj = re.match(r'(.*)(cloudlearn_[^\s]*)(.*)', line, re.M|re.I)

if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
    print(matchObj.group(3))

else:
    print('No match!')

print(re.M|re.I)
print(10|3)