#!/usr/bin/env python3
from PIL import Image
import os


def get_images(path):
    return [img for img in os.listdir(path) if 'ic' in img]


def fix_image(filename, dir):
    dest_dir = './output/images'
    new_image = Image.open(os.path.join(dir, filename)).convert('RGB')
    new_image = new_image.rotate(270).resize((128, 128))
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    return new_image.save(os.path.join(dest_dir, filename), 'JPEG')


def run():
    images = get_images('./images')
    for img in images:
        fix_image(img, './images')

    print("OK. All images were fixed.")

    
if __name__ == '__main__':
    run()