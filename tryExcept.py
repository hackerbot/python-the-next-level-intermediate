# Try
# Except

userDefined = 'b'

# try:
#     a = int(userDefined)
# except ValueError:
#     a = int(1)
# except Exception:
#     a = int(0)
#  finally:
#     print(a)

class MyException(Exception):
    pass

try:
    #a = int(userDefined)
    raise MyException('My Exception Error!')
except ValueError:
    a = int(1)
    print('Error', a)
except MyException as e:
    a = int(0)
    print('Error', a, e)
except:
    print('Error -1')    
else:
    print(a)