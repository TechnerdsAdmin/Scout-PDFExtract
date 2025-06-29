
import pdfplumber
import config
import log
import sys

def data_extraction(input_file):

   logger = log.logging.getLogger()
   try:
      with pdfplumber.open(input_file) as pdf:
         # Read pdf data
         all_page_data = ''
         for pdf_page in pdf.pages:
            
            # layout = True to maintain te text format
            single_page_data = pdf_page.extract_text(layout=True)
            
            # separate each page's text with newline
            all_page_data = all_page_data + '\n' + single_page_data
         
         # get only header information from all page data
         index = all_page_data.find(config.keyword_line)
         if index > 0:
            #Header information
            return all_page_data[0:index]

         else:
            # Exit the application if input firl does not have Total and PO
            logger.error("Application terminated due to Total or Purchase order not found.")
            #sys.exit(1)
   except:
      logger.error("An error occured in data_extraction method.")
      sys.exit(1)
         

    
