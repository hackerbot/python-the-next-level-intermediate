# What will get printed when running this code?
def dostuff(param1, **param2):
print(type(**param2))
dostuff('capitals', Arizona='Phoenix', California='Sacramento', Texas='Austin')
# True
# list
# tuple
# California
# 'Sacramento'
# dict
# str