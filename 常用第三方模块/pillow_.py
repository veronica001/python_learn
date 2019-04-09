#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。
此外，在安装第三方模块一节中，我们强烈推荐安装Anaconda，安装后，数十个常用的第三方模块就已经就绪，不用pip手动安装。
'''
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('../img/test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')
# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。

def rndchar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width , height), (255,255,255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)

# 填充每个像素:
for i in range(width):
    for j in range(height):
        draw.point((i,j),fill = rndColor())

# 输出文字:
for x in range(4):
    draw.text((x * 60 + 10, 10), rndchar(), font = font, fill=rndColor2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')