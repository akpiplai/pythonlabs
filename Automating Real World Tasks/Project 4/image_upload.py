#! /usr/bin/env python3

import common
import requests

url = "http://localhost/upload/"

def main():

    files = common.list_files("images", "jpeg")
    
    for f in files:
        try:
            with open(f, "rb") as opened:
                r = requests.post(url, files = {'file' : opened})
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    main()    

