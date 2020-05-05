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
    b dw 258
    c dd 3012
    d dq 302

; our code starts here
segment code use32 class=code
    start:
        ; ...
    ;(c+c+c)-b+(d-a) cu semn
    mov ebx,[c];ebx=c
    add ebx,[c];ebx=c+c
    add ebx,[c];ebx=c+c+c
    mov ax,[b];ax=b
    cwde;eax=b
    sub ebx,eax;ebx=c+c+c-b=-1
    mov eax,ebx
    cdq
    mov ecx,edx; ecx:ebx=(c+c+c)-b
    mov eax,dword[d]
    mov edx,dword[d+4];edx:eax=d
    add eax,ebx
    adc edx,ecx;edx:eax=c+c+c-b+d
    mov ebx,eax
    mov al,[a]
    cbw
    cwde
    sub ebx,eax
    mov eax,ebx;edx:eax=c+c+c-b+d-a
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
