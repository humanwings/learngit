def printlist(mylist,tab=-1) :
    for item in mylist:
        if isinstance(item,list):
            if tab > -1 :
                printlist(item,tab + 1)
            else:
                printlist(item)
        else:
            for num in range(tab):
                print("\t", end="")
            print(item)

class Runner:

    def __init__(self,filename):
        try:
            with open(filename) as fn :
                self.name = filename.split("\\") [-1].split(".")[0]
                self.years = 20
                #self.runnerinfo = fn.readline().strip().split(",")
                self.info = [self.replacechar(thestr) for thestr in fn.readline().strip().split(",")]
        except IOError as ie:
            print("IOError" ,ie)
        except IndexError as ie:
            print("IndexError" ,ie)

    def getTop3(self):
        mylist = [self.replacechar(thestr) for thestr in self.info]        #列表推导
        mylist.sort()
        return mylist[0:3]

    def replacechar(self,thestr):
        if ":" in thestr:   
            thestr = thestr.replace(":",".")
        elif "-" in thestr:
            thestr = thestr.replace("-",".")
        return thestr
    