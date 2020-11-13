def getKey(dic = {},key = "") :
    result = ""
    
    try:
        result = dic[key]
    except KeyError :
        result = None

    return result

