# The Russian Peasant''s Algorithm Test

# Multiply two numbers together.
# Requirements: multiply by 2, divide by 2, remove even rows, and Add numbers

# AKA = Mediation and Duplication Method

# Inputs -> two numbers
# Output -> the solution to those two numbers multiplied together
#           using the Russian Peasant's Algorithm

import time

CACHE = {}                              # Cache hash table as dictionary

def russian(a,b):                       # Russian Peasan'ts Algorithm
    key = (a,b)                         # Define Key needed for CACHE
    if key in CACHE:                    # Adding Keys into Cache
        z = CACHE[key]
    else: 
        x = a; y = b                    # Semicolon -> Compound Statement
        z = 0                           # Acumulator
        while x > 0:                    # While loop Begins
            if x % 2 == 1: z = z + y    # Module operator
            y = y << 1                  # Shift Binary over to left
            x = x >> 1                  # Shift Binary over to right
            CACHE[key] = z              # Cached Acumulator
        return z                        # Return Z

def testRussian():
    startTime = time.time()
    print(russian(357,16))              # Without Cache
    print('Russian Algorithm took %f seconds' % (time.time()-startTime))

    print(russian(357,16))              # With Cache
    print('Russian Algorithm took %f seconds' % (time.time()-startTime))
    
    assert russian (357,16) == 5712

testRussian()