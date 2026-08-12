
def dest(string):
    null = "000"

    if string == None:
        return null

    if "D" in string:
        null[1] = '1'
    if "M" in string:
        null[2] = '1'
    if "A" in string:
        null[0] = '1'

    return null

def comp(string):
    code = "0000000"

    if string == "0":
        for i in range(1, 7):
            if i%2 != 0:
                code[i] = "1"
    elif string == "1":
        for i in range (1, 7):
            code[i] = "1"
    elif string == "-1":
        code[1]="1"
        code[2]="1"
        code[3]="1"
        code[5]="1"

    if "M" in string:
        code[0] = '1'

    if not("D" in string):
        code[1] = '1'

    if not("A" in string) and not("M" in string):
        code[3] = '1'

    if "D+1" in string:
        for i in range(2, 7):
            code[i] = '1'

    if "A+1" in string or "M+1" in string:
        code[1] = code[2] = code[4] = code[5] = code[6] = '1'

    if "D-1" in string:
        code[3] = code[4] = code[5] = '1'

    if "A-1" in string or "M-1" in string:
        code[1] = code[2] = code[5] = '1'

    if "D+" in string:
        code[5] = '1'

    if "D-" in string:
        code[2] = code[5] = code[6] = '1'

    if "-D" in string:
        code[4] = code[5] = code[6] = '1'

    if "D|" in string:
        code[2] = code[4] = code[6] = '1'

    return code





def jump(string):
    if string == None:
        return "000"
    elif string == "JGT":
        return "001"
    elif string == "JEQ":
        return "010"
    elif string == "JGE":
        return "011"
    elif string == "JLT":
        return "100"
    elif string == "JNE":
        return "101"
    elif string == "JLE":
        return "110"
    elif string == "JMP":
        return "111"
