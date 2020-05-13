; mccarthy91.asm
; A recursive subroutine that takes a single arguments on the stack and returns
; 91 if n < 100 otherwise n - 10
;
; pseudocode
;
; short mccarthy91(short n)
;   if n > 100
;     return n - 10
;   else
;     return mccarthy91(mccarthy91(n + 11))

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
    MCCARTHY91
        ADD R6, R6, -3
        STR R5, R6, 0
        STR R7, R6, 1
        ADD R5, R6, -1
        LDR R0, R5, 4
        LD R1, NHUNDRED
        ADD R1, R0, R1
        BRNZ RECURSE
        ADD R0, R0, -10
        STR R0, R5, 3
        BR END
        RECURSE ADD R0, R0, 11
        ADD R6, R6, -1
        STR R0, R6, 0
        JSR MCCARTHY91
        JSR MCCARTHY91
        LDR R0, R6, 0
        ADD R6, R6, 3
        STR R0, R5, 3
        END LDR R5, R6, 0
        LDR R7, R6, 1
        ADD R6, R6, 2
        RET
        
    NHUNDRED .fill -100
.end
