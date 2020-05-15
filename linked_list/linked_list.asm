; linked_list.asm
; A program to make a linked list circular.

; pseudocode
; def circular(ll)
;   head = curr = ll[0]
;   return if head == 0
;   while (curr)
;     next = curr.next
;     if next == 0
;       curr.next = head
;     curr = next 


.orig x3000
        LD R0, LL
        ADD R1, R0, 0
        BRZ DONE
        BRNP 1
MOVE    ADD R0, R2, 0
        LDR R2, R0, 0
        BRNP MOVE
        STR R1, R0, 0
DONE    HALT

; Parameters, these values will be written to from within pylc3.
; This can be changed to be ".fill" instead. pyLC3 will overwrite them just before the
; code is ran.
LL      .blkw 1

.end
