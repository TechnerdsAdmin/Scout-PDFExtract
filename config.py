import configparser
import os

def read_config():
    import log
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
        #global header_data_name_csv[9]
        #global line_data_name_csv[8]
        
        output_dir = config['DEFAULT']['OUTPUT_DIR']
        is_valid(output_dir)
        log_file_dir = config['DEFAULT']['LOG_FILE_PATH']
        is_valid(log_file_dir)
        output_header_csv = config['DEFAULT']['OUTPUT_FILE_HEADER_CSV']
        output_line_csv = config['DEFAULT']['OUTPUT_FILE_LINE_CSV']

        keyword_date = config['SUKUP_HEADER']['SUKUP_DATE']
        keyword_line = config['SUKUP_HEADER']['SUKUP_LINE']
        keyword_ship = config['SUKUP_HEADER']['SUKUP_SHIPTO']
        keyword_terms = config['SUKUP_HEADER']['SUKUP_TERMS']
        keyword_shipvia = config['SUKUP_HEADER']['SUKUP_SHIPVIA']

        symbol1_normal = config['SUKUP_NORMALIZATION']['SUKUP_CUR']
        symbol2_normal = config['SUKUP_NORMALIZATION']['SUKUP_DELIMETER']

        key_valid = config['SUKUP_VALIDATION']['SUKUP_PO']
        key_total = config['SUKUP_VALIDATION']['SUKUP_TOTAL']       
    else:
        # Get a logger instance
        logger = log.logging.getLogger()
        logger.error("Configuration file(config.ini) does not available.")
        #print("Configuration file(config.ini) does not available.")

def is_valid(folder_name):
    if os.path.exists(folder_name):
        return True
    else:
        # Check minimal length for creating directory
        if len(folder_name) > 3:
            os.mkdir(folder_name)
        else:
            import log
            logger = log.logging.getLogger()
            logger.error("Output/Log directory " + folder_name +  " not available in config file, So output file/log file stored in applicaion path")
            #print("Output/Log directory " + folder_name +  " not available in config file, So output file/log file stored in applicaion path")
            return False
        


