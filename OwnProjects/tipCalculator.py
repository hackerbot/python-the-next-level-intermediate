import sys

def tip():
    '''
    Calculates tip amount depending on the total cost of the meal and your
    desired generosity in percentile
    '''
    print('How much was your meal?')
    
    price = int(sys.stdin.readline())
    print('What percemt do you want to tip thme? Leave off any periods or percent signs')
   
    tip = int(sys.stdin.readline())
    finalTipAmount = price * (tip / 100)
    print('You will want to tip them %s' % finalTipAmount + 'dollars')

tip()