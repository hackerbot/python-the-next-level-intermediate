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