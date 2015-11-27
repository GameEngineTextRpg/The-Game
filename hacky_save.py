# a file that can be used to save variables
# NOTE: unsafe, as the savefile could be configured to wipe disk
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
            self.varNames.append(line.split(chr(7))[0])
        openfile.close()

    # save a variable to the file
    # varname is the name of the variable, and val is its value
    def put (self, varname, val):
        
        # if the variable is a string, adds single quotes to differentiate it.
        if type(val) is str:
            val = '\'' + val + '\''

        # creates the line
        line = varname + chr(7) + str(val) + chr(7) + '\n'

        # replaces existing variable with same name if it already exists, otherwise creates new variable
        if varname in self.varNames:
            self.contents[self.varNames.index(varname)] = line
        else:
            self.contents.append(line)
            self.varNames.append(varname)

    # gets a variable, list, or dict from the savefile
    # varname is the name of the variable
    def get (self, varname):

        # tries to fix any user messing around
        try:
            # finds the line that the variable is in, then splits it into a list, finds its value, and evaluates it, returns it
            return eval(self.contents[self.varNames.index(varname)].split(chr(7))[1])
        except SyntaxError:
            return None

    # truncates the file and writes new contents
    def write (self):
        openfile = open(self.filename, 'w')
        openfile.truncate()
        openfile.writelines(self.contents)
        openfile.close()
