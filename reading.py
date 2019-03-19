# Functions for reading tables and databases

import glob
from database import *

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# YOU DON'T NEE D TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING

# Write the read_table and read_database functions below


def read_table(file_name):
    ''' (str) -> Table
    this function takes a filename as its parameter and returns an object
    of type Table that contains the data in the csv file
    '''
    # open the file
    file = open(file_name, 'r')
    # read all the lines of the file into a list
    file_list = file.readlines()
    # split every line in the file into a list of its words and strip the
    # newline character
    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip('\n')
        file_list[i] = file_list[i].split(',')
    # use the zip method to transpose the elements of the nested lists into
    # tuples and then use map to convert the tuples into lists again
    # but first we pop out the first list in the big list in order to have the
    # keys for the dictionary that will be created using the Table class
    keys_list = file_list.pop(0)
    file_list = list(zip(*file_list))
    file_list = list(map(list, file_list))
    # create an object using the table class
    result = Table()
    # use the add_columns method and apply the keys_list and file_list as its
    # parameters and let it be the result
    result.add_columns(keys_list, file_list)
    return result


def read_database():
    '''() -> Database
    this function takes no parameter and returns an object of type Database
    that stores all the csv files in the current directory in Database form
    '''
    # use glob to import the names of all the csv files in the directory
    # into a list
    file_list = glob.glob('*.csv')
    # create a variable of type Database
    result = Database()
    # create an empty table that will contain the Table objects of the csv
    # files
    tables_list = []
    # use elemental loop in file_list
    for element in file_list:
        # append the returned result of calling read_table function on the
        # element (the result is a table object)
        tables_list.append(read_table(element))
    # loop through the file list to strip the '.csv' from the filenames
    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip('.csv')
    # use the add_key_value method for Database by inserting the file_list
    # and the table_list as the two parameters
    result.add_key_value(file_list, tables_list)
    return result
