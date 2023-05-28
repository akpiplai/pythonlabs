#!/usr/bin/env python3

import os
from os import listdir
from os.path import join, isfile
from PIL import Image

def list_image_files(dirpath):
    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    return files

def modify_and_save(infile):
    f, e = os.path.splitext(infile)
    outfile = "/opt/icons/" + f
    size = (128, 128)
    
    if infile != outfile:
        try:
            with Image.open("images/" + infile).convert("RGB") as im:
                im.rotate(90)
                im.thumbnail(size)
                im.save(outfile, "jpeg")
                print("converted file: {}".format(outfile))
        except Exception as e:
            print(e)
            print("cannnot convert {}".format("images/" + infile))

def main():
    files = list_image_files("images")
    
    print()
    print(files)
    print()
    
    for f in files:
        modify_and_save(f)
        #break

if __name__ == "__main__":
    main()