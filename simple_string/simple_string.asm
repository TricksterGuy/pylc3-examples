; simple_string.asm
; A basic assembly program that removes spaces from a string in place.
; Duplicate space characters won't be present.
.orig x3000
    AND R2, R2, 0
    AND R3, R3, 0
    
    LD R1, STRING_LOC

    NEXT ADD R4, R1, R3
    LDR R0, R4, 0
    BRZ DONE
    ADD R4, R0, -16
    ADD R4, R4, -16
    BRNP NOTSPACE
    ADD R3, R3, 1
    NOTSPACE
    ADD R4, R1, R3
    LDR R0, R4, 0
    ADD R4, R1, R2
    STR R0, R4, 0
    AND R0, R0, R0
    BRZ EXIT
    ADD R2, R2, 1
    ADD R3, R3, 1
    BR NEXT
    DONE AND R0, R0, 0
    ADD R4, R1, R2
    STR R0, R4, 0
    EXIT HALT
    ; For strings we put them at a specified location in memory. pylc3 won't
    ; write an string starting at a label due to the fact that students can add
    ; more data after the end of the string and if the code writes a big enough
    ; string that could clobber data that's already present.
    STRING_LOC .fill x4000
.end
