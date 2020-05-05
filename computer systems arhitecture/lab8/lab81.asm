bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program

extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a resd 1
    b resd 1
    format db '%u %u',0
    format2 db '%u mod %u = %u',0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
    push dword b
    push dword a
    push dword format
    call [scanf]
    add esp,4*3
    
    mov eax,[a]
    shr eax,16
    mov dx,ax
    mov eax,[a]
    div word [b]
    
    mov ebx,0
    mov bx,dx
    mov ecx,0
    mov cx,[b]
    
    push ebx
    push ecx
    push dword [a]
    push dword format2
    call [printf]
    add esp,4*4
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
