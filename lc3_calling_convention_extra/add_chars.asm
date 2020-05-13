; add_chars.asm
; A subroutine that takes 3 addresses all pointers to (int, string, and array)
; and adds the values in array to each char in sequence return length 

; pseudocode
;
; short add_chars(short* length, short* str, short* arr)
;    for (short i = 0; i < *length; i++)
;        str[i] += arr[i];
;    return *length;

.orig x3000
    ; In assembly templates we give to students we don't give the code to set up
    ; the stack as the GUI simulator can do that via
    ; Debug > Simulate Subroutine Call.
    ; The reasoning for this is if students get this part wrong, then the whole
    ; subroutine will fail to work when tested in pylc3.

    ; Subroutine begins here. pylc3 will start executing the subroutine
    ; beginning here by satisfying the preconditions of the lc3 calling
    ; convention and then setting the PC to go here. Within pylc3 a dummy value
    ; is set in R7, and a breakpoint is set at the address given in R7. The code
    ; is ran and we know we returned correctly if the PC hits R7 and the
    ; breakpoint is triggered.
    ADD_CHARS
        ADD R6, R6, -3
        STR R5, R6, 0
        STR R7, R6, 1
        ADD R5, R6, -1
        LDR R0, R5, 4
        LDR R1, R5, 5
        LDR R2, R5, 6
        LDR R0, R0, 0

        CHECK BRZ END

        LDR R3, R1, 0
        LDR R4, R2, 0
        ADD R3, R3, R4
        STR R3, R1, 0
        ADD R1, R1, 1
        ADD R2, R2, 1
        ADD R0, R0, -1
        BR CHECK

        END LDR R0, R5, 4
        LDR R0, R0, 0
        STR R0, R5, 3
        LDR R5, R6, 0
        LDR R7, R6, 1
        ADD R6, R6, 2
        RET
.end
