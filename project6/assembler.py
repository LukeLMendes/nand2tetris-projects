from parser import Parser
from codeModule import comp
from codeModule import jump
from codeModule import dest

def toBin16(number): #function to get corresponding 16-bit binary number
    return format(number, '016b')


def assembler(path):
    parser=Parser(path)
    symbol_table={}
    for i in range(0, 16):
        symbol_table[f"R{i}"]=i

    symbol_table["SP"]=0
    symbol_table["LCL"]=1
    symbol_table["ARG"]=2
    symbol_table["THIS"]=3
    symbol_table["THAT"]=4
    symbol_table["SCREEN"]=16384
    symbol_table["KBD"]=24576
    symbol_table["LOOP"]=4

    variable = 16


    current_line = -1
    while(parser.hasMoreLines()):
        current_line += 1
        parser.advance()
        if(parser.instructionType() == "L_INSTRUCTION"):
            symbol_table[parser.symbol] = current_line+1

    parser.indice = -1 #resets for second pass

    instructions = []
    while(parser.hasMoreLines()):
        parser.advance()


        if(parser.instructionType() == "A_INSTRUCTION"):
            if(parser.symbol().isdigit()):
                instructions.append(toBin16(int(parser.symbol())))
            elif (symbol_table.get(parser.symbol()) != None): #symbol is in symbol_table
                instructions.append(toBin16(symbol_table.get(parser.symbol())) )
            else:
                symbol_table[parser.symbol()] = variable #add symbol to symbol table
                variable += 1
                instructions.append(toBin16(symbol_table.get(parser.symbol())) )
        elif(parser.instructionType() == "C_INSTRUCTION"):
            instructions.append("111"+comp(parser.comp())+dest(parser.dest())+jump(parser.jump()) )

    return instructions


path = str(input())
instructions = assembler(path+".asm")
with open(f"{path}.hack", "w", encoding="utf-8") as file:
    for i in range(0, len(instructions)):
        if (i < len(instructions[i])-1):
            file.writelines(instructions[i] + '\n')
        else:
            file.writelines(instructions[i])

print("File .hack created with sucess!")




