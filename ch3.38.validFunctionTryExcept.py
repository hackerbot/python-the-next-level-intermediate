# Function we will create:

#    - solve    --> Runs thru all possible combinations of testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid --> Tests our filled_in String

import re

def valid(formula):
    '''
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    '''
    try:
        ## your code here
        return not re.search(r'\b0[0-9', formula) and eval(formula) is True
    except ArithmeticError:
        ## your code here
        return False
    except:
        ## your code here
        return False
print(valid('1+1==2'))