#!/usr/bin/env python3
from PIL import Image

def create_new():
    im = Image.open('german-dog.jpg')
    new_im = im.resize((640,480))
    new_im.save('example_rezised.jpg')


def rotate():
    im = Image.open('example_rezised.jpg')
    new_im = im.rotate(90)
    new_im.save('example_rotated.jpg')


if __name__ == '__main__':
    create_new()
    rotate()