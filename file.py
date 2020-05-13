#!/usr/bin/env python
import os
import subprocess

PWD = os.getcwd()
my_file = os.path.join(PWD, 'data.txt')

with open(my_file) as f:
    for line in f:
        print(line)
