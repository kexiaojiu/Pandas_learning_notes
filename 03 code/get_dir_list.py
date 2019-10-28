# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:33:15 2019

@author: kejie
"""

import os

path = "F:\Jupyter\\" + "01 pandas\\"

dir_list = os.listdir(path)
for file in dir_list:
    print(file)