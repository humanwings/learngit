import pickle
import mycommon

cast = ["01","02","03",["0401","0402",["040301","040302","040303"]],"05",["0601","0602"]]

pfile = "D:\doc\python\HeadFirstPythonFiles\pickle_test_01.pickle"

try:
    with open(pfile,"wb") as pf:
        pickle.dump(cast,pf)
except IOError as err:
    print("IOError error " , err)
except pickle.PickleError as err:
    print("PickleError error " , err)

try:
    with open(pfile,"rb") as pf:
        new_cast = pickle.load(pf)
except IOError as err:
    print("IOError error " , err)
except pickle.PickleError as err:
    print("PickleError error " , err)

mycommon.printlist(new_cast,0)
