//Program: Multiplication

    @R0
    D=M

    @n
    M=D

    @i
    M=1
(LOOP)
    @i
    D=M
    @R1
    D=D-M
    @END
    D;JEQ

    @n
    D=M

    @R0
    M=D+M
    D=M

    @R2
    M=D

    @i
    M=M+1

    @LOOP
    0;JMP
(END)
    @END
    0;JMP
