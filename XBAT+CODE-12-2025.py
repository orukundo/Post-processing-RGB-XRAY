# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 07:45:06 2025

Pads non-square images to square shape (white for RGB, black for non-RGB),
then resizes to a defined size (e.g., 640 x 640) and saves both padded and resized versions
to separate folders.

@author: Olivier.Rukundo
University of Limerick
"""

import os
from PIL import Image

folder = r"your/input/folder/path"
format_map = {'.jpg': 'JPEG', '.bmp': 'BMP'}
target_size = (640, 640)

padded_folder = folder + "-PADDED"
resized_folder = folder + "-RESIZED"
os.makedirs(padded_folder, exist_ok=True)
os.makedirs(resized_folder, exist_ok=True)

for filename in os.listdir(folder):
    if filename.lower().endswith(tuple(format_map.keys())):
        path = os.path.join(folder, filename)
        img = Image.open(path)
        width, height = img.size
        ext = os.path.splitext(filename)[1].lower()
        save_format = format_map[ext]

        if width != height:
            max_dim = max(width, height)
            if img.mode == "RGB":
                padded_img = Image.new("RGB", (max_dim, max_dim), color=(255, 255, 255))
            else:
                padded_img = Image.new("L", (max_dim, max_dim), color=0)
                img = img.convert("L")
            x_offset = (max_dim - width) // 2
            y_offset = (max_dim - height) // 2
            padded_img.paste(img, (x_offset, y_offset))
        else:
            padded_img = img

        padded_img.save(os.path.join(padded_folder, filename), format=save_format)

        resized_img = padded_img.resize(target_size, resample=Image.LANCZOS)
        resized_img.save(os.path.join(resized_folder, filename), format=save_format)

