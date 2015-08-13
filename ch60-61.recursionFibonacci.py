# # def foo(n):
# #     if n == 1:
# #         return n
# #     else:
# #         foo(n-1)
# 
# # 1, 1, 2, 3, 5, 8, 13, 21, 34... etc
# 
def Fib(n):
    if n == 1 or n == 2:
        return 1
    return Fib(n-1) + Fib(n-2)
 
print(Fib(5))


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
# pow(2, 3) -> 8
# pow(4, 0) -> 1


def pow(base, exp):
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
print(pow(2,3))