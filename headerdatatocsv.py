import sys
import config
import csv
import log

def header_data_to_csv(header_data):
    
    logger = log.logging.getLogger()
    lines = header_data.split('\n')
    header_data_csv = []
    #print(lines[4])
    if len(lines[4].strip()) > 0:
        # Read keyword to identified the date
        #config.read_config()
        
        po_num = lines[4].strip()
        
        header_data_csv.insert(0,po_num)
        index = header_data.find(config.keyword_date)
        #print(index)
        if index > 0:
            order_date = header_data[index+6:index+6+10]
            header_data_csv.insert(1,order_date)
        index = header_data.find(config.keyword_ship)
        if index > 0:
            # Get Ship To address
            shipAddress = get_To_Address(lines[14].strip())
            header_data_csv.insert(2,shipAddress)
            # Get Address
            addressOne = get_To_Address(lines[15].strip())
            header_data_csv.insert(3,addressOne)
            # Get City and Zip code
            address = get_To_Address(lines[16].strip())
            cityZip = address.split(",")
            header_data_csv.insert(4,cityZip)
            # Get state
            city = ''
            state = ''
            zipCode = ''
            if len(cityZip) > 0:
                city = cityZip[0].strip()
                states = cityZip[1].strip().split(" ")
                state = states[0].strip()
                zipCode = states[1].strip()
                header_data_csv.insert(5,state)
                header_data_csv.insert(6,zipCode)
            else:
                city = ""
                state = ""
                zipCode =""
                header_data_csv.insert(5,"")
                header_data_csv.insert(6,"")
            # Get terms and Ship Via
            index = header_data.find(config.keyword_terms)
            if index > 0:
                terms = header_data[index+7:index+7+20]
                header_data_csv.insert(7,terms)
            else:
                terms = ''
            index = header_data.find(config.keyword_shipvia)
            if index > 0:
                shipVia = header_data[index+10:index+10+20]
                header_data_csv.insert(8,shipVia)
            else:
                shipVia = ''
                
            header_data = [
                ["","","","","",po_num, "", "","", "", order_date, "","","","", shipAddress.strip(), addressOne.strip(), "", city, state, zipCode, "","","","","","","", terms.strip(), "","","","","","","","","","","","","","","","",'',"","","","","","","","","","","","","","","","",'',shipVia.strip(), "","","","","","","","","","",""]
            ]
                #['customer_po_no', 'order_date', 'ship_to_name', 'ship_to_address_1', 'ship_to_city', 'ship_to_state', 'ship_to_zip', 'terms', 'ship_via'],
                #["","","","","",po_num, "", "","", "", order_date, "","","","", shipAddress.strip(), addressOne.strip(), "", cityZip[0].strip(), state[0].strip(), state[1].strip(), "","","","","","","", terms.strip(), "","","","","","","","","","","","","","","","",'',"","","","","","","","","","","","","","","","",'',shipVia.strip(), "","","","","","","","","","",""]
            
            #write to csv file
            header_to_csv(header_data)
            #return True
            return header_data_csv
    else:
        #print("PO Number not found, Input file consider as a not a valid file")
        logger.error("PO Number not found, Input file consider as a not a valid file")
        sys.exit(0)
       # return False

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
    #print(header_data)
    logger = log.logging.getLogger()
    # get output directory and output file name from config.ini
    #config.read_config()
    if not config.output_dir:
        header_csv_file_path = config.output_header_csv
    else:
        header_csv_file_path = config.output_dir + "\\" + config.output_header_csv
    try:
        with open(header_csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(header_data)
        #print("\nOrder header CSV file " + header_csv_file_path + " created successfully.\n")
        #logger.info("Order header CSV file " + header_csv_file_path + " created successfully.")
    except PermissionError:
        logger.error("Permission denied: Cannot write to the file due to file is already open. Close the file and try again")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("File not found: Ensure the file path is correct.")
        sys.exit(1)

    
