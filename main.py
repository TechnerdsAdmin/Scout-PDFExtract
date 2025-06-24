
import sys
import os
import config
import dataextraction
import log

# Get a logger instance
logger = log.logging.getLogger(__name__)

# argument validation
if len(sys.argv) < 2:
    #print("Error: Please provide an argument as filename.")
    logger.error("Please provide an argument as filename.")
    sys.exit(1)

# read configuration file
#config.read_config()

# getting input file from command line argument
input_file = sys.argv[1]

if os.path.exists(input_file):
    file_name = os.fsdecode(input_file)
    if file_name.endswith('.pdf') or file_name.endswith('.PDF'):
        dataextraction.data_extraction(input_file)        
    else:
        #print('Invalid input file')
        logger.error("Invalid input file")
else:
    #print("Input file does not exist")
    logger.error("Input file does not exist")
 

    
