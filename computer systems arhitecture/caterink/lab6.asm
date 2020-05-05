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
    s db 1,3,-2,-5,3,-8,5,0
    ls equ $-s
    d1 resb ls
    d2 resb ls
; our code starts here
segment code use32 class=code
    start:
        ; ...
    mov ecx,ls
    mov esi,s
    mov edx,0
    mov ebx,0
    bucla:
        ;lodsb
        mov al,[esi]
        inc esi
        cmp al,0
        jge set_poz
        jl set_neg
        set_poz:
            mov [d1+edx],al
            inc edx
            jmp final
        set_neg:
            mov [d2+ebx],al
            inc ebx
        final:   
    loop bucla
            
            
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
