# 2^3 = 8
# pow(2, 3) -> 8
# pow(4, 0) -> 1

def pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp == 2:
        return base*base
    return pow(base,exp-1)*base
 
print(pow(2,3))

# 2^3 = 8
# pow2(2, 3) -> 8
# pow2(4, 0) -> 1

def pow2(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp > 1:
        list = exp*[int(base)]
    total = 1
    for each in list:
        total *= each
        print(total)
print(pow2(2,3))