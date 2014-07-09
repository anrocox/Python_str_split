#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

How to split a string by a specific character in python?

Como dividir un string por un caracter especifico en python?
'''

#create a str
s = 'blue,red,green,black,gray'
print(s)

#generates a list of the words contained in 's', using as the delimiter
#the ',' character.
l = s.split(',')
print(l)

#create a str
s = '  dog   cat   mouse  '
print(s)

#If a delimiter isn't defined, the whitespace are taken as delimiter
l = s.split()
print(l)

#create a str
s = 'milk-+-bread-+-meat-+-eggs'
print(s)

#the delimiter may consist of multiple characters
l = s.split('-+-')
print(l)

#create a str
s = 'blue, red, green, black, gray'
print(s)

#can define the number of occurrences to split.
l = s.split(', ', 2)
print(l)
