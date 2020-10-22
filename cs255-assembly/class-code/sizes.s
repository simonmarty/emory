xdef Start, Stop, End

Start:
    move.l #-1, d0
    move.l #-1, d1

* Want to add a + b
    move.w a,d0
    move.l b, d1
    ext.l d0
    add.l b,d0
Stop:
    nop

a:  dc.w    15
b:  dc.l    50000

End:
    end
