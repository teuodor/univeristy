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
    s dd 0702090Ah,0B0C0304h, 05060108h
    ls equ ($-s)/4
    ls2 equ ls*2
    s2 resb ls2
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
    mov esi,s
    mov ecx,ls2
    mov esp,0
    bucla1:
        lodsw
        mov bx,0
        or bl,al
        shr ax,4
        or bl,al
        mov [s2+esp],bl
        inc esp
        loop bucla1
    mov dx,ls2-1
    bucla2:
        mov ecx,ls2-1
        mov esi,s2
        bucla3:
            mov al,[esi]
            cmp al,[esi+1]
            jl final
            xchg al,[esi+1]
            mov [esi],al
            final:
            inc esi
            loop bucla3
        dec dx
        cmp dx,0
        jne bucla2

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
