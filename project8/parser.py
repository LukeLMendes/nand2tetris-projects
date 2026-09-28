class Parser:
    def __init__(self, path):
        with open(path, "r") as file:
            self.vmcode = [
                command for line in file
                if (command := line.split("//", 1)[0].strip())
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
        command = self.vmcode[self.indice].split()[0].strip()
        if command == "push":
            return "C_PUSH"
        elif command == "pop":
            return "C_POP"
        elif command in ("add", "sub", "neg", "eq", "gt", "lt", "and", "not", "or"):
            return "C_ARITHMETIC"
        elif command == "label":
            return "C_LABEL"
        elif command == "if-goto":
            return "C_IF"
        elif command == "goto":
            return "C_GOTO"
        elif command == "function":
            return "C_FUNCTION"
        elif command == "call":
            return "C_CALL"
        elif command == "return":
            return "C_RETURN"
        else:
            raise ValueError(f"Unknown VM command: {command}")

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
