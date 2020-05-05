bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,scanf,fscanf,fprintf,fopen,fclose,printf        ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll  
import scanf msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll  ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll              ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
format_siruri db '%s',0
format_caracter db '%c',0
format_afisare db '%s ',0
nume_input resb 10
nume_output db 'output.txt',0
descriptor_input dd -1
descriptor_output dd -1
c resd 1
mod_scris db 'w',0
mod_citire db 'r',0
cuvant resb 20
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
    push dword nume_input
    push dword format_siruri
    call [scanf]
    add esp,8
    
    push dword c
    push dword format_caracter
    call [scanf]
    add esp,8
    
    push dword mod_citire
    push dword nume_input
    call [fopen]
    add esp,8
    
    
    mov [descriptor_input],eax
    
    push dword mod_scris
    push dword nume_output
    call [fopen]
    
    mov [descriptor_output],eax
    
    citire_cuvinte:
    push dword cuvant
    push dword format_siruri
    push dword [descriptor_input]
    call [fscanf]
    
    cmp [cuvant], byte 10
    je final
    
    mov edx,0
    numar_litere:
    mov al,[cuvant+edx]
    inc edx
    cmp al,0
    jne numar_litere
    
    
    sub edx,2
    mov al,[cuvant+edx]
    mov ecx,0
    cmp al,[c]
    je afisare
   
    
    afisare:
    push dword cuvant
    push dword format_afisare
    push dword [descriptor_output]
    call [fprintf]
    jmp citire_cuvinte
    
   
    
   
    final:
    push dword [descriptor_input]
    call [fclose]
    
    push dword [descriptor_output]
    call [fclose]
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
