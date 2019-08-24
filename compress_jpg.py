#!/usr/bin/env python

from PIL import Image
import os

def make_thumb(path, sizes=(75, 32, 16)):
    """
    缩略图生成程序 Zoe
    sizes 参数传递要生成的尺寸，可以生成多种尺寸
    """
    base, ext = os.path.splitext(path)
    try:
        im = Image.open(path)
    except IOError:
        return

    # jpg图片透明部分填充
    # mode = im.mode
    # if mode not in ('L', 'RGB'):
    #     if mode == 'RGBA':
    #         # 透明图片需要加白色底
    #         alpha = im.split()[3]
    #         bgmask = alpha.point(lambda x: 255 - x)
    #         im = im.convert('RGB')
    #         # paste(color, box, mask)
    #         im.paste((255, 255, 255), None, bgmask)
    #     else:
    #         im = im.convert('RGB')

    width, height = im.size
    if width == height:
        region = im
    else:
        if width > height:
            delta = (width - height) / 2
            box = (delta, 0, delta + height, height)
        else:
            delta = (height - width) / 2
            box = (0, delta, width, delta + width)
        region = im.crop(box)

    tail = path.split('.')[-1]
    for size in sizes:
        filename = base + "_" + "%sx%s" % (str(size), str(size)) + "." + tail
        thumb = region.resize((size, size), Image.ANTIALIAS)
        thumb.save(filename, quality=100)  # 默认保存质量是 75, 不太清楚。可选值(0~100)


def compressJpg(srcPath):
    for filename in os.listdir(srcPath):
        srcFile = os.path.join(srcPath, filename)

        if os.path.isfile(srcFile):
            make_thumb(srcFile)

        # 文件夹递归
        if os.path.isdir(srcFile):
            compressJpg(srcFile)

if __name__ == '__main__':
    compressJpg("./src")