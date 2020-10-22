    xdef    Start, Stop, End

Start:
    bra main


main:
    suba.l  #4, a7
    move.l  #3, (a7)
    bsr func
    adda.l  #4, a7
    move.l  d0, y
    bra Stop

func:
    move.l  4(a7), d0
    cmp.l   #0, d0
    bne recurse
    move.l  #1, d0
    rts

recurse:
    sub.l   #1, d0
    suba.l   #4, a7
    move.l  d0, (a7)
    bsr func
    adda.l  #4, a7
    move.l 4(a7), d1
    muls    d1, d0
    rts

Stop:
    nop

y:  ds.l    1

End:
