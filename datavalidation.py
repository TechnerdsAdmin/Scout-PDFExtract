import csv
import config
import log
import sys
import shutil
import pandas as pd

def validation_reconciliation(total_po, line_count_po):
    logger = log.logging.getLogger()

    try:
        # Get row count in csv file
        file_path = ''
        if not config.output_dir:
            file_path = config.output_line_csv 
            with open(config.output_line_csv) as file:
                reader  = csv.reader(file)
                row_count = sum(1 for row in reader)  
        else:
            file_path = config.output_dir + "\\" + config.output_line_csv 
            with open(config.output_dir + "\\" + config.output_line_csv) as file:
                reader  = csv.reader(file)
                row_count = sum(1 for row in reader)  
        
        # Get total product amount from line data csv file
        total_csv = calculate_column_sum_csv(file_path, 17)

        if not config.output_dir:
            header_csv_file_path = config.output_header_csv
            line_csv_file_path = config.output_line_csv
        else:
            header_csv_file_path = config.output_dir + "\\" + config.output_header_csv
            line_csv_file_path = config.output_dir + "\\" + config.output_line_csv

        # Compare Total and line count 
        if float(total_po) == total_csv and line_count_po == row_count -1:
            logger.info("Validation and Reconciliation are Success")
            print("\nValidation and Reconciliation are Success\n")
            print("\nOrder header CSV file " + header_csv_file_path + " created successfully.\n")
            logger.info("Order header CSV file " + header_csv_file_path + " created successfully.")
            print("\nOrder line data CSV file " + line_csv_file_path + " created successfully.\n")
            logger.info("Order line data CSV file " + line_csv_file_path + " created successfully.")
        else:
            logger.error("Validation and Reconciliation are Failed")
            print("Validation and Reconciliation are Failed\n")
            shutil.copy("Templates//orderquoteheader.csv", header_csv_file_path)
            shutil.copy("Templates//orderquoteline.csv", line_csv_file_path)
            sys.exit(1)
    except:
        logger.error("An error occured in validation method.")
        sys.exit(1)

# Calculate product amount column sum
def calculate_column_sum_csv(file_path, column_index):
    
    logger = log.logging.getLogger()
    try:
        total_sum = 0
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip the header row
            for row in reader:
                try:
                    
                    # Convert the column value to a number (float or int)
                    value = float(row[column_index]) 
                    total_sum += value
                    
                except (ValueError, IndexError):
                    # Handle cases where conversion fails or column index is out of bounds
                    logger.error("Error during convert column values to float")
                    continue 
        return total_sum
    except:
        logger.error("An error occured in calculate_column_sum_csv method.")
        sys.exit(1)
