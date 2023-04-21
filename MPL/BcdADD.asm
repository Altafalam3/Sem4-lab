.model small
.data
a dw 3629H
b dw 4738H
.code
mov ax, @data ; Initialize data section
mov ds, ax
mov ax, a ; Load number1 in ax
mov bx, b ; Load number2 in bx
add al, bl; add lower two digits. Result in al
daa ; adjust result to valid bcd
mov bl, al ; store result in bl
adc ah, bh ; add upper two digits. Result in ah
mov al, ah; al=ah as daa works on al only
daa ; adjust result to valid BCD
mov bh, al; store result in bh
mov ch, 04h ; Count of digits to be displayed
mov cl, 04h ; Count to roll by 4 bits cl, 04h
l2:rol bx, cl ; roll bl so that msb comes to lsb
mov dl, bl ; load dl with data to be displayed
and dl, 0fH ; get only lsb dl, 0fH
cmp dl, 09 ; check if digit is 0-9 or letter A-F
jbe l4
add dl, 07 ; if letter add 37H else only add
l4: add dl, 30H
mov ah, 02 ; Function 2 under INT 21H (Display character)
int 21H
dec ch ; Decrement Count
jnz l2
mov ah, 4cH ; T ; Terminate Program
int 21H
end