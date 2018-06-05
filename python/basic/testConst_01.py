from MyPackage import const
from MyPackage.const import ConstError

const.MYNAME = "wujian"

print("定义常量：", const.MYNAME)
print(const.MYAGE)
print(const.MYCOMPANY)

try :
    const.MYNAME = "wujian2"
except ConstError as ce:
    print(ce)

try :
    del const.MYCOMPANY
except ConstError as ce:
    print(ce)

try :
    del const.MYNAME2
except NameError as ce:
    print(ce)

    