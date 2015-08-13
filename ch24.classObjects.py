## Python Class Objects

## class ClassName:
##     <statement-1>

## Class objects support two kinds of operations: 
##                  - attribute references ( <class>.<attribute> )
##                  - instantiation ( <class>() )

## Many classes like to create objects with instances customized to a
## specific initial state.  ( def __init__(self): )

## Methods may call other methods by using method attributes of the self argument

## Classes support inheritance  ( class DerivedClassName(BaseClassName): )

## There is a convention that is followed by most Python code: a name prefixed
##   with an underscore (e.g. _spam) should be treated as a non-public part of
##   the API 
class BaseClass:
    def c(self):
        return 3
    
class TestClass(BaseClass):
    def __init__(self):
        self.b = 2
        self._d = 4
    def add(self):
        pass
    def plusOne(self):
        c = self.c
        return self.add()+1

c = TestClass()
c.a = 1

print c.a
print c.b
print c.c()
print c._d
    


