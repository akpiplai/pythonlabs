#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool

def run(src):
    print("syncing from {} to {}".format(src, src.replace("TestSrc", "TestDest")))
    subprocess.call(["rsync", "-zrvh", src, src.replace("TestSrc", "TestDest")])
    
if __name__ == "__main__":
    srcpaths = []
        
    for dirpath, dirnames, filenames in os.walk("TestSrc"):
        for name in filenames:
            srcpaths.append(os.path.join(dirpath, name))
    
    p = Pool(len(srcpaths))
    
    p.map(run, srcpaths)
    
    
        
        
    

