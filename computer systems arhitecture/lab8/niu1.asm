bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,scanf,fscanf,fprintf,fscanf,fopen,printf
import scanf msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll      
import fscanf msvcrt.dll 
import fopen msvcrt.dll     
import printf msvcrt.dll    ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
format_sir db '%s',0
format_carac db '%c',0
format_numar db '%d',0

mod_citire db 'r',0
descriptor1 dd -1

caracter_fisier resb 1
sir resb 10
carac resb 1
numar resb 1
; our code starts here
segment code use32 class=code
    start:
        ; ...
    push dword sir
    push dword format_sir
    call [scanf]
    add esp,4*2
    
    push dword carac
    push dword format_carac
    call [scanf]
    add esp,4*2

    push dword numar
    push dword format_numar
    call [scanf]
    add esp,4*2
    
    push dword mod_citire
    push dword sir
    call [fopen]
    add esp,4*2
    
    mov [descriptor1],eax
    
    repeta:
    push dword caracter_fisier
    push dword format_carac
    push dword [descriptor1]
    call [fscanf]
    add esp,4*3
    
    mov al,[carac]
    cmp [caracter_fisier],al
    jne final_loop
    
    mov ecx,[numar]
    
    forex:
    pushad
    push dword [caracter_fisier]
    push dword format_carac
    call [printf]
    add esp,4*2
    popad
    loop forex
    jmp peste
    
    
    
    final_loop:
    push dword [caracter_fisier]
    push dword format_carac
    call [printf]
    add esp,4*2
    
    peste:
    cmp [caracter_fisier],byte 10
    jne repeta
    
    final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
