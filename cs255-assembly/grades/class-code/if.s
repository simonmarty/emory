    xdef    Start, Stop, End

Start:
    move.l  a,d0
    cmp.l   b,d0
    blt False
    muls    #2,d0
    move.l  d0,a
False:
    move.l  a,b
Stop:
    nop

a:  dc.l    15
b:  dc.l    20

End:
