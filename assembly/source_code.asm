section .data
    msg db "Hello, World!", 0

section .text
    global _start

_start:
    mov eax, 4          ; syscall number for write
    mov ebx, 1          ; file descriptor (stdout)
    mov ecx, msg        ; address of the message
    mov edx, 13         ; length of the message
    int 0x80            ; make the system call

    mov eax, 1          ; syscall number for exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; make the system call