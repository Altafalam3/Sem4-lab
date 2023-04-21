.model small
.data
num dw 05h
.code
MOV ax, @data ; initialize the data segment
MOV ds, ax
MOV ax, 01 ; initialize ax = 1
MOV bx, num ; load the number in cx
CALL fact ; call procedure
MOV di, ax ; store lsb of result in di
MOV bp, 2 ; initialize count for no of times display is called
MOV bx, dx ; store msb of result in reg bx
MOV bx, di ; store lsb of result in bx
DEC bp ; decrement bp
MOV ah,4ch
Int 21h
Fact proc near ;function for finding the factorial
CMP bx,01 ;if bx=1
JZ l11 ;if yes ax=1
l12: MUL bx ;find factorial
DEC bx ; decrement bx
CMP bx,01 ;multiply bx=1
JNE l12
RET
l11:MOV ax,01 ;initialize ax=1
RET ;return to called program
fact ENDP ;end procedure
END ;end program