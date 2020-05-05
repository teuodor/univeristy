bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit        
extern fopen, fprintf, fclose, scanf, minim
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll       ; tell nasm that exit exists even if we won't be defining it



import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 public class=data
    ; ...
    sir times 50*4 db 0
    format_citire db '%d',0
    format_print db '%x',0
    mod_acces db 'w',0
    nume_fisier db 'min.txt',0
    descriptor_fisier dd -1
; our code starts here
segment code use32 public class=code
    start:
        ; ...
        mov eax,sir
        mov ecx,0
        sub eax,4
        
        continua:
            inc ecx
            add eax,4
            pushad
            
            push eax
            push dword format_citire
            call [scanf]
            add esp,4*2
            
            popad
            
        cmp dword[eax],0
        jne continua
        
    dec ecx
    
    
        push dword ecx
        push dword sir
        call minim
        
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp,4*2
        
        mov [descriptor_fisier],eax
        cmp eax,0
        je final
        
        push dword ebx
        push dword format_print
        push dword [descriptor_fisier]
        call [fprintf]
        add esp,4*3
        
        
        
        ; exit(0)
    final:
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
