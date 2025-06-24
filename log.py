
import logging
import config

# read configuration file
config.read_config()
if not config.log_file_dir:
    # Configure logging
    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
else:
    logging.basicConfig(filename= config.log_file_dir + "\\" + 'app.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')