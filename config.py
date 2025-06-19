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
        
        output_dir = config['DEFAULT']['output_directory']
        is_valid(output_dir)
        log_file_dir = config['DEFAULT']['log_file_path']
        is_valid(log_file_dir)
        output_header_csv = config['DEFAULT']['output_file_header_csv']
        output_line_csv = config['DEFAULT']['output_file_line_csv'] 
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
        


