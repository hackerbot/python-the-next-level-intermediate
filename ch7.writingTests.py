# testing

# WHY?
# To Understand our Code Better
# To learn when we made a mistake
# To know when we are finished
# To ensure any future programe changes/additions don't break our programe

def adding(a,b):
    return a + b

def testAdding():
    assert adding(3,4) == 7
    assert adding(3,2) != 6
    assert adding(99,49) == 148
    
    return 'All Tests Pass for function adding()'

print(testAdding())