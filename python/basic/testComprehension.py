symbols = '$¢£¥€¤'
print([ord(symbol) for symbol in symbols])

listA = [1,2,3,4]
listB = [10,20,30,40]

print([x*y for x in listA for y in listB])

tupleA = ((x, y) for x in listA for y in listB)

print(tupleA)