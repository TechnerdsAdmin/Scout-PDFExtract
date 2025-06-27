import sys
import config
import csv
import log

# Get required fields from header data
def header_data_to_csv(header_data):
    
    logger = log.logging.getLogger()
    try:
        lines = header_data.split('\n')
        header_data_csv = []
        
        if len(lines[4].strip()) > 0:
            
            # Get PO number
            po_num = lines[4].strip()
            header_data_csv.insert(0,po_num)

            # Get order date using keyword and extract it
            index = header_data.find(config.keyword_date)
            
            if index > 0:
                order_date = header_data[index+6:index+6+10]
                header_data_csv.insert(1,order_date)
            
            # Get Ship address information using keyword
            index = header_data.find(config.keyword_ship)
            if index > 0:
                # Get Ship To address
                shipAddress = get_to_address(lines[14].strip())
                header_data_csv.insert(2,shipAddress)
                # Get Address
                addressOne = get_to_address(lines[15].strip())
                header_data_csv.insert(3,addressOne)
                # Get City and Zip code
                address = get_to_address(lines[16].strip())
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

                # Header data inforamtion    
                header_data = [
                    ["","","","","",po_num, "", "","", "", order_date, "","","","", shipAddress.strip(), addressOne.strip(), "", city, state, zipCode, "","","","","","","", terms.strip(), "","","","","","","","","","","","","","","","",'',"","","","","","","","","","","","","","","","",'',shipVia.strip(), "","","","","","","","","","",""]
                ]
                
                #write to csv file
                header_to_csv(header_data)

                return header_data_csv
        else:
            logger.error("PO Number not found, Input file consider as a not a valid file")
            sys.exit(1)
    except:
        logger.error("An error occured in linedataheader_data_to_csv method.")
        sys.exit(1)

# Logic to get ship address details 
def get_to_address(fromToAddress):
    logger = log.logging.getLogger()

    try:
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
    except:
        logger.error("An error occured in get_to_address method.")
        sys.exit(1)

# Write order header data to csv file 
def header_to_csv(header_data):
    
    logger = log.logging.getLogger()
    try:
        # get output directory and output file name from config.ini
        if not config.output_dir:
            header_csv_file_path = config.output_header_csv
        else:
            header_csv_file_path = config.output_dir + "\\" + config.output_header_csv

        # Append data to existing template excel sheet
        try:
            with open(header_csv_file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(header_data)
        except PermissionError:
            logger.error("Permission denied: Cannot write to the file due to file is already open. Close the file and try again")
            sys.exit(1)
        except FileNotFoundError:
            logger.error("File not found: Ensure the file path is correct.")
            sys.exit(1)
    except:
        logger.error("An error occured in header_to_csv method.")
        sys.exit(1)

    
