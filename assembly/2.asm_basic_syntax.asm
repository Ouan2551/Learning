; have 3 sections
; data_section, bss_section, text_section
; 1) data_section => declaring data or constants etc. (use for declare)
;   "section.data" ; declare section
; 2) bss_section => declaring variables
;   "section.bss"

; 3) text_section => actual code start with "global_start" tell that execution run first over there
;   "section.text
;       global _start
;   _start:"
; comment just use ";"

; syntax_language
; format => [label] mnemonic [operands] [;comment]
; mnemonic is instruction tell program to do something

; examples
section.text
    global _start ;declare for linker

_start: ; tell linker entry point
    mov edx,len ; message length
    mov ecx,msg ; message to write
    mov edx,1 ; file descriptor
    mov eax,4 ; system call number (write)
    int 0x80 ; call kernel

    mov eax,1 ; system call number (exit)
    int 0x80 ;call kernel

section .data
msg db 'Hello world', 0xa ; string to write
len equ $ - msg ; length of string