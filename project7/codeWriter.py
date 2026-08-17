def writeArithmetic(string):
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
    assembly = "@SP\nA=M-1\nD=M\nA=A-1\nD=D-M\n@TRUE\nD;JEQ\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP\n0;JMP\n(TRUE)\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP)"
    return assembly
  elif (string.strip() == "gt"):
    assembly = "@SP\nA=M-1\nD=M\nA=A-1\nD=M-D\n@TRUE\nD;JGT\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP\n0;JMP\n(TRUE)\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP)"
    return assembly
  elif (string.strip() == "lt"):
    assembly = "@SP\nA=M-1\nD=M\nA=A-1\nD=M-D\n@TRUE\nD;JLT\n@SP\nM=M-1\nA=M-1\nM=0\n@JUMP\n0;JMP\n(TRUE)\n@SP\nM=M-1\nA=M-1\nM=-1\n(JUMP)"
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

def writePushPop(command, segment, index):
  if command == "C_PUSH":
    if segment == "argument":
      assembly = f"@{index}\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "local":
      assembly = f"@{index}\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "that":
      assembly = f"@{index}\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "this":
      assembly = f"@{index}\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "static":
      assembly = f"@file_name.{index}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "constant":
      assembly = f"@{index}\nD=A\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly
    elif segment == "pointer":
      if index == 0:
        assembly = "@3\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
      elif index == 1:
        assembly = "@4\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
        return assembly
    elif segment == "temp":
      assembly = f"@{index+5}\nD=M\n@SP\nM=M+1\nA=M-1\nM=D"
      return assembly




