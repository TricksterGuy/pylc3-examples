.orig x3000
    LD R0, A ; load params
    LD R1, B
    ADD R2, R0, R1 ; do computation
    ST R2, ANS ; write result
    HALT

    ; Parameters, these values will be written to from within pylc3.
    A .blkw 1
    B .blkw 1
    ; It is important to use .blkw here over a .fill as .blkw will allow randomization of the value.
    ; .fill's will always have the value at that location.
    ; The reasoning for this is sometimes if you do a .fill 0 and a student doesn't know how to clear
    ; a register they will instead load from this location.
    ANS .blkw 1
.end
