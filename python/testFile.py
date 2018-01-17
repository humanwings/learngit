import sys
import os

print(os.getcwd())

infile = "D:\doc\python\HeadFirstPythonFiles\人員一覧.txt"
outfile = "D:\doc\python\HeadFirstPythonFiles\人員一覧_bak.txt"
errfile = "D:\doc\python\HeadFirstPythonFiles\\not_exist.txt"

if not os.path.exists(infile) :
    print("The input file does not exist!")
    sys.exit()

if os.path.exists(outfile) :
    print("The output file already exists!")
    os.remove(outfile)


with open(infile) as fh:
    for line in fh:
        print(line.strip())

print()

fi = open(infile)
fo = open(outfile,"w")
for line in fi:
    #print(line.strip())
    (name,age) = line.split(",",1)
    print(name," : ",age,file=fo)

fi.close()
fo.close()

try:
    fe = open(errfile)
    print(fe.readline())
except IOError as err:
    print("file error : " + str(err) )
finally:
    if "fe" in locals():
        fe.close()
