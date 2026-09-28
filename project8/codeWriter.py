class CodeWriter:
  def __init__(self, path):
    self.output_file = open(path, "w", encoding="utf-8")
    self.file_name = None
    self.current_function = "BOOTSTRAP"
    self.true_count = 0
    self.jump_count = 0
    self.i = 0


  def setFileName(self, file_name):
    self.file_name = file_name
    # Flow commands outside a function are scoped to the current file.
    self.current_function = file_name

  def writeInit(self):
    self.current_function = "BOOTSTRAP"
    self.output_file.write("@256\nD=A\n@SP\nM=D\n")
    self.writeCall("Sys.init", 0)

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
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@R13\nM=D\n@{index}\nD=A\n@ARG\nD=D+M\n@R14\nM=D\n@R13\nD=M\n@R14\nA=M\nM=D"
        return assembly
      elif segment=="local":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@R13\nM=D\n@{index}\nD=A\n@LCL\nD=D+M\n@R14\nM=D\n@R13\nD=M\n@R14\nA=M\nM=D"
        return assembly
      elif segment=="this":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@R13\nM=D\n@{index}\nD=A\n@THIS\nD=D+M\n@R14\nM=D\n@R13\nD=M\n@R14\nA=M\nM=D"
        return assembly
      elif segment=="that":
        assembly = f"@SP\nM=M-1\nA=M\nD=M\n@R13\nM=D\n@{index}\nD=A\n@THAT\nD=D+M\n@R14\nM=D\n@R13\nD=M\n@R14\nA=M\nM=D"
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
    self.output_file.write(f"({self.current_function}${label})\n")

  def writeGoto(self, label):
    self.output_file.write(f"@{self.current_function}${label}\n0;JMP\n")

  def writeIf(self, label):
    self.output_file.write(
      f"@SP\nAM=M-1\nD=M\n@{self.current_function}${label}\nD;JNE\n"
    )

  def writeFunction(self, functionName, nVars):
    # Function scope is lexical; calls and returns do not change it.
    self.current_function = functionName
    self.output_file.write(f"({functionName})\n")
    for _ in range(nVars):
      self.writePushPop("C_PUSH", "constant", 0)

  def writeCall(self, functionName, nArgs):
    current_function = self.current_function

    # push returnAddress
    self.output_file.write(f"@{current_function}$ret.{self.i}" + "\n")
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
    self.output_file.write(f"@{functionName}\n0;JMP" + "\n")

    # (returnAddress)
    self.output_file.write(f"({current_function}$ret.{self.i})" + "\n")

    self.i += 1

  def writeReturn(self):
    # frame = *(LCL)
    # Save FRAME before writing the return value.
    self.output_file.write("@LCL\nD=M\n@R13\nM=D\n")
    # returnAddress = *(frame-5)
    self.output_file.write("@5\nA=D-A\nD=M\n@R14\nM=D\n")

    # *(ARG) = pop()
    self.output_file.write("@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n")
    # SP = ARG + 1
    self.output_file.write("@ARG\nD=M+1\n@SP\nM=D\n")

    # Restore the saved segments in this order:
    # THAT = *(frame-1)
    # THIS = *(frame-2)
    # ARG = *(frame-3)
    #LCL = *(frame-4)
    for segment in ("THAT", "THIS", "ARG", "LCL"):
      self.output_file.write(f"@R13\nAM=M-1\nD=M\n@{segment}\nM=D\n")

    # goto returnAddress
    self.output_file.write("@R14\nA=M\n0;JMP\n")


  def close(self):
    self.output_file.close()





