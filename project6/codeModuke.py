
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
    default = "0000000"
    if "M" in string:
        default[0] = '1'

    if not("D" in string):
        default[1] = '0'

    if not("A" in string) and not("M" in string):
        default[3] = '0'

    if ("+" in string) or ("-" in string):
        default[5] = "1"
    elif ("&" in string) or ("|" in string):
        default[5] = "0"


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
