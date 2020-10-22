    xdef Start, Stop, End

Start:
    move.l  #4, a

Loop:
    move.l  a,  d0
    cmp.l   #0, d0
    ble Loop_End

    move.l  a, d0
    sub.l   #1, d0
    move.l  d0, a

    bra Loop
Loop_End:
    move.l  a, b
Stop:
    nop

a:  dc.l    4
b:  ds.l    1
End:
    end
