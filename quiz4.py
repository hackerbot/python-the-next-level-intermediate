# What will get Printed after running this code?
d = lambda p: p * 2
t = lambda p: p * 3
x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)
# 7
# 12
# 24
# 36
# 48