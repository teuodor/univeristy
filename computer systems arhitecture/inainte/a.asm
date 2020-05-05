bits 32 

global start
 
extern exit
extern printf 
extern secventa_maxima
             
             
import exit msvcrt.dll    
import printf msvcrt.dll


segment data use32 public class=data
    sir db 13,13h,10b,7,-3,100,101b,11h,27,-1,4
    lungime_sir_const equ $-sir
    lungime_sir db $-sir
    format_hexa db '%x, ',0
    secv times lungime_sir_const db 0
    index db 0
    lungime db 0
segment code use32 public class=code
    start:
        push dword lungime
        push dword index
        push dword lungime_sir
        push dword sir
        call secventa_maxima
        mov ecx,[lungime]
        mov ebx,[index]
        
        bucla:
            mov eax,[sir+ebx]
            inc ebx
            push eax
            push dword [format_hexa]
            call [printf]
            add esp,4*2
            loop bucla
            
            
        
        push    dword 0      
        call    [exit]       
