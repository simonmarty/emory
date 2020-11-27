* THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
* SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. Simon Marty

* ********************************************************************
* Do not touch the following 2 xdef lists:
* ********************************************************************
        xdef Start, Stop, End
        xdef A, B, len_a, len_b, max, min, sum, common

* ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
* You can add more xdef here to export labels to emacsim
* ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*      Put your assembler program here - between the start and stop label
*      DO NOT define any variables here - see the variable section below
* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Start:
        movea.l  #A, a0
        movea.l  #B, a1

        move.l  (a0), d0
        move.l  (a1), d1
        move.l  #0, d3

        move.l  #0, d2
        loopstart1:
        cmp.l   len_a, d2
        bge loopend1
        move.l  d2, d4
        muls    #4, d4
        move.l  (a0, d4), d4
        add.l   d4, d3
        cmp.l   d0, d4
        ble if1done
        move.l  d4, d0
        if1done:
        cmp.l   d1, d4
        bge if2done
        move.l  d4, d1
        if2done:
        add.l   #1, d2
        bra loopstart1
        loopend1:

        move.l  #0, d2
        loopstart2:
        cmp.l   len_b, d2
        bge loopend2
        move.l  d2, d4
        muls    #4, d4
        move.l  (a1, d4), d4
        add.l   d4, d3
        cmp.l   d0, d4
        ble if3done
        move.l  d4, d0
        if3done:
        cmp.l   d1, d4
        bge if4done
        move.l  d4, d1
        if4done:
        add.l   #1, d2
        bra loopstart2
        loopend2:

        move.l  d0, max
        move.l  d1, min
        move.l  d3, sum

        move.l  #0, d3 * sum
        move.l  #0, d0 * index 1
        
        loopstart3:
        move.l  #0, d1 
        cmp.l   len_a, d0
        bge loopend3  * if index 1 >= len_a end loop

        move.l  d0, d2  
        muls    #4, d2  
        move.l  (a0, d2), d2
        loopstart4:
        cmp.l   len_b, d1
        bge loopend4
        
        move.l  d1, d4
        muls    #4, d4
        move.l  (a1, d4), d4
        
        cmp.l   d2, d4
        bne skipcountup
        add.l   #1, d3
        skipcountup:
        add.l   #1, d1
        bra loopstart4
        loopend4:
        add.l   #1, d0
        bra loopstart3
        loopend3:

        move.l  d3, common


* ********************************************************************
* Do not touch the stop label - you need it to stop the program
*********************************************************************
Stop:   nop



* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*    Variable Section -   Put your variables here IF you need more
*
*    DO NOT define A, B, len_a, len_b, max, min, sum and common !!!
*    They are already defined below
*
*    You can add more variables below this line if you need them
* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





* ********************************************************************
* Adjust the arrays (and lengths) below to test different arrays
* ********************************************************************
A:      dc.l  13,3,21,1,8,5,4,23
B:      dc.l  4,8,15,16,23,42
len_a:  dc.l  8
len_b:  dc.l  6

* ********************************************************************
* Do not touch anything below this line !!!
* ********************************************************************
max:    ds.l  1
min:    ds.l  1
sum:    ds.l  1
common: ds.l  1

End:    nop
        end
