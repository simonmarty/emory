    xdef    Start, Stop, End

Start:

main:

    move.l  #3, -(a7)
    bsr fibb
    adda.l  #4, (a7)
    move.l  d0, ans
    bra End

fibb:
    move.l  a6, -(a7)
    movea.l a7, a6
    move.l 8(a6), d0    * 8(a6 is the location of N)
    cmp.l   #0, d0
    beq base_case
    cmp.l   #1, d0
    beq base_case
    
    move.l  8(a6), d0
    sub.l   #1, d0
    move.l  d0, -(a7)
    bsr fibb
    adda.l  #4, a7

    move.l  d0, -4(a6)
    move.l  8(a6), d0
    sub.l   #2, d0
    move.l  d0, -(a7)
    bsr fibb
    add.l   #-4(a6), d0
    movea.l a6, a7
    movea.l (a7)+, a6
    rts

base_case:
    move.l  #1, d0
    movea.l a6, a7
    movea.l (a7)+, a6
    rts 

Stop:


ans ds.l    1


End:
