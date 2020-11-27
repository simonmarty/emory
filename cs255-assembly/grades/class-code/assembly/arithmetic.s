    xdef Start, Stop, End
    xdef Mistakes, Multiplication,Div

Start:
* Instructions go here
    add.w datas, d0 *d0 = 15
    add.w datas, d0 *d0 = 30
    sub.w   #10, d0 *d0 = 20, result: d0 - 10
Mistakes:
    add.w datab, d1
    add.w datai, d1

Multiplication:
    move.w #10, d0
    move.l #-1, d1
    MOVE.W #20,d1
    muls d0,d1

Div:
    move.l #10,d1
    divs #3, d1
    * Move quotient
    move.w d1, datas
    * Move remainder
    swap d1
    move.w d1, datas

Stop:
    nop
* Declaring variables goes here
datab:  ds.b    1
datas:  dc.w    1500
rem:    ds.w    1
datai:  dc.l    -25
End:
