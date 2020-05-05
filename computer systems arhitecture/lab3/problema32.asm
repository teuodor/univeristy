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
    a db 2
    b db 3
    c dw 258
    e dd 120
    x dq 302
; our code starts here
segment code use32 class=code
    start:
        ; ... (a-2)/(b+c)+a*c+e-x; a,b-byte; c-word; e-doubleword;-cu semn
    mov al,[a]
    sub al,2
    cbw
    cwd; dx:ax=(a-2)
    mov cx,ax
    mov bx,[c]
    mov al,[b]
    cbw
    add bx,ax
    mov ax,cx
    idiv bx;ax=(a-2)/(b+c)
    mov cx,ax;cx=(a-2)/(b+c)
    mov al,[a]
    cbw;ax=a
    imul word [c]
    push dx
    push ax
    pop eax;eax=a*c
    mov ebx,eax;ebx=a*c
    mov ax,cx;ax=(a-2)/(b+c)
    cwde
    add ebx,eax;ebx=(a-2)/(b+c)+a*c
    mov eax,ebx;eax=(a-2)/(b+c)+a*c
    cdq;edx:eax=(a-2)/(b+c)+a*c
    mov ebx,eax
    mov ecx,edx
    mov eax,[e]
    cdq
    add eax,ebx
    add edx,ecx;edx:eax=(a-2)/(b+c)+a*c+e
    mov ebx,dword[x]
    mov ecx,dword[x+4]
    sub eax,ebx
    sub edx,ecx;edx:eax=(a-2)/(b+c)+a*c+e-x
    
    
    
    
    
    
    
    
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
