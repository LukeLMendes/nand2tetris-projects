from parser import Parser
from codeWriter import CodeWriter
from pathlib import Path

def vmTranslator(path):
  file_name = Path(path).stem
  parser = Parser(path)
  codeWriter = CodeWriter(Path(path).with_suffix(".asm"))
  codeWriter.setFileName(file_name)

  while(parser.hasMoreLines()):
    parser.advance()
    commandType = parser.commandType()
    arg1 = parser.arg1()

    if (commandType == "C_ARITHMETIC"):
      codeWriter.writeArithmetic(arg1)
    else:
      arg2 = parser.arg2()
      codeWriter.writePushPop(commandType, arg1, arg2)

  codeWriter.close()


path = input()
vmTranslator(path)
print(".asm File created with success")


