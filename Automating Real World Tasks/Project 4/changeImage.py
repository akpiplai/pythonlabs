#!/usr/bin/env python3

import common
from os.path import join

def main():
    imagedir = "images"
    files = common.list_files(imagedir, "jpeg")
        
    for f in files:
        try:
            common.modify_and_save(f, "jpeg", "images", *(600, 400))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()