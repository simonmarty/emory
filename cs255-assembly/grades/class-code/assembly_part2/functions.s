    xdef Start, Stop, End

Start:

main:
    move.l  #5, x
    bsr function
    bsr function
    bra Stop

function:
    move.l x,d0
    add.l   #1, d0
    move.l  d0, x
    rts
Stop:
    nop

x: dc.l 0

End:
