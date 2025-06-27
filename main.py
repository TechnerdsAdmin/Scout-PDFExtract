
import sys
import os
import dataextraction
import log
import headerdatatocsv
import linedatatocsv
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
        sys.exit(1)
    else:
        # move both csv files to output folder from template folder
        try:
            #config.read_config()
            if not config.output_dir:
                header_csv_file_path = config.output_header_csv
                line_csv_file_path = config.output_line_csv
            else:
                header_csv_file_path = config.output_dir + "\\" + config.output_header_csv
                line_csv_file_path = config.output_dir + "\\" + config.output_line_csv
            
            shutil.copy("Templates//orderquoteheader.csv", header_csv_file_path)
            logger.info("Order header csv file copied to output folder successfully")
            shutil.copy("Templates//orderquoteline.csv", line_csv_file_path)
            logger.info("Order line csv file copied to output folder successfully")
        except FileNotFoundError:
            logger.error("Source file not found.")
            sys.exit(1)
        except Exception as e:
            logger.error("An error occurred while copying file")
            sys.exit(1)
else:
    logger.error("Input file does not exist")
    sys.exit(1)

# Split header data and line data 
extract_data = dataextraction.data_extraction(input_file)

# Pass header data and get header csv file
header_list = headerdatatocsv.header_data_to_csv(extract_data)

if header_list:
    # Process the Line data
    linedatatocsv.line_data_to_csv(header_list, input_file)
else:
    logger.error("PO Number not found, Input file consider as a not a valid file")
    sys.exit(1)