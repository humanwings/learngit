import numpy as np
from collections import Counter 

tempArray = np.random.randint(0,10,size=(80,100))

tempList = tempArray.tolist()

result = Counter()

for a in tempList :
    result.update(a)

print(result)