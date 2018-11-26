

kvtypes = {1:"股票型", 2:"债券型", 3:"混合型"}

vktypes =  {v : k for k, v in kvtypes.items()}

kvstyles = {1:"价值型", 2:"成长型", 3:"平衡型", 4:"指数型", 5:"其他"}

vkstyles = {v : k for k, v in kvstyles.items()}


def get_type_value(type_key) :

    return kvtypes.get(type_key,"-")

def get_type_key(type_value) :

    print(vktypes)
    return vktypes.get(type_value,0)

def get_style_value(style_key) :

    return kvstyles.get(style_key,"-")

def get_style_key(style_value) :

    print(vkstyles)
    return vkstyles.get(style_value,0)

def per2f(pernum) :

    try:
        return float(pernum.strip('%'))*1000/100000

    except Exception as e:

        print("【ERROR】: " + e)
        return ""
    

def f2per(fnum) :

    try:

        return "{:.1f}%".format(fnum*100)
    
    except Exception as e:

        print(e)
        return "-"

def n2yi(num) :

    try:

        return str(round(float(num)/100000000.0,2)) + "亿"
    
    except Exception as e:

        print(e)
        return "-"
