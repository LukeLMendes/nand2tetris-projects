class CodeWriter:
  def __init__(self, path):
    self.output_file = open(path, "w", encoding="utf-8")
    self.file_name = None
    self.function_name = None
    self.true_count = 0
    self.jump_count = 0
    self.ret = {}


  def setFileName(self, string):
    self.file_name = string

  def setFunctionName(self, string):
    self.function_name = f"{self.file_name}.{string}"
    self.ret[self.function_name] = 0

  def translateArithmetic(self, string):
    if (string.strip() == "add"):
      assembly = "@SP\nA=M-1\nD=M\nA=A-1\nM=D+M\n@SP\nM=M-1"
      return assembly
    elif (string.strip() == "sub"):
      assembly = "@SP\nA=M-1\nD=M\nA=A-1\nM=M-D\n@SP\nM=M-1"
      return assembly
    elif (string.strip() == "neg"):
      assembly = "@SP\nA=M-1\nM=-M"
      return assembly
    elif (string.strip() == "eq"):
      assembly = f"@SP\nA=M-1\nD=M\nA=A-1\nD=D-M\n@TRUE{self.true_count}\nD;JEQ\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP{self.jump_count}\n0;JMP\n(TRUE{self.true_count})\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP{self.jump_count})"
      self.true_count += 1
      self.jump_count += 1
      return assembly
    elif (string.strip() == "gt"):
      assembly = f"@SP\nA=M-1\nD=M\nA=A-1\nD=M-D\n@TRUE{self.true_count}\nD;JGT\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP{self.jump_count}\n0;JMP\n(TRUE{self.true_count})\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP{self.jump_count})"
      self.true_count += 1
      self.jump_count += 1
      return assembly
    elif (string.strip() == "lt"):
      assembly = f"@SP\nA=M-1\nD=M\nA=A-1\nD=M-D\n@TRUE{self.true_count}\nD;JLT\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP{self.jump_count}\n0;JMP\n(TRUE{self.true_count})\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP{self.jump_count})"
      self.true_count += 1
      self.jump_count += 1
      return assembly
    elif (string.strip() == "and"):
      assembly = "@SP\nA=M-1\nD=M\nA=A-1\nM=D&M\n@SP\nM=M-1"
      return assembly
    elif (string.strip() == "or"):
      assembly = "@SP\nA=M-1\nD=M\nA=A-1\nM=D|M\n@SP\nM=M-1"
      return assembly
    elif (string.strip() == "not"):
      assembly = "@SP\nA=M-1\nM=!M"
      return assembly


  def writeArithmetic(self, string):
    assembly = self.translateArithmetic(string)
    self.output_file.write(assembly + "\n")

  def translatePushPop(self, command, segment, index):
    if command == "C_PUSH":
      if segment == "argument":
        assembly = f"@{index}\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "local":
        assembly = f"@{index}\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "that":
        assembly = f"@{index}\nD=A\n@THAT\nA=D+M\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "this":
        assembly = f"@{index}\nD=A\n@THIS\nA=D+M\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "static":
        assembly = "@" + self.file_name + f".{index}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "constant":
        assembly = f"@{index}\nD=A\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "pointer":
        assembly = f"@{3+index}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif segment == "temp":
        assembly = f"@{index+5}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
    elif command == "C_POP":
      if segment=="argument":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@5\nM=D\n@{index}\nD=A\n@ARG\nD=D+M\n@6\nM=D\n@5\nD=M\n@6\nA=M\nM=D"
        return assembly
      elif segment=="local":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@5\nM=D\n@{index}\nD=A\n@LCL\nD=D+M\n@6\nM=D\n@5\nD=M\n@6\nA=M\nM=D"
        return assembly
      elif segment=="this":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@5\nM=D\n@{index}\nD=A\n@THIS\nD=D+M\n@6\nM=D\n@5\nD=M\n@6\nA=M\nM=D"
        return assembly
      elif segment=="that":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@5\nM=D\n@{index}\nD=A\n@THAT\nD=D+M\n@6\nM=D\n@5\nD=M\n@6\nA=M\nM=D"
        return assembly
      elif segment=="static":
        assembly = "@SP\nM=M-1\nA=M\nD=M\n@" + self.file_name + f".{index}\nM=D"
        return assembly
      elif segment=="pointer":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@{3+index}\nM=D"
        return assembly
      elif segment=="temp":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@{index+5}\nM=D"
        return assembly
    else:
      raise ValueError(f"Unknown segment: {segment}")

  def writePushPop(self, command, segment, index):
    assembly = self.translatePushPop(command, segment, index)
    self.output_file.write(assembly + "\n")

  def writeLabel(self, label):
    label = f"({self.function_name}${label})"
    self.output_file.write(label + "\n")

  def writeGoto(self, label):
    label = f"{self.function_name}${label}"
    goto_command = f"@{label}\n0;JMP"
    self.output_file.write(goto_command + "\n")

  def writeIf(self, label):
    label = f"{self.function_name}${label}"
    ifgoto_command = f"@SP\nM=M-1\nA=M\nD=M\n@{label}\nD;JGT"
    self.output_file.write(ifgoto_command + "\n")

  def writeFunction(self, functionName, nVars):
    self.setFunctionName(functionName)

    #creates a funcion, opening space in the memory for the locals variables
    self.output_file.write(f"({self.function_name})" + "\n") # (functionName)
    self.writePushPop("C_PUSH", "constant", 0)               # push constant 0
    self.writePushPop("C_POP", "temp", 0)                    # pop temp 0
    self.writeLabel("LOOP")                                  # (LOOP)
    self.writePushPop("C_PUSH", "temp", 0)                   # push temp 0
    self.writePushPop("C_PUSH", "constant", int(nVars))      # push constant nVars
    self.writeArithmetic("lt")                               # lt
    self.writeArithmetic("neg")                              # neg
    self.writeIf("END_LOOP")                                 # if-goto END_LOOP
    self.writePushPop("C_PUSH", "constant", 0)               # push constant 0
    self.writePushPop("C_PUSH", "temp", 0)                   # push temp 0
    self.writePushPop("C_PUSH", "constant", 1)               # push constant 1
    self.writeArithmetic("add")                              # add
    self.writePushPop("C_POP", "temp", 0)                    # pop temp 0
    self.writeGoto("LOOP")                                   # goto LOOP
    self.writeLabel("END_LOOP")                              # (END_LOOP)

def writeCall(self, functionName, nArgs, fileName):
  callee_name = f"{fileName}.{functionName}"

  # push returnAddress
  self.output_file.write(f"@{self.function_name}$ret.{self.ret.get(self.function_name)}" + "\n")
  self.output_file.write("D=A\n@SP\nM=M+1\nA=M-1\nM=D" + "\n")

  # push LCL
  push = "D=M\n@SP\nM=M+1\nA=M-1\nM=D"
  self.output_file.write("@LCL\n" + push + "\n")

  # push ARG
  self.output_file.write("@ARG\n" + push + "\n")

  # push THIS
  self.writePushPop("C_PUSH", "pointer", 0)

  # push THAT
  self.writePushPop("C_PUSH", "pointer", 1)

  # ARG = SP-5-nArgs
  self.output_file.write(f"@5\nD=A\n@{nArgs}\nD=D+A\n@SP\nD=M-D\n@ARG\nM=D" + "\n")

  # LCL = SP
  self.output_file.write("@SP\nD=M\n@LCL\nM=D" + "\n")

  # goto functionName
  self.output_file.write("@{callee_name}\n0;JMP" + "\n")

  # (returnAddress)
  self.output_file.write("({self.function_name}$ret.{self.ret.get(self.function_name)})" + "\n")

  self.ret[self.function_name] += 1

def writeReturn(self):

  # *(ARG) = pop()
  self.output_file.write("@SP\nA=M-1\nD=M\nARG\nA=M\nM=D" + "\n")

  # frame = *(LCL)
  # THAT = *(frame-1)
  self.output_file.write("@LCL\nD=M\n@5\nM=D\nM=M-1\nA=M\nD=M\n@THAT\nM=D" + "\n")

  # THIS = *(frame-2)
  self.output_file.write("@5\nM=M-1\nA=M\nD=M\n@THIS\nM=D" + "\n")

  # ARG = *(frame-3)
  self.output_file.write("@5\nM=M-1\nA=M\nD=M\n@ARG\nM=D" + "\n")

  #LCL = *(frame-4)
  self.output_file.write("@5\nM=M-1\nA=M\nD=M\n@LCL\nM=D" + "\n")

  #goto returnAddress
  self.output_file.write("@5\nM=M-1\nA=M\nA=M\n0;JMP" + "\n")


  def close(self):
    self.output_file.close()





