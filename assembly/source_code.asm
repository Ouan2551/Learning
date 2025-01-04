section .data
    message db "Hello, world!", 10  ; Define a message string

section .text
    global _start

_start:
    mov rax, 1        ; System call number for write
    mov rdi, 1        ; File descriptor 1 (stdout)
    mov rsi, message   ; Address of the message string
    mov rdx, 13       ; Length of the message string
    syscall           ; Invoke the system call

    mov rax, 60       ; System call number for exit
    mov rdi, 0        ; Exit code 0 (success)
    syscall           ; Invoke the system call