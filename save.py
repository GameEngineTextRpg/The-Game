# a file that can be used to save variables
# 
# USAGE:
# 1. create an object of <savefile> = saveFile(<filename>)
# 2. when accessing the file to read or write, use <savefile>.start()
# 3a. to save a variable, use <savefile>.put(<variable_name>, <variable_value>)
# 3b. to read a variabel, use <savefile>.get(<variable_name>)
# 4. to finish saving the variables, use <savefile>.write()
class saveFile (object):

    # create the savefile
    # filename is the name of the file
    def __init__ (self, filename):
        self.filename = filename

    # opens the file and gets its contents as well as the names of all of the variables
    def start (self):
        openfile = open(self.filename)
        self.contents = openfile.readlines()
        self.varNames = []
        for line in self.contents:
            self.varNames.append(line.split(' ')[1])
        openfile.close()

    # save a variable to the file
    # varname is the name of the variable, and val is its value
    def put (self, varname, val):

        # finds the variable type
        varType = type(val)

        # enters as a dict if dict
        if varType is dict:
            line = 'dict ' + varname + ' '
            for entry in val:
                line += (getType(type(entry)) + str(entry).replace(' ', '_') + ' ' + getType(type(val[entry])) + str(val[entry]).replace(' ', '_') + ' ')

        # enters as a list if list
        elif varType is list:
            line = 'list ' + varname + ' '
            for entry in val:
                line += (getType(type(entry)) + str(entry).replace(' ', '_') + ' ')

        # enters as a single if not list or dict
        else:
            line = 'single ' + varname + ' ' + getType(varType)
            line += (str(val).replace(' ', '_') + ' ')

        # puts a newline at the end
        line += '\n'

        # replaces existing variable with same name if it already exists, otherwise creates new variable
        if varname in self.varNames:
            self.contents[self.varNames.index(varname)] = line
        else:
            self.contents.append(line)
            self.varNames.append(varname)

    # gets a variable, list, or dict from the savefile
    # varname is the name of the variable
    def get (self, varname):

        # finds the line that the variable is in, then splits it into a list
        line = self.contents[self.varNames.index(varname)].split(' ')
        sizeType = line[0]

        # if the variable is a dictionary, configures and returns the dictionary
        if sizeType == 'dict':
            cur_dict = {}
            for i in range((len(line) - 2) / 4):
                cur_dict[putType(line[4 * i + 2], line [4 * i + 3])] = putType(line[4 * i + 4], line[4 * i + 5])
            return cur_dict

        # if the variable is a list, configures and returns the list
        elif sizeType == 'list':
            cur_list = []
            for i in range((len(line) - 2) / 2):
                cur_list.append(putType(line[2 * i + 2], line[2 * i + 3]))
            return cur_list
        
        # if the variable is a single, configures and returns the single
        elif sizeType == 'single':
            return putType(line[2], line[3])

    # truncates the file and writes new contents
    def write (self):
        openfile = open(self.filename, 'w')
        openfile.truncate()
        openfile.writelines(self.contents)
        openfile.close()

# returns the variable type as a string
# varType is the type(var)
def getType (varType):
    if varType is int:
        string = 'int '
    elif varType is str:
        string = 'str '
    elif varType is long:
        string = 'long '
    elif varType is float:
        string = 'float '
    return string

# returns the string as its original variable
# strType is the variable's type as a string, and strVal is the variable's value as a string
def putType (strType, strVal):
    if strType == 'int':
        return int(strVal)
    elif strType == 'str':
        return strVal.replace('_', ' ')
    elif strType == 'long':
        return long(strVal)
    elif strType == 'float':
        return float(strVal)
