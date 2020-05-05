bits 32

global start        

extern exit
import exit msvcrt.dll

segment data use32 class=data
    input db 1,2,3,4,5,6,7,8
    input_length equ $-input

    src db 2,4,6
    src_length equ $-src
    src_index db 0

    dst db 12,14,16
    output times input_length db 0

segment code use32 class=code
    start:
        mov ebx,0
        mov ecx,input_length
        start_input_loop:
        
            mov al, [input + ebx]
            mov edx,0
            
            start_src_bucla:
            
                cmp al,[src+edx]
                je end_src_bucla
                cmp edx,src_length
                je papa
                inc edx
                jmp start_src_bucla
            
            
            end_src_bucla:
            mov al,[dst+edx]
            mov [input + ebx],al
            
            papa:
            
            inc ebx
            loop start_input_loop
        end_input_loop:
    
        push dword 0
        call [exit]
