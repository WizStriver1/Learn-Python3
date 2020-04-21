# -*- coding: utf-8 -*-
import base64
with open("IU.jpg","rb") as f:#转为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    file=open('b64.txt','wt')#写成文本格式
    file.write(base64_data)
    file.close()