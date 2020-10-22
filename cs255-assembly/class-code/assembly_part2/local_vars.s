    xdef    Start, Stop, End

Start:
* Order
* Local vars
* return address
* parameters
main:
     * x is below y

    move.l  #1, -(a7)

    move.l  #2, -(a7)

    bsr g

    adda.l  #8, a7
    move.l  d0, d
    bra Stop

g:
    move.l  a6, -(a7)
    movea.l a7, a6
    suba.l  #8, a7

    move.l  12(a6), d0
    add.l   #1, d0
    move.l  d0, -4(a6)
    move.l  8(a6), d1 * 4(a7) is a
    add.l   #1, d1
    move.l  d1, -8(a6)
    muls    d0, d0
    muls    d1, d1
    add.l   d1, d0
    movea.l a6, a7
    movea.l (a7)+, a6
    rts
Stop:
    nop

d:  ds.l

End
    end


    * How to use a6
    *
    *
    * b
    * a
    * old a6, a6 points here
    *return address
    * y
    * x