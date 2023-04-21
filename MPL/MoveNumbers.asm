.model small
.code
start:
MOV SI,2000h
MOV DI,4000h
MOV CL,05h
LOOP1: MOV bl,[SI]
MOV [DI],bl
INC SI
INC DI
DEC CL
JNZ LOOP1
int 03h
end start