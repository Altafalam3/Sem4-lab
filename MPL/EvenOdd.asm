.model small
.data
array db 12h, 23h, 26h, 63h, 25h, 36h, 2fh, 33h, 10h, 35h
.code
start: MOV ax,@data
MOV ds,ax
MOV cl,10
MOV SI,2000h
MOV DI,2008h
LEA BP,array
back: MOV AL,DS:[BP]
MOV BL,AL
AND AL,01H
JZ next
MOV [DI],bl
INC DI
JMP skip
next: MOV [SI],bl
INC SI
skip: INC BP
DEC CL
JNZ back
int 03H
end start