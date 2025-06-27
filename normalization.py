import os
import sys
import config

def data_normalization(line_data):

    # Read normalization symbols from config file
    #config.read_config()
    # Remove currency symbols '$' and ',' in line datas
    replace = False
    data_normal = ''
    for char in line_data:
        if char == config.symbol1_normal:
            replace = True
            char = ""
            data_normal = data_normal + char
        else:
            if replace == True:
                if char == config.symbol2_normal:
                    char = ""
                    replace = False
                if char == "\n":
                    replace = False
            data_normal = data_normal + char
    return data_normal


