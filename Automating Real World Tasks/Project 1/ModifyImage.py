#!/usr/bin/env python3

import os
from os import listdir
from os.path import join, isfile
from PIL import Image

def list_image_files(dirpath, extension):
    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f)) and f.lower().endswith(extension)]
    return files

def modify_and_save(infile):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    size = (128, 128)
    
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.rotate(90)
                im.thumbnail(size)
                im.save(outfile)
        except:
            print("cannnot convert {}".format(infile))

def main():
    files = list_image_files(".", ".jpeg")
    
    for f in files:
        modify_and_save(f)

if __name__ == "__main__":
    main()
