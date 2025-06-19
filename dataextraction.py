
import pdfplumber
import headerdatatocsv
import linedatatocsv

def data_extraction(input_file):
   with pdfplumber.open(input_file) as pdf:
       # Read pdf data
       all_page_data = ''
       for pdf_page in pdf.pages:
          single_page_data = pdf_page.extract_text(layout=True)
          
          # separate each page's text with newline
          all_page_data = all_page_data + '\n' + single_page_data
       
       # get only header information from all page data
       index = all_page_data.find("Line")
       if index > 0:
          if headerdatatocsv.header_data_to_csv(all_page_data[0:index]):
             # Process line data
             if linedatatocsv.line_data_to_csv(all_page_data[index:]):
                print("Completed...")
             else:
                print("Input file is not a valid file")
       else:
          print("Input file is not a valid file")
       
       #page = pdf.pages[0]
       #text = page.extract_text()
       #print(text)

       # Extract the data
       #tables = page.extract_table()
       #for table in tables:
        #  print(table)
         

    
