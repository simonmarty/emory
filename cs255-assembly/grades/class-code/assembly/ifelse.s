    xdef Start, Stop, End

Start:
    move.l  a,d0
    cmp.l   b,d0
    blt Else    * if a < b

    muls #2, d0
    move.l  d0,a
    bra Continue
Else:
    move.l  b,d0
    muls    #2, d0
    move.l  d0, b

Continue:
    move.l  a,b
Stop:
    nop

End: