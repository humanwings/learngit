print(__name__)

print(__package__)

from ..sub1 import sub1m1

innervalue = "sub2m1.innervalue"

def getvalue():

    return "sub2m1.getvalue"

print(sub1m1.innervalue)

print(sub1m1.getvalue())