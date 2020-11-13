def getKey(dic = {},key = "") :
    result = ""
    
    try:
        result = dic[key]
    except KeyError :
        result = None
    except TypeError :
        result = None
    except :
        result = None
        
    return result

