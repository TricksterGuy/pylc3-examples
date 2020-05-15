; The following are special lines in complx's assembler telling the assembler to load a plugin.

; Plugin lc3_udiv grants the student a new trap called UDIV (callable via UDIV or TRAP x80)
; UDIV takes the values in R0 and R1 and the following is done.
; R0 = R0 / R1
; R1 = R0 % R1
; When stepped through the calculation is immediately done upon executing.

; Plugin lc3_multiply grants the student a new instruction called MULT (replacing the unused opcode D)
; Its syntax is similar to the ADD instruction except it computes
; DR = SR1 * SR2 or DR = SR1 * SEXT(IMM5)

;@plugin filename=lc3_udiv vector=x80
;@plugin filename=lc3_multiply

; student.asm
; A program to grade a student.

; pseudocode
; struct Student {
;   char* name;
;   short num_tests;
;   short num_homeworks;
;   short tests[];
;   short homeworks[];
;   short grade;
; }
; def grade_student(student)
;   print student.name
;   sum_tests = 0
;   for (short i = 0; i < student.num_tests; i++)
;     sum_tests += student.tests[i]
;   sum_hws = 0
;   for (short i = 0; i < student.num_homeworks; i++)
;     sum_hws += student.homeworks[i]
;   student.grade = ((sum_tests / student.num_tests) * 30 + (sum_hws / student.num_homeworks) * 70) / 100

.orig x3000
        LD R0, STUDENT
        PUTS
CHECK   LDR R7, R0, 0
        BRZ DONE
        ADD R0, R0, 1
        BR CHECK
DONE    ADD R2, R0, 1
        LDR R3, R2, 0 ; num tests
        LDR R4, R2, 1 ; num hws
        ADD R2, R2, 2
        AND R0, R0, 0
ADD_T   LDR R5, R2, 0
        ADD R0, R0, R5
        ADD R2, R2, 1
        ADD R3, R3, -1
        BRP ADD_T
        LD R1, TEST_F
        MUL R0, R0, R1
        ADD R6, R0, 0
        AND R0, R0, 0
ADD_HW  LDR R5, R2, 0
        ADD R0, R0, R5
        ADD R2, R2, 1
        ADD R4, R4, -1
        BRP ADD_HW
        LD R1, HW_F
        MUL R0, R0, R1
        ADD R0, R0, R6
        LD R1, HUNNIT
        UDIV
        STR R0, R2, 0
        HALT
STUDENT .fill x4000
TEST_F  .fill 10 ; 10 * 3 = 30
HW_F    .fill 14 ; 14 * 5 = 70
HUNNIT  .fill 100
.end
