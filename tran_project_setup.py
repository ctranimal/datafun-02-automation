"""
File: tran_project_setup.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Canh Tran

"""

#####################################
# Import Modules at the Top
#####################################

# Import from the Python Standard library
import pathlib
import sys      
import time

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules

import utils_tran

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

REGIONS = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
]

# This global variable: will SKIP executing code if isOff is True
isOff : bool = False

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.

    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: start_year = {start_year}, end_year = {end_year}")

    for year in range(start_year, end_year + 1):
         folder_name = "dir_" + str(year)
         year_path = ROOT_DIR / folder_name
         year_path.mkdir(exist_ok=True)
         logger.info(f"Created folder: {year_path}")


  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")

    for folder in folder_list:
         folder_path = ROOT_DIR / folder
         folder_path.mkdir(exist_ok=True)
         logger.info(f"Created folder: {folder_path}")      
    
  
#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")

    for folder in folder_list:
        folder_name = prefix + str(folder)
        folder_path = ROOT_DIR / folder_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")   
  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''    
    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")

    # define the max # number of folder created, to prevent infinite looping
    max_FoldersCreated_num : int = 5

    # counter to iterate through
    counter_num : int = 1

    while (counter_num <= max_FoldersCreated_num):
        folder_name = "dir_" + str(counter_num)
        folder_path = ROOT_DIR / folder_name
        folder_path.mkdir(exist_ok=True)
        logger.info(f"Created folder: {folder_path}")   
        logger.info(f"   WAITING: counter = {counter_num}, duration_seconds = {duration_seconds}")        
        time.sleep(duration_seconds)  # wait for duration_seconds before creating new folder
        counter_num += 1


#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    lowercase_list = [item.lower() for item in folder_list]
    spaceremoved_list = [ item2.replace(" ", "") for item2 in lowercase_list]

    logger.info(f"IMPROVE_LIST: the original list is transformed to = {spaceremoved_list}")    

    # Now, make a call to function 3 implemented, with prefix "dir"
    create_prefixed_folders_using_list_comprehension(spaceremoved_list, "dir_")


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    logger.info(f"Byline: {utils_tran.get_byline()}")

    # isOff as boolean varialbe: it's a good to "turn-off" certain codes to be executed, easy to test out in main function.
    # when everything is DONE, switch isOff to False, and the code  becomes "LIVE"
    if(not(isOff)):
        # Call function 1 to create folders for a range (e.g. years)
        create_folders_for_range(start_year=2020, end_year=2023) 

        # Call function 2 to create folders given a list
        folder_names = ['data-csv', 'data-excel', 'data-json']
        create_folders_from_list(folder_names)     

        # Call function 3 to create folders using list comprehension
        folder_names = ['csv', 'excel', 'json']
        prefix = 'output-'
        create_prefixed_folders_using_list_comprehension(folder_names, "dir_")     

        # Call function 4 to create folders periodically using while
        duration_secs:int = 5  # duration in seconds
        create_folders_periodically(duration_secs)     

        # Call function 5 to create standardized folders, no spaces, lowercase
        create_standardized_folders(REGIONS, to_lowercase=True, remove_spaces=True)       
    else:
        #placeholder for else case
        pass
        
    
    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()