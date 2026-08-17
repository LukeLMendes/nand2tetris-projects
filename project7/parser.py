class Parser:
    def __init__(self, path):
        with open(path, "r") as file:
            self.vmcode = file.readlines()
            self.indice = -1

    def hasMoreLines(self):
        for i in range(self.indice+1, len(self.vmcode)):
            if (len(self.vmcode[i].strip()) > 0 and not(self.vmcode[i].strip().startswith("//")) ):
                return True
        return False

    def advance(self):
        self.indice += 1
        while (len(self.vmcode[self.indice].strip()) ==  0 or self.vmcode[self.indice].strip().startswith("//")):
            self.indice += 1

    def commandType(self):
        if ("push" in self.vmcode[self.indice].strip()):
            return "C_PUSH"
        elif ("pop" in self.vmcode[self.indice].strip()):
            return "C_POP"
        elif ("add" in self.vmcode[self.indice] or "sub" in self.vmcode[self.indice] or
              "neg" in self.vmcode[self.indice] or "eq" in self.vmcode[self.indice]  or
              "gt" in self.vmcode[self.indice] or "lt" in self.vmcode[self.indice] or
              "and" in self.vmcode[self.indice] or "not" in self.vmcode[self.indice]):
            return "C_ARITHMETIC"

    def arg1(self):
        if self.commandType() == "C_ARITHMETIC":
            arg1 = self.vmcode[self.indice].strip()
            return arg1
        return None

    def arg2(self):
        if self.commandType() == "C_POP":
            arg2 = self.vmcode[self.indice].strip().split()[1]
            return arg2
        if self.commandType() == "C_PUSH":
            arg2 = self.vmcode[self.indice].strip().split()[1]
            return arg2
        

