; simple_io.asm
; A basic assembly program that continuously reads input from console input and
; only echos back uppercase A-Z. Input terminates with a newline character '\n'
.orig x3000
    NEXT GETC
    ADD R1, R0, -10
    BRZ DONE
    ADD R1, R1, -16
    ADD R1, R1, -16
    ADD R1, R1, -16
    ADD R1, R1, -7
    BRN NEXT
    ADD R1, R0, -16
    ADD R1, R1, -16
    ADD R1, R1, -16
    ADD R1, R1, -16
    ADD R1, R1, -16
    ADD R1, R1, -10
    BRP NEXT
    OUT
    BR NEXT
    DONE HALT
.end
