; simple_sum.asm
; A basic assembly program that sums values in an array and stores the result at 
.orig x3000
    AND R0, R0, 0
    LD R2, ARRAY_LOC
    LDI R3, ARRAY_LENGTH_LOC
    BRNZ END
    NEXT LDR R1, R2, 0
    ADD R0, R1, R0
    ADD R2, R2, 1
    ADD R3, R3, -1
    BRP NEXT
    END STI R0, ANSWER_LOC
    HALT
    ; This is a "pointer" to the memory address that contains the array length.
    ARRAY_LENGTH_LOC .fill x4000
    ; For arrays we put them at a specified location in memory. pylc3 won't
    ; write an array starting at a label due to the fact that students can add
    ; more data after the end of the array and if the code writes a big enough
    ; array that could clobber data that's already present.
    ARRAY_LOC .fill x4001
    ; We will write the answer to this memory address. [x5000]
    ANSWER_LOC .fill x5000
.end
