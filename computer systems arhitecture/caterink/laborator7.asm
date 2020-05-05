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
    s dd 12345607h,1A2B3C15h,13A33412h
    ls equ ($-s)/4
    d resb ls
    e db 7

; our code starts here
segment code use32 class=code
    start:
        ; ...
    mov ecx,ls
    mov esi,s
    mov edx,0
    bucla:
        lodsd
        mov bl,al
        shl eax,24
        shr eax,24
        div byte[e]
        cmp ah,0
        jne final
        mov [d+edx],bl
        inc edx
        final:
    loop bucla
        
        
        
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
