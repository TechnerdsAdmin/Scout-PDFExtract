
import pdfplumber
import headerdatatocsv
import linedatatocsv
import config
import log
import sys

def data_extraction(input_file):

   logger = log.logging.getLogger("")
   
   with pdfplumber.open(input_file) as pdf:
       # Read pdf data
       all_page_data = ''
       for pdf_page in pdf.pages:
          
          single_page_data = pdf_page.extract_text(layout=True)
          
          # separate each page's text with newline
          all_page_data = all_page_data + '\n' + single_page_data
       
       # Read keyword to identified the table data
       config.read_config()
       # get only header information from all page data
       index = all_page_data.find(config.keyword_line)
       if index > 0:
          return all_page_data[0:index]

         #  if headerdatatocsv.header_data_to_csv(all_page_data[0:index]):
         #     # Process line data
         #     if linedatatocsv.line_data_to_csv(all_page_data[index:], input_file):
         #        #print("Completed...")
         #        logger.info("Process Completed ")
         #     else:
         #        logger.error("Total/PO keyword not found so halt the application")
         #        #print("Input file is not a valid file")
       else:
          logger.error("Total/PO keyword not found so halt the application")
          sys.exot(0)
          #print("Input file is not a valid file")
         

    
