class Parser:
    def __init__(self, path):
        with open(path, "r") as arquivo:
            self.assembly = arquivo.readlines()
            self.indice = -1

    def hasMoreLines(self):
        if (self.indice >= len(self.assembly) - 1):
            return False
        else:
            for i in range(self.indice+1, len(self.assembly)):
                if len(self.assembly[i].strip()) == 0:
                    continue

                if not(self.assembly[i].strip().startswith("\\")):
                    return True
            return False

    def advance(self):
        while (self.assembly[self.indice].strip().startswith("//") or
             len(self.assembly[self.indice].strip()) == 0):
            self.indice += 1

    def instructionType(self):
        if (self.assembly[self.indice].strip().startswith("@")):
            return "A_INSTRUCTION"
        elif (self.assembly[self.indice].strip().startswith("(")):
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    def symbol(self):
        instruction = self.assembly[self.indice].strip()
        if self.instructionType() == "A_INSTRUCTION":
            return instruction.strip("@")
        elif self.instructionType() == "L_INSTRUCTION":
            return instruction.strip("()")






