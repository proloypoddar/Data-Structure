def changeXY(s):
    if len(s)==0:
        return ''
    if s[0]=="x":
        return "y"+changeXY(s[1:])
    else:
        return s[0]+changeXY(s[1:])
print(changeXY("xhixhix"))