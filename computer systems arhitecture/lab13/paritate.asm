bits 32
global _paritate
segment code public code use32
_paritate:
	push ebp
	mov ebp,esp
    
    mov eax,[ebp+8]
    and eax, 1
    not eax
    
	pop ebp
    ret