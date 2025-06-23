import os
import config
import csv
import normalization
import pdfplumber

def line_data_to_csv(line_data, input_file):

    # Valdation check using keywords
    index = line_data.find("Total")
    if index > 0:
        # Data normalization
        data_normal = normalization.data_normalization(line_data)
        #print(data_normal)

        # write line data to csv
        linedata_to_csv(data_normal, input_file)

        return True
    else:
        return False

def linedata_to_csv(data_normal, input_file):

    line_data_header= [
        ['line_no', 'product_id', 'quantity_ordered', 'unit_of_measure', 'unit_price', 'description', 'extended_price', 'required_date']
    ]

    # get output directory and output file name from config.ini
    config.read_config()
    if not config.output_dir:
        with open(config.output_header_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data_header)
        #print("\nOrder line data CSV file " + config.output_line_csv + " created successfully.\n")
    else:
        with open(config.output_dir + "\\" + config.output_line_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data_header)
        #print("\nOrder line data CSV file " + config.output_dir + "\\" + config.output_line_csv + " created successfully.\n")
    
    line_start = 0
    line_no =''
    product_amount=''
    product_desc=''
    product_id=''
    product_qty=''
    unit_measure=''
    unit_price=''
    req_date=''
    with pdfplumber.open(input_file) as pdf:
        page_count = len(pdf.pages)
        for page in pdf.pages:
            #print(page.page_number)
            words = page.extract_words()
            for word in words:
                if page.page_number == 1 and word["top"] > 210:
                    if word["x0"] >= 20 and word["x1"] <= 36:
                        if product_amount != "":
                            write_linedata_csv(line_no, product_qty, unit_measure, product_id, product_desc, req_date, unit_price, product_amount,0)
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
                                write_linedata_csv(line_no, product_qty, unit_measure, product_id, product_desc, req_date, unit_price, product_amount, 0)
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
            write_linedata_csv(line_no, product_qty, unit_measure, product_id, product_desc, req_date, unit_price, product_amount, 1)
                #print(line_no+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_desc+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")
            # line_no =''
            # product_amount=''
            # product_desc=''
            # product_id=''
            # product_qty=''
            # unit_measure=''
            # unit_price=''
            # req_date=''
    # # Display headers
    # print("Line"+"\t"+"QTY"+"\t"+"UM"+"\t"+"Item"+"\t"+"Description"+"\t"+"Date Prom"+"\t"+"Price"+"\t"+"Amount"+"\n")
    # # get each columns values
    # line = ''
    # count = 0
    # display = False
    # appendData = False
    # duplicate = 0
    # for char in data_normal.strip():
    #     if char == '\n':
    #         if len(line) > 2:
    #             line_list = line.split()
    #             #print(line_list)
    #             if len(line_list) == 1:
    #                 if appendData == False:
    #                     product_description = product_description + " " + line_list[0]
    #                 else:
    #                     if product_id[1].isdigit():
    #                         product_id = product_id + " " + line_list[0]
    #                     else:
    #                         product_description = product_description + " " + line_list[0]
    #                 display = True
    #                 duplicate = 0
    #             if len(line_list) == 2:
    #                 product_id = product_id + " " + line_list[0]
    #                 product_description = product_description + " " + line_list[1]
    #                 display = True
    #                 appendData = True
    #                 duplicate = 0
    #             if len(line_list) == 3:
    #                 product_id = product_id + " " + line_list[0] + " " + line_list[1]
    #                 product_description = product_description + " " + line_list[2]
    #                 #display = True
    #                 duplicate = 0
    #                 appendData = True
    #             if duplicate == 1:
    #                 print(line_num+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_description+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")
    #                 display = False
    #                 duplicate = 0
    #             if len(line_list) > 7:
    #                 duplicate = 1
    #                 line_num = line_list[0]
    #                 product_qty = line_list[1]
    #                 unit_measure = line_list[2]
    #                 product_id = line_list[3]
    #                 product_description = line_list[4]
    #                 if line_list[5].find("/") > 0:
    #                     req_date = line_list[5]
    #                     unit_price = line_list[6]
    #                     product_amount = line_list[7]
    #                 else:
    #                     req_date = line_list[6]
    #                     product_description = product_description + " " + line_list[5]
    #                     unit_price = line_list[7]
    #                     product_amount = line_list[8]
    #             line = ''
    #             if display == True:
    #                 display = False
    #                 print(line_num+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_description+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")
    #         count = count + 1
    #         if count == len(data_normal):
    #             #line_list = line.split()
    #             break
    #     else:
    #         if count > 0:
    #             line = line + char
    # #print(line_list)
    # #print(line_num)

    # line_data = [
    #     ['line_no', 'product_id', 'quantity_ordered', 'unit_of_measure', 'unit_price', 'description', 'extended_price', 'required_date'],
    #     [line_num, product_id, product_qty, unit_measure, unit_price, product_description, product_amount, req_date]
    #     #[po_num, order_date, shipAddress.strip(), addressOne.strip(), cityZip[0].strip(), state[0].strip(), state[1].strip(), terms.strip(), shipVia]
    # ]

    # # get output directory and output file name from config.ini
    # config.read_config()
    # if not config.output_dir:
    #     with open(config.output_header_csv, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(line_data)
    #     #print("\nOrder line data CSV file " + config.output_line_csv + " created successfully.\n")
    # else:
    #     with open(config.output_dir + "\\" + config.output_line_csv, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(line_data)
    #     #print("\nOrder line data CSV file " + config.output_dir + "\\" + config.output_line_csv + " created successfully.\n")

def write_linedata_csv(line_no, product_qty, unit_measure, product_id, product_desc, req_date, unit_price, product_amount, display):
    
    line_data = [
        [line_no, product_qty, unit_measure, product_id, product_desc, req_date, unit_price, product_amount]
    ]
    config.read_config()
    if not config.output_dir:
        with open(config.output_header_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        if display == 1:
            print("\nOrder line data CSV file " + config.output_line_csv + " created successfully.\n")
    else:
        with open(config.output_dir + "\\" + config.output_line_csv, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        if display == 1:
            print("\nOrder line data CSV file " + config.output_dir + "\\" + config.output_line_csv + " created successfully.\n")
    

    #print(line_no+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_desc+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")