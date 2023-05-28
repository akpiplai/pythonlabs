#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

dest = "data/prod_backup/"

def run(src):
  print ("syncing from {} to {}".format(src, dest))
  subprocess.call(["rsync", "-zrvh", src, dest])

if __name__ == "__main__":
  srcpaths = []

  for dirpath, dirnames, filenames in os.walk("data/prod/"):
    srcpaths.append(dirpath)

print(srcpaths)
p = Pool(len(srcpaths))

p.map(run, srcpaths)