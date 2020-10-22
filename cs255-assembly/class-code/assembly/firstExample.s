    xdef Start, Stop, End, Label


Start:
    MOVE.B #10,x
    MOVE.W #z, a0       * Immediate addressing: number z[0]
    MOVE.W (a0), d0
    MOVE.W 2(a0), d1
    MOVEA.W #y, a0

Label:  MOVE.B x,d2

Stop:
    NOP
x:  ds.b    2 * 1 is the number of "blocks"
    even      * x points to the first byte
y:  dc.w    1 * 1 is initial value
w:  ds.w
z:  dc.w    1,2,3,4,5 * Makes a word array, z points to the first byte
End:
