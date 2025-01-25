"""
Module: kamidenny_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Kami Denny

Date: 2025-01-24
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
import pathlib
import time
from datetime import datetime

# Import local modules
import utils_kamidenny


#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)


#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:

    '''
    Purpose:
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).

    Returns:
    None
    '''
    for year in range(start_year, end_year + 1):            # Loop through the range of years
        folder_year = data_path.joinpath(str(year))         # Create a path object for the year
        folder_year.mkdir(parents=True, exist_ok=True)      # Create the folder if it doesn't exist
        print(f"Created folder: {folder_year}")

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}") 


#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, make_lowercase: bool = False, replace_spaces: bool = False, add_date: bool = False) -> None:
    '''
    Purpose:
    Create folders from a list of names.
    
    Arguments:
    folder_list -- A list of folder names to create.
    make_lowercase -- If True, convert folder names to lowercase.
    replace_spaces -- If True, replace spaces with underscores.
    add_date -- If True, add today's date to the end of folder names.

    Returns:
    None
    '''

    #Define today's date
    today_date = datetime.now().strftime("%Y%m%d")

    for folder_name in folder_list:
        if make_lowercase:
            folder_name = folder_name.lower()               # Convert to lowercase
        if replace_spaces:
            folder_name = folder_name.replace(" ", "_")     # Replace spaces with underscores
        if add_date:
            folder_name = f"{folder_name}_{today_date}"     # Add today's date to the end of the folder name
        
        folder_name = data_path.joinpath(folder_name)       # Create a path object for the folder
        folder_name.mkdir(parents=True, exist_ok=True)      # Create the folder if it doesn't exist
        print(f"Created folder: {folder_name}")

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, make_lowercase={make_lowercase}, replace_spaces={replace_spaces}, add_date={add_date}")


#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-', or 'final-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Purpose:
    # Create folders from a list of names with a prefix.
    
    Arguments:
    folder_list -- A list of folder names to create.
    prefix -- A prefix to add to each folder name.

    Returns:
    None
    '''

    for folder_name in folder_list:
        prefix_folder_name = f"{prefix}{folder_name}"              # Add the prefix to the folder name
        folder_name = data_path.joinpath(prefix_folder_name)       # Create a path object for the folder
        folder_name.mkdir(parents=True, exist_ok=True)             # Create the folder if it doesn't exist

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders where prefix={prefix}, and folder_list={folder_list}")


#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int, max_folders: int) -> None:
    '''
    Purpose:
    Create folders periodically with a delay between each folder.
    
    Arguments:
    duration_seconds -- The number of seconds to wait between creating each folder.
    max_folders -- The maximum number of folders to create.

    Returns:
    None
    '''
    folder_number = 0                                                # Initialize the folder number
    while folder_number < max_folders:                               # Loop until the folder number reaches the maximum
        folder_name = data_path.joinpath(f"folder_{folder_number}")  # Create a path object for the folder
        folder_name.mkdir(parents=True, exist_ok=True)               # Create the folder if it doesn't exist
        print(f"Created folder: {folder_name}")                      # Print the folder name
        folder_number += 1                                           # Increment the folder number
        time.sleep(duration_seconds)                                 # Wait for the specified duration

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}, max_folders={max_folders}")


#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_kamidenny.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'final-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    max_folders:int = 6    # maximum number of folders to create
    create_folders_periodically(duration_secs, max_folders)
    
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, make_lowercase=True, replace_spaces=True, add_date=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
