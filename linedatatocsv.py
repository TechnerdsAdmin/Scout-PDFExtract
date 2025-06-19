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
    for char in data_normal:
        if char == '\n':
            line = line + char
            count = count + 1
            if count == 3:
                line_list = line.split()
                break
        else:
            if count > 0:
                line = line + char
    print(line_list[0])

    line_data = [
        ['line_no', 'product_id', 'quantity_ordered', 'unit_of_measure', 'unit_price', 'description', 'extended_price', 'required_date'],
        line_list
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
    