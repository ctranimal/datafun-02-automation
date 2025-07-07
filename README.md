# datafun-02-automation
Implemented all 5 functions as described in starter code provided in datafun_02_automation project.

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################
def create_folders_for_range(start_year: int, end_year: int) -> None

#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################
def create_folders_from_list(folder_list: list) -> None

#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################
def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################
def create_folders_periodically(duration_seconds: int) -> None

#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################
def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None
