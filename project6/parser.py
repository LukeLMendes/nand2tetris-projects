class Parser:
    def __init__(self, path):
        with open(path, "r") as file:
            self.assembly = [
                line for line in file
                if line.strip() and not(line.strip().startswith("//"))
            ]
            self.indice = -1

    def hasMoreLines(self):
        if (self.indice >= len(self.assembly) - 1):
            return False
        else:
            return True

    def advance(self):
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

    def dest(self):
        instruction = self.assembly[self.indice].strip()
        if not("=" in instruction):
            return None
        else:
            return instruction.split("=")[0].strip()

    def comp(self):
        instruction = self.assembly[self.indice].strip()
        if not("=" in instruction):
            if not(";" in instruction):
                return instruction
            else:
                return instruction.split(";")[0].strip()
        else:
            if not(";" in instruction):
                return instruction.split("=")[1].strip()
            else:
                comp = instruction.split("=")[1].strip().split(";")[0].strip()
                return comp

    def jump(self):
        instruction = self.assembly[self.indice].strip()
        if not(";" in  instruction):
            return None
        else:
            return instruction.split(";")[1].strip()





