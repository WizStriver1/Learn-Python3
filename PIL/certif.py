#!/usr/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import textwrap
import glob, os

def draw_text(draw, content, position=(0, 0), fnt='font/microsoftyahei.ttf', fill=(0, 0, 0, 0)):
    draw.text(position, content, font=fnt, fill=fill)

def draw_admit_text(base, draw, msg, font_type, font_size, fill_color, draw_height):
    fnt = ImageFont.truetype(font_type, font_size)
    w, h = draw.textsize(msg, font=fnt)
    draw_text(draw, msg, ((base.size[0]-w)/2, draw_height), fnt, fill_color)

base = Image.open('uploads/test_bg.png').convert('RGBA')
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

d = ImageDraw.Draw(txt)

admit_content = [
    {
        'font_type': 'font/microsoftyaheibold.ttf',
        'font_size': 16,
        'fill_color': (124, 179, 225),
        'draw_height': 203,
        'msg': '恭喜你,获得'
    },
    {
        'font_type': 'font/fzdbsjw.ttf',
        'font_size': 24,
        'fill_color': (86, 155, 213),
        'draw_height': 233,
        'msg': 'Lv3考证资格'
    },
    {
        'font_type': 'font/fzlthk.ttf',
        'font_size': 16,
        'fill_color': (86, 155, 213),
        'draw_height': 300,
        'msg': '申请考证试链接：'
    },
    {
        'font_type': 'font/fzlthk.ttf',
        'font_size': 18,
        'fill_color': (86, 155, 213),
        'draw_height': 325,
        'msg': '255.255.255.255:20000'
    }
]
for content in admit_content:
    draw_admit_text(base, d, unicode(content['msg'], 'utf-8'), content['font_type'], content['font_size'], content['fill_color'], content['draw_height'])

out = Image.alpha_composite(base, txt)

out.show()