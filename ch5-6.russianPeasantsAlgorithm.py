# The Russian Peasant''s Algorithm
# Been Around for long time. (17th Century B.C.)

# Multiply two numbers together.
# Requirements: multiply by 2, divide by 2
# remove even rows, and Add numbers

# AKA = Mediation and Duplication Method

# example 1
# 24 x 16 = ?
# 
# X 12 x 32 = ?
# X 6    64
# 3    128
# 1    256
# ---------
# 128 + 256 = 384

# example 2
# 1238 x 13 = 3094

# 119     26
# 59      52
# 29      14
# x 14        208
# 7       416
# 3       832
# 1       1664
# ----------
# 3094

print(10 % 2)
print(3 % 2)

x = 1
y = 2
print(x << 1, y >> 1)

# Inputs -> two numbers
# Output -> the solution to those two numbers multiplied together
#           using the Russian Peasant's Algorithm

def russian(a,b):                   # Russian Peasan'ts Algorithm
    x = a; y = b                    # Semicolon -> Compound Statement
    z = 0                           # Acumulator
    while x > 0:                    # While loop Begins
        if x % 2 == 1: z += y       # Module operator
        y = y << 1                  # Shift Binary over to left
        x = x >> 1                  # Shift Binary over to right
    return z                        # Return Z

print(russian(357,16))
print(russian(16,24))

# 17 in base 2: 1001 = 16 + 1 = 17            10001
#               >> 1                    << 1
#               1000 = 8            100010 = 32+ 2 = 34