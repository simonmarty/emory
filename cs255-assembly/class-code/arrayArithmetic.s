* arrayArithmetic

    xdef Start, Stop, End

Start:
* a[i] = i foreach i
    move.l  #a, a0

    move.l  #0, (a0)
    move.l  #1, 4(a0)
    move.l  #2, 8(a0)
    move.l  #3, 12(a0)
    move.l  #4, 16(a0)

Stop:
    nop


* Create an array of ints (length 5)
a:    ds.l    5

End:
    end
