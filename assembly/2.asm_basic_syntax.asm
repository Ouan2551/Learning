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
; 2.asm_basic_syntax.asm - Windows 64-bit version using printf

default rel

section .data
    msg db "Hello, world", 0xa, 0
    ; NULL-terminated string for printf

section .text
    global main
    extern printf

main:
    lea rcx, [msg]      ; first argument (Windows x64 uses rcx)
    call printf         ; call C printf
    mov eax, 0
    ret