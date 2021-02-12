def calc(num1,op,num2):
    num1 = float(num1)
    num2 = float(num2)
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2

def EndWith3Div(string,character):
    flag = False
    i = 0
    listaMultiplos = []
    while i<len(string):
        if i%3 == 0:
            listaMultiplos.append(i)
        i+=1
    listaMultiplos.reverse()
    listaMultiplos = listaMultiplos[0:-1]
    if len(string) == 3 and string[0] == character and string[1] == character and string[2] == character:
        flag = True
    for n in listaMultiplos:
        DebePasar = string.endswith(character * (n+1)) or string.endswith(character * (n+2)) or string.endswith(character * (n+3))
        if string.endswith(character*n) and not DebePasar:
            flag = True
    return flag
    

