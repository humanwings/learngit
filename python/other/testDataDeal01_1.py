import os
import sys
import mycommon

jamesfile = "D:\doc\python\HeadFirstPythonFiles\james.txt"
juliefile = "D:\doc\python\HeadFirstPythonFiles\julie.txt"
mikeyfile = "D:\doc\python\HeadFirstPythonFiles\mikey.txt"
sarahfile = "D:\doc\python\HeadFirstPythonFiles\sarah.txt"

def replacelist(mylist):
    #for index in range(len(mylist)):
    #    mylist[index] = replacechar(mylist[index])
    #return mylist    
    return [replacechar(thestr) for thestr in mylist]        #列表推导

def replacechar(thestr):
    if ":" in thestr:
        thestr = thestr.replace(":",".")
    elif "-" in thestr:
        thestr = thestr.replace("-",".")
    return thestr

def gethighscore(mylist):
    highscore = ["","",""]
    #if highscore[0] == "":
        #print("================")
    for i in range(len(highscore)):
        for j in range(len(mylist)):
            if highscore[i] == "" or float(highscore[i]) > float(mylist[j]) :
                highscore[i] = mylist[j]
                k = j
        del mylist[k]
    return highscore    



try:
    with open(jamesfile) as jaf,open(juliefile) as juf,jaf,open(mikeyfile) as mif,jaf,open(sarahfile) as saf:
        jalist = jaf.readline().strip().split(",")
        julist = juf.readline().strip().split(",")
        milist = mif.readline().strip().split(",")
        salist = saf.readline().strip().split(",")
except IOError as ie:
    print("IOError" ,ie)

#sys.exit()

jalist = replacelist(jalist)
print(jalist)
#jalist = gethighscore(jalist)
jalist.sort()                      #原地排序
#jalisted = sorted(jalist)         #复制排序
print(jalist)

print("-------------")

julist = replacelist(julist)
print(julist)
julist = gethighscore(julist)
print(julist)
print("-------------")

milist = replacelist(milist)
print(milist)
milist = gethighscore(milist)
print(milist)
print("-------------")

salist = replacelist(salist)
print(salist)
salist = gethighscore(salist)
print(salist)






