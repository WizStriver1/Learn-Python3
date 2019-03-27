#!/usr/env python3
# -*- coding: utf-8 -*-
'''
恭喜你,获得
Lv3考证资格
申请考证试链接：
97.93.37.37:9000
############
姓名，性别，身份证号，受聘的燃气经营企业名称，人员类别，恭喜你，通过，考试，证书编号，发证部门
'''


from PIL import Image, ImageDraw, ImageFont
import textwrap
import glob, os

# img = Image.open('uploads/test_bg.png')
# img.show()

# img = Image.open('uploads/test_bg.png')
#
# draw = ImageDraw.Draw(img)
# draw.line((-100, 0) + img.size, fill=0)
# draw.line((0, img.size[1], img.size[0], 0), fill=128)
#
# img.show()

# Draw Partial Opacity Text
# base = Image.open('uploads/test_bg.png').convert('RGBA')
# txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
#
# fnt = ImageFont.truetype('uploads/Edmunds Distressed.ttf', 40)
#
# d = ImageDraw.Draw(txt)
#
# d.text((10, 10), "Hello", font=fnt, fill=(255, 0, 0, 3000))
#
# d.text((10, 60), 'World', font=fnt, fill=(0, 255, 0, 255))
#
# out = Image.alpha_composite(base, txt)
#
# out.show()
def draw_text(draw, content, position=(0, 0), fnt='font/microsoftyahei.ttf', fill=(0, 0, 0, 0)):
    draw.text(position, content, font=fnt, fill=fill)

def draw_line(draw, msg, position=(0, 0), fnt='font/microsoftyahei.ttf', fill=(0, 0, 0, 0)):
    x, y = position
    w, h = draw.textsize(msg, font=fnt)
    draw.line((x, y + h, x + w, y + h), fill=fill)

base = Image.open('uploads/certificate_bg.png').convert('RGBA')
stamp = Image.open('uploads/zhang_icon.png').convert('RGBA')
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

d = ImageDraw.Draw(txt)

# for content in certif_content:
    # draw_certif_text(base, unicode(content['msg'], 'utf-8'), content['font_type'], content['font_size'], content['fill_color'], content['draw_height'])

# out = Image.alpha_composite(base, txt)

# out.show()

certif_content = [
    {
        'msg': '        姓 名 ：'
    },
    {
        'msg': '纳兰嫣然',
        'underline': True
    },
    {
        'msg': ' ，性 别 ：'
    },
    {
        'msg': '女',
        'underline': True
    },
    {
        'msg': ' ，身 份 证 号 ：'
    },
    {
        'msg': '849******3424',
        'underline': True
    },
    {
        'msg': ' ，受聘的燃气经营企业名称 ：'
    },
    {
        'msg': '云岚宗高级炼药师协会',
        'underline': True
    },
    {
        'msg': ' ，人员类别 ：'
    },
    {
        'msg': '超超炼药宗师',
        'underline': True
    },
    {
        'msg': ' 。'
    },
    {
        'msg': '        恭喜你，通过 ',
        'word_wrap': True
    },
    {
        'msg': '超超炼药宗师',
        'underline': True,
        'font_size': 24,
        'fill_color': (77, 73, 44)
    },
    {
        'msg': ' 考试，证书编号：'
    },
    {
        'msg': 'SUPER000000',
        'underline': True
    },
    {
        'msg': ' 。'
    },
    {
        'msg': '发证部门',
        'position': (365, 288)
    },
    {
        'msg': '2019年03月25日',
        'position': (340, 316)
    }
]

font_type = 'font/fzdbsjw.ttf'
default_font_size = 16
line_height = 32
default_fill_color = (114, 104, 92)
origin_draw_width = 47
draw_width = origin_draw_width
draw_height = 85
text_range = 403
surplus_range = text_range

def get_font_size(content):
    if 'font_size' in content:
        return content['font_size']
    else:
        return default_font_size

def get_fill_color(content):
    if 'fill_color' in content:
        return content['fill_color']
    else:
        return default_fill_color

def get_position(content, font_size):
    if 'position' in content:
        return content['position']
    elif font_size != default_font_size:
        return (draw_width, draw_height + default_font_size - font_size)
    else:
        return (draw_width, draw_height)

def word_wrap(content):
    global draw_height, draw_width, surplus_range

    if 'word_wrap' in content:
        del content['word_wrap']

    draw_height += line_height
    draw_width = origin_draw_width
    surplus_range = text_range

def move_cursor(width):
    global draw_width, surplus_range

    surplus_range = surplus_range - width
    draw_width += width

def to_draw_text(content, msg, position, fnt, fill_color):
    w, h = d.textsize(msg, font=fnt)
    draw_text(d, msg, position, fnt, fill_color)
    if 'underline' in content and content['underline']:
        draw_line(d, msg, position, fnt, fill_color)
    move_cursor(w)

def get_former_msg(content, fnt):
    former_msg = str()
    msg = content['msg']
    for s in msg:
        w, h = d.textsize(former_msg + s, font=fnt)
        if w > surplus_range:
            content['msg'] = msg[msg.index(s):]
            content['word_wrap'] = True
            break
        former_msg += s
    return former_msg

def convert2unicode(content):
    if isinstance(content['msg'], str):
        content['msg'] = content['msg'].decode('utf-8')
    return content['msg']

def draw_certif_text(content):

    if 'word_wrap' in content:
        word_wrap(content)

    font_size = get_font_size(content)
    fill_color = get_fill_color(content)
    position = get_position(content, font_size)
    msg = convert2unicode(content)
    fnt = ImageFont.truetype(font_type, font_size)

    w, h = d.textsize(msg, font=fnt)

    if w < surplus_range or 'position' in content:
        to_draw_text(content, msg, position, fnt, fill_color)
    else:
        to_draw_text(content, get_former_msg(content, fnt), position, fnt, fill_color)
        draw_certif_text(content)

for content in certif_content:
    draw_certif_text(content)

out = Image.alpha_composite(base, txt)
out.paste(stamp, (350, 235), stamp)

out.save('test.png', 'png')