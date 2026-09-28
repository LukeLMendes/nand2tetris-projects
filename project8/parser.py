class Parser:
    def __init__(self, path):
        with open(path, "r") as file:
            self.vmcode = [
                line for line in file
                if line.strip() and not(line.strip().startswith("//"))
            ]
            self.indice = -1

    def hasMoreLines(self):
        if (self.indice >= len(self.vmcode) - 1):
            return False
        else:
            return True

    def advance(self):
        self.indice += 1

    def commandType(self):
        if ("push" in self.vmcode[self.indice].strip()):
            return "C_PUSH"
        elif ("pop" in self.vmcode[self.indice].strip()):
            return "C_POP"
        elif ("add" in self.vmcode[self.indice] or "sub" in self.vmcode[self.indice] or
              "neg" in self.vmcode[self.indice] or "eq" in self.vmcode[self.indice]  or
              "gt" in self.vmcode[self.indice] or "lt" in self.vmcode[self.indice] or
              "and" in self.vmcode[self.indice] or "not" in self.vmcode[self.indice] or
              "or" in self.vmcode[self.indice]):
            return "C_ARITHMETIC"
        elif ("label" in self.vmcode[self.indice]):
            return "C_LABEL"
        elif ("if-goto" in self.vmcode[self.indice]):
            return "C_IF"
        elif ("goto" in self.vmcode[self.indice]):
            return "C_GOTO"
        elif ("function" in self.vmcode[self.indice]):
            return "C_FUNCTION"
        elif ("call" in self.vmcode[self.indice]):
            return "C_CALL"
        elif ("return" in self.vmcode[self.indice]):
            return "C_RETURN"

    def arg1(self):
        if self.commandType() == "C_ARITHMETIC":
            arg1 = self.vmcode[self.indice].strip()
            return arg1 #returns "add", "sub", "neg" etc.
        else:
            arg1 = self.vmcode[self.indice].strip().split()[1].strip()
            return arg1 #return local, this, that, functionName etc.


    def arg2(self):
        arg2 = self.vmcode[self.indice].strip().split()
        return int(arg2[2]) #return index, nVars ,nArgs or label

