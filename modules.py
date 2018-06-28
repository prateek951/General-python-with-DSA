"""
Modules are pieces of code that other people have written
to fulfill common tasks such as generating random numbers
performing mathematical operations etc.

First step import module name at top of your code
and then using the module name and the dot notation
you can use the methods and values provided by the module.

"""

import random

for i in range(5):
    value = random.randint(1,6)
    print(value)

"""
There is another kind of import that can be used if you need
only certain functions from  a module

from modulename import var

then var can be used anywhere in the code as if it was
defined normally in the code.

"""

from math import pi
print(pi)

# Trying to import a module that is not there causes
# the ImportError


"""
3 main types of modules in Python those you write yourself,
those you install from external sources, and those
that are preinstalled with Python.

Last type is called standard library and contains many useful
modules include string,re,datetime,math,random,os,multiprocessing,
subprocess,socket,email,json,doctest,unittest,pdb,argparse and sys


"""

