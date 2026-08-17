### Dictionary of comp instructions
COMP_TABLE = {
    "0":   "0101010", "1":   "0111111", "-1":  "0111010",
    "D":   "0001100", "A":   "0110000", "!D":  "0001101",
    "!A":  "0110001", "-D":  "0001111", "-A":  "0110011",
    "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    "M":   "1110000", "!M":  "1110001", "-M":  "1110011",
    "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
    "D|M": "1010101",
}
###

def dest(string):
    if string is None:
        return "000"
    a = '1' if 'A' in string else '0'
    d = '1' if 'D' in string else '0'
    m = '1' if 'M' in string else '0'
    return a + d + m

def comp(string):
    return COMP_TABLE.get(string)


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
