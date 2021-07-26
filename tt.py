# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:56:42 2021

@author: 82109
"""
from fp_growth import find_frequent_itemsets

if __name__ == '__main__':
    a= find_frequent_itemsets('examples/tsk.csv', 2)
    print(a)