bits 32

global secventa_maxima
segment code use32 public class=data
a db 2
segment code use32 public class=code
    secventa_maxima:
    mov esi,[esp+4]
    
    mov ebx,0
    mov edx,0
    bucla:
        mov eax,[esp+16]
        cmp edx,[eax]
        jb nu
        mov eax,[esp+12]    ;esp+16:= lungime, esp+12:= index
        mov [eax],ebx
        sub [eax],edx
        mov eax,[esp+16]
        mov [eax],edx
        
        
        nu:
        mov ax,0
        mov al,[esi+ebx]        
        div byte[a]
        cmp ah,1
        je impar
        jne par
        
        impar:
        inc edx
        jmp conditie_iesire
        
        
        par:
        mov edx,0
        
        conditie_iesire:
        inc ebx
        mov eax,[esp+8]
        cmp ebx,[eax]
        je final
        jmp bucla
     
     
     
    final:
    ret
    
        
        
    