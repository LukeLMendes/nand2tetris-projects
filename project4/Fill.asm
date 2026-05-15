
(WATCH_KBD)
    @KBD
    D=M             // Le o valor do teclado
    
    @SET_BLACK
    D;JNE           // Se D != 0 (tecla pressionada), vai pra preto
    
    @color
    M=0             // Caso contrario, cor = 0 (branco)
    @START_FILL
    0;JMP

(SET_BLACK)
    @color
    M=-1            // Cor = preto (-1)

(START_FILL)
    @8192           // Prepara o contador (8192 palavras da tela)
    D=A
    @n
    M=D
    
    @SCREEN
    D=A
    @address
    M=D             // address = 16384 (ponteiro pra atela)

(FILL_LOOP)
    @n
    D=M
    @WATCH_KBD
    D;JEQ           // Se ja pintou as 8192 palavras, volta a vigiar o teclado

    @color
    D=M
    @address
    A=M             // Acessa o endereço de memoria atual da tela
    M=D             // Pinta a palavra inteira (16 pixels)

    @address
    M=M+1           // Move pra proxima palavra
    @n
    M=M-1           // Decrementa o contador
    
    @FILL_LOOP
    0;JMP
