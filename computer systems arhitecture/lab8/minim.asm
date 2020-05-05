bits 32
segment code use 32 public code
global minim
minim:
    mov esi,[esp+4]
    mov ecx,[esp+8]
    mov ebx,[esi]
    repeta:
        lodsd
        cmp eax,ebx
        ja nu
        xchg eax,ebx
        nu:
        loop repeta
        
        ret 