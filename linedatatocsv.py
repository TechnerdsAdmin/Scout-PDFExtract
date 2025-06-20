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

    # get each columns values
    line = ''
    count = 0
    #line_list = []
    # line_num = []
    # product_id = []
    # product_qty = []
    # unit_measure = []
    # unit_price = []
    # product_description = []
    # product_amount = []
    # req_date = [] 
    for char in data_normal.strip():
        if char == '\n':
            
            if len(line) > 2:
                line_list = line.split()
                print(line_list[0])
                # line_num.insert(count, line_list[0])
                # product_qty.insert(count, line_list[1])
                # unit_measure.insert(count, line_list[2])
                # product_id.insert(count, line_list[3])
                # product_description.insert(count, line_list[4])
                # req_date.insert(count, line_list[5])
                # unit_price.insert(count, line_list[6])
                # product_amount.insert(count, line_list[7])
                line_num = line_list[0]
                product_qty = line_list[1]
                unit_measure = line_list[2]
                product_id = line_list[3]
                product_description = line_list[4]
                req_date = line_list[5]
                unit_price = line_list[6]
                product_amount = line_list[7]
                #line_num.append(line_list[0])
            count = count + 1
            if count == 2:
                line_list = line.split()
                break
        else:
            if count > 0:
                line = line + char
    print(line_list)
    print(line_num)

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
        print("\nOrder line data CSV file " + config.output_line_csv + " created successfully.\n")
    else:
        with open(config.output_dir + "\\" + config.output_line_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(line_data)
        print("\nOrder line data CSV file " + config.output_dir + "\\" + config.output_line_csv + " created successfully.\n")
    