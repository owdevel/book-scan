#!/usr/bin/python

import os # Path stuff
from shutil import copyfile # Copy files


# Config
INPUTPATH = './src'
OUTPUTPATH = './input'
LEFTDIR = 'left'
RIGHTDIR = 'right'
FRONT = 'front'
BACK = 'back'
EXT = '.jpg'

LEFT_REVERSE = False
RIGHT_REVERSE = True

leftpath = os.path.join(INPUTPATH, LEFTDIR)
rightpath = os.path.join(INPUTPATH, RIGHTDIR)

# Get left and right files in order
left = sorted([image for image in (os.listdir(leftpath))], reverse = LEFT_REVERSE)
right = sorted([image for image in (os.listdir(rightpath))], reverse = RIGHT_REVERSE)

# Get front and back cover files
for file in os.listdir(INPUTPATH):
    name = os.path.splitext(file)[0]
    if name == FRONT:
        frontpath = file
    elif name == BACK:
        backpath = file


# Assertions
assert(len(left) == len(right), "Left and Right folders are not of equal length")
assert(frontpath != None, "Front cover not found")
assert(backpath != None, "Back cover not found")


# Begin renaming
count = 0

# Front Cover
copyfile(os.path.join(INPUTPATH, frontpath),  os.path.join(OUTPUTPATH, f'{count:03}' + EXT))
count = count + 1

# Pages
for i in range(0, len(left)):
    copyfile(os.path.join(leftpath, left[i]), os.path.join(OUTPUTPATH, f'{count:03}' + EXT))
    count = count + 1
    copyfile(os.path.join(rightpath, right[i]), os.path.join(OUTPUTPATH, f'{count:03}' + EXT))
    count = count + 1

# Back Cover
copyfile(os.path.join(INPUTPATH, backpath),  os.path.join(OUTPUTPATH, f'{count:03}' + EXT))
