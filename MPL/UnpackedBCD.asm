.model small
.data
a db 13H
.code
mov ax, @data ; Initialize data section
mov ds, ax
mov al, a ; Load number1 in al
and al, 0f0h ; mask lower nibble
mov cl, 04h
rcr al, cl ; rotate it 4 times to right to make it 09h
mov bh, al ; store result in bh
call disp ; display the upper nibble
mov al, a ; Load number1 in al
and al, 0fh ; mask upper nibble
mov bh, al ; store result in bh
call disp ; display the lower nibble
mov ah, 4cH ; Terminate Program
int 21H
disp proc near
mov ch, 02h ; Count of digits to be displayed
mov cl, 04h ; Count to roll by 4 bits
l2: rol bh, cl ; roll bl so that msb comes to lsb
mov dl, bh ; load dl with data to be displayed
and dl, 0fH ; get only lsb
cmp dl, 09 ; check if digit is 0-9 or letter A-F
jbe l4
add dl, 07 ; if letter add 37H else only add 30H
l4: add dl, 30H
mov ah, 02 ; Function 2 under INT 21H (Display character)
int 21H
dec ch ; Decrement Count
jnz l2
mov ah, 02h
mov dl, ' '
int 21h
endp
ret
end