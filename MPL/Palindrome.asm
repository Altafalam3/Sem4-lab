.MODEL SMALL
.STACK 100H
.DATA ; The string to be printed
STRING DB 'Madam', '$'
STRING1 DB 'String is palindrome', '$'
STRING2 DB 'String is not palindrome', '$'
.CODE
MAIN PROC FAR
MOV AX, @DATA
MOV DS, AX
; check if the string is;
;palindrome or not
CALL Palindrome
;interrupt to exit
MOV AH, 4CH
INT 21H
MAIN ENDP
Palindrome PROC
; load the starting address
; of the string
MOV SI, OFFSET STRING
; traverse to the end of;
;the string
LOOP1 :
MOV AX, [SI]
CMP AL, '$'
JE LABEL1
INC SI
JMP LOOP1
;load the starting address;
;of the string
LABEL1 :
MOV DI, OFFSET STRING
DEC SI
; check if the string is palindrome;
;or not
LOOP2 :
CMP SI, DI
JL OUTPUT1
MOV AX, [SI]
MOV BX, [DI]
CMP AL, BL
JNE OUTPUT2
DEC SI
INC DI
JMP LOOP2
OUTPUT1:
;load address of the string
LEA DX,STRING1
; output the string;
;loaded in dx
MOV AH, 09H
INT 21H
RET
OUTPUT2:
;load address of the string
LEA DX,STRING2
; output the string
; loaded in dx
MOV AH,09H
INT 21H
RET
Palindrome ENDP
END MAIN