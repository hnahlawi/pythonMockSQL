from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard
#  processes them, and uses the below function to output csv results

# create global variables to avoid hardcoding

# full query length
q_length = 6
# table names index in query
tables_qindex = 3
# column names index in query
columns_qindex = 1
# constraints index in query
constraints_qindex = 5


def num_rows(table):
    ''' (Table) -> int
    this function returns the number of rows in a Table object with the table
    object being its parameters
    >>> a = Table()
    >>> a.set_dict({'name':['antony','micheal','bob','paul'],
    ... 'grades':[76,85,65,43]})
    >>> num_rows(a)
    4
    '''
    # get the dictionary of the table
    dictionary = table.get_dict()
    # create a copy of the dictionary
    dictionary2 = dictionary.copy()
    # create a list of the keys in the dictionary
    list1 = list(dictionary2.keys())
    # the result is the length of any value of any key
    # arbitrarily choose the first key from the list
    result = len(dictionary2[list1[0]])
    return result


def get_list(table):
    ''' (Table) -> list of list
    this function takes a Table as its parameters and returns the values of the
    dictionary in Table as a list of lists
    Examples:
    the last command finds the difference between the two lists b and c
    >>> a = Table()
    >>> a.set_dict({'name':['antony','micheal','bob','paul'],
    ... 'grades':[76,85,65,43]})
    >>> b = get_list(a)
    >>> c = [['antony', 'micheal', 'bob', 'paul'], [76, 85, 65, 43]]
    >>> [x for x in b if not x in c]
    []
    '''
    # create a variable that holds the dictionary of the table using get_dict
    # method
    dictionary = table.get_dict()
    result = []
    # loop through every element in the dictionary and append every value to
    # the new_list
    for element in dictionary:
        result.append(dictionary[element])
    return result


def first_table(table, multiples):
    ''' (Table, int) -> list of list
    this function takes a Table object and a number as its parameters and
    returns a list of all of the values in its dictionary in which each element
    in every list (value) in the table is multiplied by the number specified
    Examples:
    the last command finds the difference between the two lists b and c
    >>> a = Table()
    >>> a.set_dict({'name':['alex', 'bob'], 'grade':[76, 85]})
    >>> b = first_table(a, 2)
    >>> c = [['alex', 'alex', 'bob', 'bob'], [76, 76, 85, 85]]
    >>> [x for x in b if not x in c]
    []
    '''
    # get the list of the table (list of values) given
    new_list = get_list(table)
    # create an empty list
    result_list = []
    # loop through every element in the new_list
    for element in new_list:
        # create a new list that contains the multiplication of every element
        element_list = []
        # loop through every element(inner list) and multiply the elements
        # and add it to the element_list
        for i in range(len(element)):
            element_list += ([element[i]] * multiples)
        # append the element_list (the multiplied column) to the result_list
        result_list.append(element_list)
    return result_list


def second_table(table, multiples):
    '''(Table, int) -> list of list
    this function takes a Table object and a number as its parameters and
    returns a list of all of the values in its dictionary in which the list is
    multiplied by the specified number
    '''
    # get the list of values of the table object by using the get_list function
    new_list = get_list(table)
    # multiply every element in the list by the specified number
    for i in range(len(new_list)):
        new_list[i] = new_list[i] * multiples
    return new_list


def get_column_names(table1, table2):
    ''' (Table, Table) -> list
    this function returns a list of the column names of two Table objects
    (dictionary) given two Table objects as its parameters
    Examples:
    the last command finds the difference between the two lists names and c
    >>> a = Table()
    >>> b = Table()
    >>> a.set_dict({'name':['Alex', 'Bob'], 'grade':[74, 54]})
    >>> b.set_dict({'show':['arrow', 'the flash'], 'year':[2012, 2014]})
    >>> names = get_column_names(a, b)
    >>> c = ['name', 'show', 'year', 'grade']
    >>> [x for x in names if not x in c]
    []
    '''
    # get the dictionaries for the two tables
    dict1 = table1.get_dict()
    dict2 = table2.get_dict()
    # get a list of the keys of the two dictionaries
    list1 = list(dict1.keys())
    list2 = list(dict2.keys())
    # return the sum of both lists
    return list1 + list2


def cartesian_product(table1, table2):
    '''(Table, Table) -> Table
    do the cartesian product of two tables by multiplying every row from the
    first table with every row form the second table
    >>> a = Table()
    >>> b = Table()
    >>> a.set_dict({'name':['hadi','john'],'grade':[46,10]})
    >>> b.set_dict({'year':[2013,2014],'column2':['red','blue']})
    >>> c =  cartesian_product(a,b)
    >>> c.get_dict() == {'name': ['hadi', 'hadi', 'john', 'john'],
    ... 'year': [2013, 2014, 2013, 2014], 'grade': [46, 46, 10, 10],
    ... 'column2': ['red', 'blue', 'red', 'blue']}
    True
    '''
    # get the two dictionaries of the two tables given
    dict1 = table1.get_dict()
    dict2 = table2.get_dict()
    # get the lists of the keys of the two tables
    list1 = list(table1.get_dict().keys())
    list2 = list(table2.get_dict().keys())
    # add the two lists together
    total_keys = list1 + list2
    # get the final list of values by using the functions for the first table
    # and the second table and add them
    final_list = first_table(table1, num_rows(table2))\
        + second_table(table2, num_rows(table1))
    # create a result table and add the columns to it using the add_columns
    # method
    result = Table()
    result.add_columns(total_keys, final_list)
    return result


def constraint_eval(constraint_str, table):
    ''' (str , Table) -> list of bool
    this function takes a table and a constraint as its parameters and returns
    a list of booleans that has the evaluations of the constraint for every
    cell in the table in the column specified in the constraint
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraint_eval("column1>'2000'",a)
    [True, False]
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraint_eval("column1='2000'",a)
    [False, False]
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraint_eval("column1='2013'",a)
    [True, False]
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraint_eval('column1=column2',a)
    [False, True]
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraint_eval('column1>column2',a)
    [True, False]
    '''
    # index of the first part of the constraint after splitting
    # the constraint str
    part1_index = 0
    # index of the second part of the constraint after splitting
    # the constraint str
    part2_index = 1
    # if there is an equal operator in the constraint string we replace it by
    # two equal signs and we split the string at the double equal sign
    # and we store the operator in a variable
    if '=' in constraint_str:
        constraint_str = constraint_str.replace('=', '==')
        list1 = constraint_str.split('==')
        operator = '=='
    # otherwise we split the constraint string at the greater than sign
    # and store the operator
    else:
        list1 = constraint_str.split('>')
        operator = '>'
    # part1 of the final_constraint is the name of the columns in list1 which
    # contains the constraints two parts
    part1 = table.get_column(list1[part1_index])
    # get the dictionary for the table and create an empty list
    table_dict = table.get_dict()
    result = []
    # if the second part of the constraint (part after the operator) is
    # one of the keys in the dictionary
    if list1[part2_index] in list(table_dict.keys()):
        # part2 is the column values of the second part of list1
        part2 = table.get_column(list1[part2_index])
        # use range loop using the length of part1
        for i in range(len(part1)):
            # if part1[i] (first column cell)
            # is not a digit add quotation marks to make the evaluation of
            # strings possible otherwise keep it as it is
            if not part1[i].isdigit():
                part1_cell = '"' + part1[i] + '"'
            else:
                part1_cell = part1[i]
            # if part2[i] (second column cell) is not a digit add quotation
            # marks to make the evaluation of strings possible
            # otherwise keep it as it is
            if not part2[i].isdigit():
                part2_cell = '"' + part2[i] + '"'
            else:
                part2_cell = part2[i]
            # get the final constraint and evaluate it
            final_constraint = part1_cell + operator + part2_cell
            result.append(eval(final_constraint))
    # if the second part of the constraint is not a column
    else:
        # strip the quotation marks from the second part of the constraint
        list1[part2_index] = list1[part2_index].strip("'")
        # loop through the length of part1
        for i in range(len(part1)):
            # if part1[i](cell in first column)
            # is not a digit add quotation marks to make the
            # evaluation of strings possible otherwise keep it as it is
            if not part1[i].isdigit():
                part1_cell = '"' + part1[i] + '"'
            else:
                part1_cell = part1[i]
            # if list1[part2_index] (value given in constraint) is not a digit
            # add quotation marks to make the evaluation of strings possible
            # otherwise keep it as it is
            if not list1[part2_index].isdigit():
                part2_cell = '"' + list1[part2_index] + '"'
            else:
                part2_cell = list1[part2_index]
            # find the final constraint and append its evaluation to the result
            # list
            final_constraint = part1_cell + operator + part2_cell
            result.append(eval(final_constraint))
    return result


def constraints_eval(constraint_list, table):
    '''(list of str, Table) -> list of list of bool
    this function takes a list of constraints and a Table object as its
    parameters and returns a list that contains lists of booleans where each
    list represents the evaluations of a constraint on every cell in the column
    specified
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraints_eval(["column1>'2000'","column1=column2"],a)
    [[True, False], [False, True]]
    >>> a = Table()
    >>> a.set_dict({'column1':['2013', '1994'], 'column2':['2012', '1994']})
    >>> constraints_eval(["column1>'1990'","column1=column2"],a)
    [[True, True], [False, True]]
    '''
    # create an empty list
    result = []
    # loop through every element of the constraint list and call the
    # constraint_eval function on every element and the table given
    for element in constraint_list:
        result.append(constraint_eval(element, table))
    return result


def print_csv(table):
    '''(Table) -> NoneType
    Print a representation of table.
    '''
    dict_rep = table.get_dict()
    columns = list(dict_rep.keys())
    print(','.join(columns))
    rows = num_rows(table)
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))


def run_query(database, query):
    ''' (Database, str) -> Table
    this function runs queries on files in a database and returns a Table
    object given a Database object and a query in proper syntax
    REQ: query syntax should be as follows
    select (column names)(1) from (tables)(2) where (constraint)(3)
    (1): column names are separated by commas and no spaces (* stands for all
    columns)
    (2): tables are file names separated by commas and no spaces or extensions
    (3): constraint has one of four forms:
    1- column_name1>'value'
    2- column_name1='value'
    3- column_name1>column_name2
    4- column_name1=column_name2
    Example:
    >>> a = Table()
    >>> b = Table()
    >>> a.set_dict({'name':['hadi','john'],'grade':['46','10']})
    >>> b.set_dict({'year':[2013,2014],'column2':['76','10']})
    >>> c = Database()
    >>> c.set_dict({'a':a,'b':b})
    >>> result = run_query(c,'select column2 from a,b where column2=grade')
    '''
    # split the query
    query_list = query.split()
    table_names = query_list[tables_qindex].split(',')
    # create a list that contains the table names in a query using split
    table_obj_list = []
    # get the table objects from the database
    for element in table_names:
        table_obj_list.append(database.get_tables(element))
    # the intial table is the first table in the tables list
    # use range loop to do cartesian product for all the tables until all the
    # tables are done
    result_table = table_obj_list[0]
    for i in range(len(table_obj_list) - 1):
        # every cartesian product is the product of result_table
        # with the table that
        # has the index i + 1 in the tables obj list
        result_table = cartesian_product(result_table, table_obj_list[i + 1])
    # if the query has full length (has a where token)
    if len(query_list) == q_length:
        # get a list of all the given constraints using split
        constraints = query_list[constraints_qindex].split(',')
        # get the list of list of booleans using by calling the
        # constraints_bools function on the list of constraints result_table
        constraints_bools = constraints_eval(constraints, result_table)
        # for every element in constraint_bools (every constraint given)
        for element in constraints_bools:
            i = 0
            # use while loop while i is less than the number of rows in
            # result_table
            while i < num_rows(result_table):
                # if a boolean value is false (does not satisfy a constraint)
                if not element[i]:
                    # delete the row
                    result_table.delete_row(i)
                    # remove the boolean from the list of list of booleans
                    element.pop(i)
                    # decrease i by 1 because every component of element is
                    # shifted one position down because of pop and because of
                    # deleting rows (therefore we don't skip testing a row)
                    i -= 1
                # increase i by 1 for every iteration
                i += 1
    # create a result table
    final_table = Table()
    result_columns = []
    # if the columns part of the query is a * it means all columns
    if query_list[columns_qindex] == '*':
        # create a list of all the columns by getting the keys of the dict
        # in table1
        columns = list(result_table.get_dict().keys())
    # otherwise we create a list of all the columns given using split
    else:
        columns = query_list[columns_qindex].split(',')
    # for every element in columns we append the corresponding value in
    # result_table
    # dictionary in order to get a list of all the values we need
    for element in columns:
        result_columns.append(result_table.get_column(element))
    # use add_columns method and use the list of column names (columns) and the
    # list of column values (result_columns) as the parameters for the method
    final_table.add_columns(columns, result_columns)
    return final_table

if(__name__ == "__main__"):
    query = input("Enter a SQuEaL query, or a blank line to exit:")
    c = read_database()
    a = run_query(c, query)
    print_csv(a)
