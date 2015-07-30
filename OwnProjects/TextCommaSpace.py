'''
Created on Apr 27, 2015

@author: ninh
'''

string = input('Enter input:\n')

stringnew = string.replace(" ", ", ") and string.replace("  ", ", ")
print(stringnew)