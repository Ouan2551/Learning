section .data
    message db 'Hello, world!', 0Ah ; Define a string with newline (0Ah)

section .text
    global _start
_start:
    mov eax, 4  ; system call number for write
    mov ebx, 1  ; file descriptor (stdout)
    mov ecx, message  ; address of string to write
    mov edx, 13  ; number of bytes to write
    int 0x80  ; call kernel

    mov eax, 1 ; system call number for exit
    mov ebx, 0 ; exit status
    int 0x80