import sys
import config
import csv
import normalization
import pdfplumber
import datavalidation
import log

# Extract line data from pdf
def line_data_to_csv(line_data, input_file):
    logger = log.logging.getLogger()
    try:
        line_data_list = []
        all_page_data = ''
        with pdfplumber.open(input_file) as pdf:
            for pdf_page in pdf.pages:
                
                single_page_data = pdf_page.extract_text(layout=True)
                
                # separate each page's text with newline
                all_page_data = all_page_data + '\n' + single_page_data
            
            # get only header information from all page data
            index = all_page_data.find(config.keyword_line)
            if index > 0:
                # Get line data from all data
                line_data = all_page_data[index:]
        
        # Valdation check using keywords
        index = line_data.find(config.key_total)
        if index > 0:
            # Data normalization
            data_normal = normalization.data_normalization(line_data)
            
            # get line data and write into csv
            line_data_list = linedata_to_csv(data_normal, input_file)

            return line_data_list
        else:
            return line_data_list
    except:
        logger.error("An error occured in line_data_to_csv method.")
        exit(1)

# Get line data from data normalization data
def linedata_to_csv(data_normal, input_file):

    logger = log.logging.getLogger()
    try:
        line_start = 0
        line_no =''
        product_amount=''
        product_desc=''
        product_id=''
        product_qty=''
        unit_measure=''
        unit_price=''
        req_date=''
        total_in_po = 0
        line_count_po = 0
        
        with pdfplumber.open(input_file) as pdf:
            
            # Read page by page
            for page in pdf.pages:
                # Read word by word
                words = page.extract_words()
                for word in words:
                    # Get Total value from PO
                    total_pos = data_normal.find("Total")
                    if total_pos > 0:
                        total_in_po = data_normal[total_pos+6:total_pos+6+15].strip()
                    if page.page_number == 1 and word["top"] > 210:
                        if word["x0"] >= 20 and word["x1"] <= 36:
                            if product_amount != "":
                                line_count_po = line_count_po + 1
                                write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 0)
                            line_no = word["text"]
                            line_start = 1
                        if word["x0"] >= 57 and word["x1"] <= 73:
                            product_qty = word["text"]
                        if word["x0"] >= 102 and word["x1"] <= 115:
                            unit_measure = word["text"]
                        if word["x0"] >= 125 and word["x1"] < 205:
                            if line_start == 1:
                                product_id = word["text"]
                            if line_start == 2:
                                product_id = product_id + word["text"]
                        if word["x0"] >= 207 and word["x1"] < 350:
                            if line_start == 1:
                                product_desc = word["text"]
                            if line_start == 2:
                                product_desc = product_desc + word["text"]
                        if word["x0"] >= 400 and word["x1"] < 455:
                            req_date = word["text"]
                            req_date = req_date.split("/")
                            if len(req_date[0]) == 1:
                                req_date[0] = " 0" + req_date[0]
                            else:
                                req_date[0] = " " + req_date[0]
                            if len(req_date[1]) == 1:
                                req_date[1] = "0" + req_date[1]
                            else:
                                req_date[1] = req_date[1]
                            req_date = req_date[0] + "/" + req_date[1] + "/" + req_date[2]
                        if word["x0"] >= 480 and word["x1"] < 530:
                            unit_price = word["text"]
                            unit_price = unit_price.replace(config.symbol1_normal,"")
                            unit_price = unit_price.replace(config.symbol2_normal,"")
                        if word["x0"] >= 550 and word["x1"] < 605:
                            product_amount = word["text"]
                            product_amount = product_amount.replace(config.symbol1_normal,"")
                            product_amount = product_amount.replace(config.symbol2_normal,"")
                            line_start = 2
                    else:
                        # Process rest of the first page
                        if page.page_number > 1 and word["top"] > 70:
                            if word["x0"] >= 20 and word["x1"] <= 36:
                                if product_amount != "":
                                    line_count_po = line_count_po + 1
                                    write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 0)
                                line_no = word["text"]
                                line_start = 1
                            if word["x0"] >= 57 and word["x1"] <= 73:
                                product_qty = word["text"]
                            if word["x0"] >= 102 and word["x1"] <= 115:
                                unit_measure = word["text"]
                            if word["x0"] >= 125 and word["x1"] < 205:
                                if line_start == 1:
                                    product_id = word["text"]
                                if line_start == 2:
                                    product_id = product_id + word["text"]
                            if word["x0"] >= 207 and word["x1"] < 350:
                                if line_start == 1:
                                    product_desc = word["text"]
                                if line_start == 2:
                                    product_desc = product_desc + word["text"]
                            if word["x0"] >= 400 and word["x1"] < 455:
                                req_date = word["text"]
                                req_date = req_date.split("/")
                                if len(req_date[0]) == 1:
                                    req_date[0] = " 0" + req_date[0]
                                else:
                                    req_date[0] = " " + req_date[0]
                                if len(req_date[1]) == 1:
                                    req_date[1] = "0" + req_date[1]
                                else:
                                    req_date[1] = req_date[1]
                                req_date = req_date[0] + "/" + req_date[1] + "/" + req_date[2]
                            if word["x0"] >= 480 and word["x1"] < 530:
                                unit_price = word["text"]
                                unit_price = unit_price.replace(config.symbol1_normal,"")
                                unit_price = unit_price.replace(config.symbol2_normal,"")
                            if word["x0"] >= 550 and word["x1"] < 605:
                                product_amount = word["text"]
                                product_amount = product_amount.replace(config.symbol1_normal,"")
                                product_amount = product_amount.replace(config.symbol2_normal,"")
                                line_start = 2
            if product_amount != "":
                line_count_po = line_count_po + 1
                # Write line data to csv file
                write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 1) 
                
                # Validation and reconciliation 
                datavalidation.validation_reconciliation(total_in_po, line_count_po)
    except:
        logger.error("An error occured in linedata_to_csv method.")
        sys.exit(1)
                
# Write line data to csv file
def write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, display):
    
    logger = log.logging.getLogger()
    try:
        line_data = [
            ["", line_no, product_id, product_qty, unit_measure, unit_price, product_desc,"","","","","",req_date, "","","","", product_amount, "","","","","","","","","","","","","","","","","","","","","",""]
        ]
        
        if not config.output_dir:
            line_csv_file_path = config.output_line_csv
        else:
            line_csv_file_path = config.output_dir + "\\" + config.output_line_csv
        try:
            with open(line_csv_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(line_data)
        except PermissionError:
            logger.error("Permission denied: Cannot write to the file due to file is already open. Close the file and try again")
            sys.exit(1)
        except FileNotFoundError:
            logger.error("File not found: Ensure the file path is correct.")
            sys.exit(1)
    except:
        logger.error("An error occured in write_linedata_csv method.")
        sys.exit(1)

