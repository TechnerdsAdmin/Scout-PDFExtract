import sys
import config
import csv
import normalization
import pdfplumber
import datavalidation
import log

def line_data_to_csv(line_data, input_file):
    
    line_data_list = []
    all_page_data = ''
    with pdfplumber.open(input_file) as pdf:
        for pdf_page in pdf.pages:
            
            single_page_data = pdf_page.extract_text(layout=True)
            
            # separate each page's text with newline
            all_page_data = all_page_data + '\n' + single_page_data
        
        # Read keyword to identified the table data
        #config.read_config()
        # get only header information from all page data
        index = all_page_data.find(config.keyword_line)
        if index > 0:
            line_data = all_page_data[index:]
    # Valdation check using keywords
    #print(line_data)
    index = line_data.find(config.key_total)
    if index > 0:
        # Data normalization
        data_normal = normalization.data_normalization(line_data)
        #print(data_normal)

        # write line data to csv
        line_data_list = linedata_to_csv(data_normal, input_file)

        return line_data_list
    else:
        return line_data_list

def linedata_to_csv(data_normal, input_file):

    logger = log.logging.getLogger("")
    
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
    #line_data_csv = []
    with pdfplumber.open(input_file) as pdf:
        page_count = len(pdf.pages)
        for page in pdf.pages:
            #print(page.page_number)
            words = page.extract_words()
            for word in words:
                #total_word = word["text"]
                total_pos = data_normal.find("Total")
                if total_pos > 0:
                    total_in_po = data_normal[total_pos+6:total_pos+6+15].strip()
                    #print(total_in_po)
                if page.page_number == 1 and word["top"] > 210:
                    if word["x0"] >= 20 and word["x1"] <= 36:
                        if product_amount != "":
                            #line_count_po = line_count_po + 1
                            
                            line_count_po = line_count_po + 1
                            write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 0)
                        #line_list.insert(0,word["text"])
                        line_no = word["text"]
                        line_start = 1
                        #print(word["text"])
                    if word["x0"] >= 57 and word["x1"] <= 73:
                        product_qty = word["text"]
                        #line_list.insert(1,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 102 and word["x1"] <= 115:
                        unit_measure = word["text"]
                        #line_list.insert(2,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 125 and word["x1"] < 205:
                        if line_start == 1:
                            #line_list.insert(3,word["text"])
                            product_id = word["text"]
                        if line_start == 2:
                            product_id = product_id + word["text"]
                            #line_list.append(3,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 207 and word["x1"] < 350:
                        if line_start == 1:
                            product_desc = word["text"]
                            #line_list.insert(4,word["text"])
                        if line_start == 2:
                            product_desc = product_desc + word["text"]
                            #line_list.append(4,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 400 and word["x1"] < 455:
                        req_date = word["text"]
                        #line_list.insert(5,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 480 and word["x1"] < 530:
                        unit_price = word["text"]
                        unit_price = unit_price.replace("$","")
                        unit_price = unit_price.replace(",","")
                        #line_list.insert(6,word["text"])
                        #print(word["text"])
                    if word["x0"] >= 550 and word["x1"] < 605:
                        product_amount = word["text"]
                        product_amount = product_amount.replace("$","")
                        product_amount = product_amount.replace(",","")
                        #line_list.insert(7,word["text"])
                        #print(word["text"])
                        line_start = 2
                else:
                    if page.page_number > 1 and word["top"] > 70:
                        if word["x0"] >= 20 and word["x1"] <= 36:
                            if product_amount != "":
                                line_count_po = line_count_po + 1
                                write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 0)
                            #line_list.insert(0,word["text"])
                            line_no = word["text"]
                            line_start = 1
                            #print(word["text"])
                        if word["x0"] >= 57 and word["x1"] <= 73:
                            product_qty = word["text"]
                            #line_list.insert(1,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 102 and word["x1"] <= 115:
                            unit_measure = word["text"]
                            #line_list.insert(2,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 125 and word["x1"] < 205:
                            if line_start == 1:
                                #line_list.insert(3,word["text"])
                                product_id = word["text"]
                            if line_start == 2:
                                product_id = product_id + word["text"]
                                #line_list.append(3,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 207 and word["x1"] < 350:
                            if line_start == 1:
                                product_desc = word["text"]
                                #line_list.insert(4,word["text"])
                            if line_start == 2:
                                product_desc = product_desc + word["text"]
                                #line_list.append(4,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 400 and word["x1"] < 455:
                            req_date = word["text"]
                            #line_list.insert(5,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 480 and word["x1"] < 530:
                            unit_price = word["text"]
                            unit_price = unit_price.replace("$","")
                            unit_price = unit_price.replace(",","")
                            #line_list.insert(6,word["text"])
                            #print(word["text"])
                        if word["x0"] >= 550 and word["x1"] < 605:
                            product_amount = word["text"]
                            product_amount = product_amount.replace("$","")
                            product_amount = product_amount.replace(",","")
                            #line_list.insert(7,word["text"])
                            #print(word["text"])
                            line_start = 2
        if product_amount != "":
            line_count_po = line_count_po + 1
            write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, 1) 
            # Validation and reconciliation 
            datavalidation.validation_reconciliation(total_in_po, line_count_po)
            #return line_data_csv
                
def write_linedata_csv(line_no, product_id, product_qty, unit_measure, unit_price, product_desc, product_amount, req_date, display):
    
    line_data = [
        ["", line_no, product_id, product_qty, unit_measure, unit_price, product_desc,"","","","","",req_date, "","","","", product_amount, "","","","","","","","","","","","","","","","","","","","","",""]
    ]
    #print(line_data)
    logger = log.logging.getLogger("")
    config.read_config()
    if not config.output_dir:
        line_csv_file_path = config.output_line_csv
    else:
        line_csv_file_path = config.output_dir + "\\" + config.output_line_csv
    try:
        with open(line_csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        # if display == 1:
        #     print("\nOrder line data CSV file " + line_csv_file_path + " created successfully.\n")
        #     logger.info("Order line data CSV file " + line_csv_file_path + " created successfully.")
    except PermissionError:
        #print("Permission denied: Cannot write to the file. Check permissions.")
        logger.error("Permission denied: Cannot write to the file due to file is already open. Close the file and try again")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("File not found: Ensure the file path is correct.")
        sys.exit(1)
    
