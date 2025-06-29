import os
import sys
import config

def data_normalization(line_data):

    # Read normalization symbols from config file and remove it for product amount and unit price
    #config.read_config()
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
