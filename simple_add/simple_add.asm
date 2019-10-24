; simple_add.asm
; A basic assembly program that loads from two parameters stored in A and B
; adds them and stores the result at ANS.
.orig x3000
    LD R0, A ; load params
    LD R1, B
    ADD R2, R0, R1 ; do computation
    ST R2, ANS ; write result
    HALT

    ; Parameters, these values will be written to from within pylc3.
    ; These can be changed to .fill pylc3 will overwrite them just before the
    ; code is ran.
    A .blkw 1
    B .blkw 1
    
    ; For the ANS label however...
    ; It is important to use .blkw here over a .fill as a correct implementation
    ; of .blkw will allow randomization of the value. .fill's will always have
    ; the value at that location.

    ; The reasoning for this is sometimes if you do a .fill 0 and a student
    ; doesn't know how to clear a register they will instead load from this
    ; location. Treated as a lesson on initialization.
    ANS .blkw 1
.end
