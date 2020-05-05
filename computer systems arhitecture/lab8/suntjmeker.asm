bits 32

global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data
    input db 1,2,3,4,5,6,7,8
    input_length equ $-input
    input_index db 0

    src db 2,4,6
    src_length equ $-src
    src_index db 0

    dst db 12,14,16
    output times input_length db 0

segment code use32 class=code
    start:
        mov ebx,0
        start_input_loop:
            mov eax, [input + ebx]

            mov ecx, [input_index]
            cmp ecx, [input_length]
            je end_input_loop
            inc ebx
            jmp start_input_loop
        end_input_loop:
    
        push dword 0
        call [exit]
