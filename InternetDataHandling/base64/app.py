# -*- coding: utf-8 -*-
import base64, os

def get_ext(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension

def get_filename(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return filename

def detect_newname(filepath, index=1):
    filename, file_extension = os.path.splitext(filepath)
    new_path = filename + '_' + str(index) + file_extension
    if os.path.exists(new_path):
        return detect_newname(filepath, index + 1)
    return new_path

def new_filename(filepath, index=1):
    if os.path.exists(filepath):
        return detect_newname(filepath)
    return filepath

def write2file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def readfile(filename):
    with open(filename, 'rb') as f:
        return f.read()

def img2base64(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        bs2 = base64.b64decode(data)
        write2file(data.encode('base64'), 'bs2.txt')

def base642img(data, filename):
    with open(filename, 'wb') as f:
        f.write(data.decode('base64'))

if __name__ == '__main__':
    base642img(readfile('bs2.txt'), new_filename('IU.jpg'))