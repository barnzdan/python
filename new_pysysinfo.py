#!/usr/bin/env python

# short script that uses code from pysysinfo.py

from pysysinfo import diskspacer
import subprocess

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print "\nSpace used in /tmp directory"
    subprocess.call([tmp_usage, tmp_arg, path])

def main():
    diskspacer()
    tmp_space()

if __name__ == "__main__":
    main()
