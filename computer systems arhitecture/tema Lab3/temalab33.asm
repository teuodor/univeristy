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
    a dw 257
    b dw 302
    c dw 555
    d dw 1000
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;(c+c+c)-b+(d-a)
    mov ax,[c]
    ;cwde
    add ax,[c]
    add ax,[c]
    sub ax,[b]
    add ax,[d]
    sub ax,[a]
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
