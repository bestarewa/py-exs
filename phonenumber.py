def isphoneNumber(text):
    if len(text) != 11:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] !=  '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-' :
        return False
    for i in range(8,11):
        if not text[i].isdecimal():
            return False
        return True
print('080,6064.5969')
print(isphoneNumber('080,6064,5969'))
print('ahmad ahmad is phone number:')
print(isphoneNumber('ahmad ahmad'))