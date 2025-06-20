import configparser
import os

def read_config():
    config_file = "config.ini"
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        config.read(config_file)
        global output_dir
        global log_file_dir
        global output_header_csv
        global output_line_csv
        global keyword_date
        global keyword_line
        global keyword_ship
        global keyword_terms
        global keyword_shipvia
        global symbol1_normal
        global symbol2_normal
        global key_valid
        global key_total
        
        output_dir = config['DEFAULT']['output_directory']
        is_valid(output_dir)
        log_file_dir = config['DEFAULT']['log_file_path']
        is_valid(log_file_dir)
        output_header_csv = config['DEFAULT']['output_file_header_csv']
        output_line_csv = config['DEFAULT']['output_file_line_csv']

        keyword_date = config['HEADER']['keyword1']
        keyword_line = config['HEADER']['keyword2']
        keyword_ship = config['HEADER']['keyword3']
        keyword_terms = config['HEADER']['keyword4']
        keyword_shipvia = config['HEADER']['keyword5']

        symbol1_normal = config['NORMALIZATION']['symbol1']
        symbol2_normal = config['NORMALIZATION']['symbol2']

        key_valid = config['VALIDATION']['key1']
        key_total = config['VALIDATION']['key2']        
    else:
        print("Configuration file(config.ini) does not available.")

def is_valid(folder_name):
    if os.path.exists(folder_name):
        return True
    else:
        # Check minimal length for creating directory
        if len(folder_name) > 3:
            os.mkdir(folder_name)
        else:
            print("Output/Log directory " + folder_name +  " not available in config file, So output file/log file stored in applicaion path")
            return False
        


