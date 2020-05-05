bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 3
    b dw 200
    c dd 1002
    d dq 302
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;c+(a-b)-(d+d+d)-fara semn
    mov eax,[c];eax=c
    mov ebx,0
    mov bl,[a];ebx=a
    add eax,ebx;eax=c+a
    mov ebx,0
    mov bx,[b];ebx=b
    sub eax,ebx;eax=c+a-b
    mov ebx,dword[d]
    mov ecx,dword[d+4];ecx:ebx=d
    mov edx,0;edx:eax=c+a-b
    sub eax,ebx
    sbb edx,ecx  
    sub eax,ebx
    sbb edx,ecx
    sub eax,ebx
    sbb edx,ecx;edx:eax=c+a-b-d-d-d
    
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
