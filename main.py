
import sys
import os
import dataextraction
import log
import headerdatatocsv
import linedatatocsv
import datavalidation
import shutil
import config

# Get a logger instance
logger = log.logging.getLogger()

# argument validation
if len(sys.argv) < 2:
    logger.error("Input file name is missing.")
    sys.exit(1)

# getting input file from command line argument
input_file = sys.argv[1]

if os.path.exists(input_file):
    file_name = os.fsdecode(input_file)
    if not file_name.endswith('.pdf'):
        logger.error("Invalid input file format. Its support only pdf files")
        sys.exit(0)
    else:
        # move both csv files to output folder from template folder
        try:
            config.read_config()
            shutil.copy("Templates//orderquoteheader.csv", config.output_dir + "//" + config.output_header_csv)
            logger.error("Oreder header csv file copied to output folder successfully")
            shutil.copy("Templates//orderquoteline.csv", config.output_dir + "//" + config.output_line_csv)
            logger.error("Oreder line csv file copied to output folder successfully")
        except FileNotFoundError:
            logger.error("Source file not found.")
        except Exception as e:
            logger.error("An error occurred while copying file")
       
else:
    logger.error("Input file does not exist")
    sys.exit(0)
 
# data extraction 
extract_data = dataextraction.data_extraction(input_file)
#print(extract_data)
# Get header data
header_list = headerdatatocsv.header_data_to_csv(extract_data)
#print(header_list)
if header_list:
    
    # # Get Line data
    linedatatocsv.line_data_to_csv(header_list, input_file)
    
else:
    logger.error("PO Number not found, Input file consider as a not a valid file")
    
