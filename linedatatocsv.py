import os
import config
import csv
import normalization

def line_data_to_csv(line_data):

    # Valdation check using keywords
    index = line_data.find("Total")
    if index > 0:
        # Data normalization
        data_normal = normalization.data_normalization(line_data)
        #print(data_normal)

        # write line data to csv
        linedata_to_csv(data_normal)

        return True
    else:
        return False

def linedata_to_csv(data_normal):

    # Display headers
    print("Line"+"\t"+"QTY"+"\t"+"UM"+"\t"+"Item"+"\t"+"Description"+"\t"+"Date Prom"+"\t"+"Price"+"\t"+"Amount"+"\n")
    # get each columns values
    line = ''
    count = 0
    display = False
    appendData = False
    duplicate = 0
    for char in data_normal.strip():
        if char == '\n':
            if len(line) > 2:
                line_list = line.split()
                #print(line_list)
                if len(line_list) == 1:
                    if appendData == False:
                        product_description = product_description + " " + line_list[0]
                    else:
                        if product_id[1].isdigit():
                            product_id = product_id + " " + line_list[0]
                        else:
                            product_description = product_description + " " + line_list[0]
                    display = True
                    duplicate = 0
                if len(line_list) == 2:
                    product_id = product_id + " " + line_list[0]
                    product_description = product_description + " " + line_list[1]
                    #display = True
                    appendData = True
                    duplicate = 0
                if len(line_list) == 3:
                    product_id = product_id + " " + line_list[0] + " " + line_list[1]
                    product_description = product_description + " " + line_list[2]
                    #display = True
                    duplicate = 0
                    appendData = True
                if duplicate == 1:
                    print(line_num+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_description+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")
                    display = False
                    duplicate = 0
                if len(line_list) > 7:
                    duplicate = 1
                    line_num = line_list[0]
                    product_qty = line_list[1]
                    unit_measure = line_list[2]
                    product_id = line_list[3]
                    product_description = line_list[4]
                    if line_list[5].find("/") > 0:
                        req_date = line_list[5]
                        unit_price = line_list[6]
                        product_amount = line_list[7]
                    else:
                        req_date = line_list[6]
                        product_description = product_description + " " + line_list[5]
                        unit_price = line_list[7]
                        product_amount = line_list[8]
                line = ''
                if display == True:
                    display = False
                    print(line_num+"\t"+product_qty+"\t"+unit_measure+"\t"+product_id+"\t"+product_description+"\t"+req_date+"\t"+unit_price+"\t"+product_amount+"\n")
            count = count + 1
            if count == len(data_normal):
                #line_list = line.split()
                break
        else:
            if count > 0:
                line = line + char
    #print(line_list)
    #print(line_num)

    line_data = [
        ['line_no', 'product_id', 'quantity_ordered', 'unit_of_measure', 'unit_price', 'description', 'extended_price', 'required_date'],
        [line_num, product_id, product_qty, unit_measure, unit_price, product_description, product_amount, req_date]
        #[po_num, order_date, shipAddress.strip(), addressOne.strip(), cityZip[0].strip(), state[0].strip(), state[1].strip(), terms.strip(), shipVia]
    ]

    # get output directory and output file name from config.ini
    config.read_config()
    if not config.output_dir:
        with open(config.output_header_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        #print("\nOrder line data CSV file " + config.output_line_csv + " created successfully.\n")
    else:
        with open(config.output_dir + "\\" + config.output_line_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        #print("\nOrder line data CSV file " + config.output_dir + "\\" + config.output_line_csv + " created successfully.\n")
    