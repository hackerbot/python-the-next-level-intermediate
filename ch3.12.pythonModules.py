# Modules

# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended

# Will search for built-in module then look at your files.

# We will use it to represent our 3 Different App Computers

import computer1, computer2
import computer3 as com3

computer1.printName()
computer2.printName()
com3.printName()

from Database import utils as dbUtils
from Handlers import utils as hUtils
# Databse --> utils.py
# Handlers --> utils.py