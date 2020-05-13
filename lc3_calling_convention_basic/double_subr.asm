; double_subr.asm
; A subroutine that takes a variable number of arguments on the stack and sums
; them and doubles the answer.
;
; pseudocode
;
; short double(short argc, short args ...)
;    short sum = 0;
;    for (short i = 0; i < argc; i++)
;        sum += args[i];
;    return sum * 2;

.orig x3000
    ; In assembly templates we give to students we don't give the code to set up
    ; the stack as the GUI simulator can do that via
    ; Debug > Simulate Subroutine Call.
    ;
    ; The reasoning for this is if students get that part wrong, then the whole
    ; subroutine will fail to work when tested in pylc3.


    ; Subroutine begins here. pylc3 will start executing the subroutine
    ; beginning here by satisfying the preconditions of the lc3 calling
    ; convention and then setting the PC to go here. Within pylc3 a dummy value
    ; is set in R7, and a breakpoint is set at the address given in R7. The code
    ; is ran and we know we returned correctly if the PC hits R7 and the
    ; breakpoint is triggered.
    DOUBLE
        ADD R6, R6, -3
        STR R5, R6, 0
        STR R7, R6, 1
        ADD R5, R6, -1
        AND R0, R0, 0
        ADD R2, R5, 5
        LDR R1, R5, 4
        CHECK BRZ END
        LDR R3, R2, 0
        ADD R0, R0, R3
        ADD R2, R2, 1
        ADD R1, R1, -1
        BR CHECK
        END ADD R0, R0, R0
        STR R0, R5, 3
        LDR R5, R6, 0
        LDR R7, R6, 1
        ADD R6, R6, 2
        RET
.end
