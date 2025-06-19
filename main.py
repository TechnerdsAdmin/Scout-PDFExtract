
import sys
import os
import config
import dataextraction

# read configuration file
config.read_config()
#output_folder = readconfig.output_dir
#print("OUTPUT: " + readconfig.output_dir)

# getting input file from command line argument
input_file = sys.argv[1]

if os.path.exists(input_file):
    file_name = os.fsdecode(input_file)
    if file_name.endswith('.pdf') or file_name.endswith('.PDF'):
        dataextraction.data_extraction(input_file)        
    else:
        print('Invalid input file')
else:
    print("Input file does not exist")
 

    
