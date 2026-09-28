import argparse
from pathlib import Path

from parser import Parser
from codeWriter import CodeWriter


def vmTranslator(path, bootstrap=True):
  """Translate a VM file or the immediate .vm files in a directory."""
  path = Path(path).expanduser().resolve()
  if path.is_dir():
    vm_files = sorted(file for file in path.glob("*.vm") if file.is_file())
    if not vm_files:
      raise ValueError(f"No .vm files found in: {path}")
    output_path = path / f"{path.name}.asm"
  elif path.is_file() and path.suffix == ".vm":
    vm_files = [path]
    output_path = path.with_suffix(".asm")
  else:
    raise ValueError(f"Expected a .vm file or directory: {path}")

  codeWriter = CodeWriter(output_path)
  try:
    if bootstrap:
      codeWriter.writeInit()

    for vm_file in vm_files:
      codeWriter.setFileName(vm_file.stem)
      parser = Parser(vm_file)
      while parser.hasMoreLines():
        parser.advance()
        commandType = parser.commandType()

        if commandType == "C_RETURN":
          codeWriter.writeReturn()
        elif commandType == "C_ARITHMETIC":
          codeWriter.writeArithmetic(parser.arg1())
        elif commandType in ("C_PUSH", "C_POP"):
          codeWriter.writePushPop(commandType, parser.arg1(), parser.arg2())
        elif commandType == "C_LABEL":
          codeWriter.writeLabel(parser.arg1())
        elif commandType == "C_GOTO":
          codeWriter.writeGoto(parser.arg1())
        elif commandType == "C_IF":
          codeWriter.writeIf(parser.arg1())
        elif commandType == "C_FUNCTION":
          codeWriter.writeFunction(parser.arg1(), parser.arg2())
        elif commandType == "C_CALL":
          codeWriter.writeCall(parser.arg1(), parser.arg2())
  finally:
    codeWriter.close()

  return output_path


def main():
  cli = argparse.ArgumentParser(description="Translate VM code to Hack assembly.")
  cli.add_argument("path", help="Input .vm file or directory containing .vm files")
  cli.add_argument(
    "--no-bootstrap", action="store_true",
    help="Skip SP=256 and call Sys.init (for tests that initialize RAM themselves)",
  )
  args = cli.parse_args()
  try:
    output_path = vmTranslator(args.path, bootstrap=not args.no_bootstrap)
  except (OSError, ValueError) as error:
    cli.error(str(error))
  print(f".asm file created successfully: {output_path}")


if __name__ == "__main__":
  main()

