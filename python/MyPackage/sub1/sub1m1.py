print(__name__)

print(__package__)

from . import sub1m2

innervalue = "sub1m1.innervalue"

def getvalue():

    return "sub1m1.getvalue"

print(sub1m2.innervalue)

print(sub1m2.getvalue())