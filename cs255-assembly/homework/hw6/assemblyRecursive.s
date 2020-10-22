    xdef Start, Stop, End
    xdef f

Start:

main:
    move.l #5, -(a7)
    bsr f

    adda.l #4, a7
    move.l d0, y
    bra Stop

f:
    move.l a6, -(a7)
    movea.l a7, a6
    suba.l #4, a7


    move.l 8(a6), d0
    cmp.l #0, d0
    bne recurse
    * Return 1
    move.l #1, d0
    bra cleanup

recurse:
    sub.l #1, d0  * Change d0 to x-1
    move.l d0, -(a7)
    bsr f

    adda.l #4, a7

    move.l d0, -4(a6)
    move.l 8(a6), d1
    muls d1, d0
    move.l d0, -4(a6)

cleanup:
    movea.l a6, a7
    movea.l (a7)+, a6
    rts

Stop:
    nop

y:  ds.l 1

End:
    end
