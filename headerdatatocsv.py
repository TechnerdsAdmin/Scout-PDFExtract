import os
import config
import csv
import config

def header_data_to_csv(header_data):
    
    lines = header_data.split('\n')
    if len(lines[4]) > 0:
        # Read keyword to identified the date
        config.read_config()

        po_num = lines[4].strip()
        index = header_data.find(config.keyword_date)
        #print(index)
        if index > 0:
            order_date = header_data[index+6:index+6+10]
           
        index = header_data.find(config.keyword_ship)
        if index > 0:
            # Get Ship To address
            shipAddress = get_To_Address(lines[14].strip())
           
            # Get Address
            addressOne = get_To_Address(lines[15].strip())
           
            # Get City and Zip code
            address = get_To_Address(lines[16].strip())
            cityZip = address.split(",")
           
            # Get state
            state = cityZip[1].strip().split(" ")

            # Get terms and Ship Via
            index = header_data.find(config.keyword_terms)
            if index > 0:
                terms = header_data[index+7:index+7+20]
            else:
                terms = ''
            index = header_data.find(config.keyword_shipvia)
            if index > 0:
                shipVia = header_data[index+10:index+10+20]
            else:
                shipVia = ''
                
            header_data = [
                ['customer_po_no', 'order_date', 'ship_to_name', 'ship_to_address_1', 'ship_to_city', 'ship_to_state', 'ship_to_zip', 'terms', 'ship_via'],
                [po_num, order_date, shipAddress.strip(), addressOne.strip(), cityZip[0].strip(), state[0].strip(), state[1].strip(), terms.strip(), shipVia]
            ]
            # write to csv file
            header_to_csv(header_data)
            return True
    else:
        print("PO Number not found, Input file consider as a not a valid file")
        return False

def get_To_Address(fromToAddress):
    
    count = 0
    toAddress = ''
    for char in fromToAddress:
        if char == " ":
            count = count + 1
            if (count > 2):
                toAddress = toAddress + char
        else:
            if (count > 2):
                toAddress = toAddress + char
            else:
                count = 0
    return toAddress        

def header_to_csv(header_data):
    
    # get output directory and output file name from config.ini
    config.read_config()
    if not config.output_dir:
        with open(config.output_header_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(header_data)
        print("\nOrder header CSV file " + config.output_header_csv + " created successfully.\n")
    else:
        with open(config.output_dir + "\\" + config.output_header_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(header_data)
        print("\nOrder header CSV file " + config.output_dir + "\\" + config.output_header_csv + " created successfully.\n")
    
    
    
