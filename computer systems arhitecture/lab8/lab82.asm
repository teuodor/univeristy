bits 32 


global start        


extern fread
extern fopen
extern fclose
extern fprintf
extern fclose
extern exit       
        
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll     

segment data use32 class=data
    ; ...
    nume db 'lab82.txt',0
    mod_acces1 db 'w',0
    descriptor dd -1
    buffer times 16 db 0
    nr_car_citite dd -1
    text db '0vc3vc4vc5',0

    
segment code use32 class=code
    start:
        ; ...
 
    mov edi,text
    mov ebx,0
    bucla1:
        cmp byte[edi+ebx],0
        je fin
        cmp byte[edi+ebx],'0'
        jb sf_bucla
        cmp byte[edi+ebx],'9'
        ja sf_bucla
        mov byte[edi+ebx],'C'
        sf_bucla:
        inc ebx
        jmp bucla1
    
    fin:
    
    push dword mod_acces1
    push dword nume
    call [fopen]
    add esp,4*2
    
    
    mov [descriptor],eax
    cmp eax,0
    je final
    

    push dword text
    push dword [descriptor]
    call [fprintf]
    add esp,4*2
    
    push dword [descriptor] 
    call [fclose]
    add esp,4
    
    
    final:
    push    dword 0      
    call    [exit]      
