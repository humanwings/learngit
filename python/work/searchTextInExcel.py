import xlrd
import re
import os

def get_excel_list(root):
    filelist = []
    for root,dirs,files in os.walk(root):
        for file in files:
            if (file.endswith("xls") or file.endswith("xlsx")) :
                filelist.append(file)
    return filelist

def open_excel(file):
    try:
        book = xlrd.open_workbook(file)
        return book
    except Exception as e :
        print(str(e))

def get_txtlist(file):
    book = open_excel(file)
    sheet = book.sheet_by_index(0)

    col = sheet.col(2)

    keylist = ["は","が","です","でした","を","ません","ます","します","しました"]

    patternlist = []

    for i,key in enumerate(keylist):
        patternlist.append(re.compile('[一-龥ぁ-んァ-ンー]*' + key + '[一-龥ぁ-んァ-ンー]*'))


    txtlist = []
    
    for i,cell in enumerate(col) :
        flag = False
        for pattern in patternlist:
            match = pattern.search(cell.value)
            if  match  :
                # print(i , ' : ' , match.group(0))
                txtlist.append(match.group(0))
                break
    print(len(txtlist))

    txtset = set(txtlist)
    print(len(txtset))

    return txtset

def check_txt(txtlist,excellist):
    
    book = open_excel(excellist[0])
    for sheet in book.sheets():
        if "画面操作概要" in sheet.name :
            print(sheet.name)

            for i in range(sheet.nrows):
                for j in range(sheet.ncols):
                    



def main():
    # txtlist = get_txtlist("diff_c.xlsx")

    excellist = get_excel_list(r"D:\work\99.tmp\010_画面設計")
    # print(len(excellist))
    
    check_txt(txtlist,excellist)


if __name__=="__main__":
    main()
