    xdef Start, Stop, End
    xdef Label

Start:

 *   move.l  a,d0
  *  cmp.l b, d0

* Six conditional branching instructions
* one for each of the six comparisons
* Format: bXX <address>
* beq
* bne   a - b != 0, --> Z = 0 or 1
* blt less than
* ble less than or equal
* bgt
* bge

* bra <address to jump to> unconditional

    move.l  a, d0
    move.l  b, d1
    cmp.l   d1, d0  * d0 - d1
    blt Label
    bra Stop
    add.l   d0, d1
Label:
    move.l  d1, a
Stop:
    nop

a:  dc.l    15
b:  dc.l    20

End:
    end
    