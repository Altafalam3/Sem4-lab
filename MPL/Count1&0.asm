.model small
.data
n1 db 31h
zeros db 1 dup(0)
ones db 1 dup(0)
.code
Start:
mov ax,@data
mov ds,ax
mov cl,08h
mov ah,00h
mov al,n1
mov dx,0000h
up: rcl al,01H
JC next
inc dl
jmp down
next: inc dh
down: loop up
mov zeros, dh
mov ones,dl
int 03H
end Start