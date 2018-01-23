def isanumber(number):
    try:
        float(repr(number))
        isnumeric = True
    except:
        isnumeric = False
    return isnumeric

