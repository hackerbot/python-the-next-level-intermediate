import fakeDatabase

CACHE = {}

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
    print(a,b)
            

def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    key = 'lastFive'
    lastFiveList = CACHE.get(key)
    if lastFiveList:
        if len(lastFiveList) >= 5:
            ## The list already had 5 items in it
            newList = lastFiveList[1:]
            newList.append('{}x{}={}'.format(a,b,result))
            CACHE[key] = newList
        else:
            ## The list had less than five items
            lastFiveList.append('{}x{}={}'.format(a,b,result))
            CACHE[key] = lastFiveList
    else:
        ## There was not a Cache so create one
        CACHE[key] = ['{}x{}={}'.format(a,b,result)]

def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    """
    cacheKey = (a,b)
    if cacheKey in CACHE:
        print(cacheKey)
    else:
        result = fakeDatabase.russian(a, b)
        updateLastMultiplied(a, b, result)
        CACHE[cacheKey] = result
        print('Latest Result: {}'.format(result))
        lastMultipliedHandler()

if __name__ == '__main__':
    multiplyHandler(2, 6)
    multiplyHandler(5, 6)
    multiplyHandler(10, 6)
    multiplyHandler(23, 6)
    multiplyHandler(4, 6)
    multiplyHandler(11, 6)
    multiplyHandler(200, 6)
    