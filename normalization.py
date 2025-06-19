import os
import sys

def data_normalization(line_data):

    # Remove currency symbols and ',' in line datas
    replace = False
    data_normal = ''
    for char in line_data:
        if char == "$":
            replace = True
            char = ""
            data_normal = data_normal + char
        else:
            if replace == True:
                if char == ",":
                    char = ""
                    replace = False
                if char == "\n":
                    replace = False
            data_normal = data_normal + char
    return data_normal


