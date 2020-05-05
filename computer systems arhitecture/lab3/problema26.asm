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
    r dd 10110101101110100100011011101010b
    t dd 10110101101110100100011001101010b
; our code starts here
segment code use32 class=code
    start:
        ; ...
    xor eax,eax
    mov ebx,[r]
    mov ecx,[t]
    
    mov edx,ecx;edx=t
    shl edx,15
    shr edx,24
    or eax,edx
    
    mov edx,ebx;edx=r
    shr edx,5
    shl edx,25
    or eax,edx
    
    xor ebx,ecx
    shl ebx,7
    shr ebx,14
    shl ebx,7
    or eax,ebx
    
    
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
