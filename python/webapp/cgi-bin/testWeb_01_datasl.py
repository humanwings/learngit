import os
import sys
import pickle
import commondist

filelist = ["D:\doc\python\HeadFirstPythonFiles\james.txt",
            "D:\doc\python\HeadFirstPythonFiles\julie.txt",
            "D:\doc\python\HeadFirstPythonFiles\mikey.txt",
            "D:\doc\python\HeadFirstPythonFiles\sarah.txt"]

datafile = "D:\doc\python\HeadFirstPythonFiles\web_datafile_01.pickle"

def init_web_data():

    webdata = {}

    for filename in filelist:
        filedata = commondist.Runner(filename)
        webdata[filedata.name] = filedata

    try:
        with open(datafile, "wb") as pf:
            pickle.dump(webdata, pf)
    except IOError as err:
        print("IOError error ", err)
    except pickle.PickleError as err:
        print("PickleError error ", err)
    
    return webdata

def get_web_data():

    try:
        with open(datafile, "rb") as pf:
            webdata = pickle.load(pf)
    except IOError as err:
        print("IOError error ", err)
    except pickle.PickleError as err:
        print("PickleError error ", err)

    return webdata

def test():
    data = init_web_data()
    for one in data:
        print(data[one].name ," : ",data[one].info)
    
    data = get_web_data()
    for one in data:
        print(data[one].name ," : ",data[one].info)
    

test()