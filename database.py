class Table():
    '''A class to represent a SQuEaL table'''
    def __init__(self):
        ''' this method initiates an object that is an empty dictionary that
        can hold data later using the set_dict method
        '''
        self._table_dict = {}

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        self._table_dict = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        return self._table_dict

    def add_columns(self, keys, cells):
        ''' (Table, list of str, list of list) -> dict
        this function takes a list of the names of the columns and a list of
        lists that has the data in the cells of each column
        '''
        # use the range loop to create new dictionary key:value combinations
        # by making every element from the keys list as as a key and the value
        # is a list of all the cells in column
        for i in range(len(cells)):
            self._table_dict[keys[i]] = cells[i]
        return self._table_dict

    def delete_row(self, index):
        '''(Table, int) -> Table
        this method deletes a row given the index of that row
        '''
        # pop the element from the value of every element in the dictionary
        # at the given index
        for element in self._table_dict:
            list1 = self._table_dict[element]
            list1.pop(index)

    def get_column(self, key):
        return self._table_dict[key]


class Database():
    '''A class to represent a SQuEaL database'''
    def __init__(self):
        ''' this method initiates an object that contains a dictionary that
        will hold the database information
        '''
        self._database_dict = {}

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        self._database_dict = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        return self._database_dict

    def add_key_value(self, keys, values):
        ''' (Database, list, list of Table) -> Database
        this method adds key-value combinations to the database dictionary
        where the keys are the table names and the values Table objects that
        hold the table
        '''
        for i in range(len(keys)):
            self._database_dict[keys[i]] = values[i]
        return self._database_dict

    def get_tables(self, table_name):
        return self._database_dict[table_name]
