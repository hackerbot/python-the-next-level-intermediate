# randomly shuffle a list

import random
import xxlimited

list = [1,2,3,4,5,6,7,8,9,0]
print(list)

random.shuffle(list)
print(list)

# randomly pick one object and switch its position with the next object
list = [1,2,3,4,5,6,7,8,9,0]
x = random.choice(list)
randomPair = list[(x):(x+2)]
print(randomPair)
reversePair = randomPair[::-1]
print(reversePair)
list2 = list[:x] + reversePair + list[x+2:]
print(list2)

list = [1,2,3,4,5,6,7,8,9,0]
tempObj = list[x]
list[x] = list[x+1]
list[x+1] = tempObj
print(list)