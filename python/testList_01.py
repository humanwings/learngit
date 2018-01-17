#from MyPackage.mycommon import * 
from MyPackage import mycommon
#from commondist import *

cast = ["00","01","02","03",["0401","0402",["040301","040302","040303"]],"05",["0601","0602"]]

mycommon.printlist(cast,0)

front = cast.copy()    #浅层copy
cast.append("07")
cast[4].append("0404")
print(cast)
print(front)

cast.extend(front)
print(cast)