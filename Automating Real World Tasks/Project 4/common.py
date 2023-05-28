#!/usr/bin/env python3

from os import listdir
from os.path import join, isfile
from PIL import Image
import os

def list_files(dirpath, file_extn):
    files = [f for f in listdir(dirpath) if isfile(join(dirpath, f)) and f.endswith(file_extn)]
    
    for idx, f in enumerate(files):
        files[idx] = join(dirpath, f)
    
    return files

def modify_and_save(infile, out_format, outdir, *size):
    filepath, extn = os.path.splitext(infile)
    d, f = os.path.split(filepath)
            
    outfile = join(outdir, f)
    
    if infile != outfile:
        try:
            with Image.open(infile).convert("RGB") as im:
                im.thumbnail(size)
                im.save(outfile + "." + out_format, out_format)
                print("converted file: {}".format(outfile))
        except Exception as e:
            raise Exception("cannnot convert {}, Exception: {}".format(infile, e))

def read_description(filename):
    field_titles = ["name", "weight", "description", "image_name"]
    field_values = []
    
    try:
        #open each file to read contents
        with open(filename, "r") as f:
           #traverse each line in the file and add to string with comma(,) separator
            for line in f:
                if line.strip(): #non-empty lines
                    field_values.append(line.strip())
    
    except Exception as e:
        raise Exception(e)                

    # add image name or the file name
    d, f = os.path.split(filename)
    field_values.append(f.replace("txt", "jpeg"))
        
    #combining keys and values to form dictionary and return to the caller
    return dict(zip(field_titles, field_values))