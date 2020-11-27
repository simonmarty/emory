* THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
* SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. Simon Marty


        xdef BinarySearch

BinarySearch:
******************************************************
* Write your recursive binary search assembler subroutine here
*
*    BinarySearch: input stack frame (see pdf for details)
*                    
******************************************************
        * low = 12(a6)
        * high = 8(a6)
        * key = 16(a6)
        * array = 20(a6)
        
        bra f

f:
        move.l  a6, -(a7)
        movea.l a7, a6
        move.l  8(a6), d0 * d0 = high
        move.l  12(a6), d1 * d1 = low
        cmp.l   d1, d0
        blt noval
        sub.l   d1, d0 * d0 = high - low
        divs    #2, d0 
        ext.l   d0 * d0 = (high - low)//2
        add.l   d1,d0 * d0 = low + (high - low)//2 = midpoint
        move.l  d0, -(a7) * d0 is the midpoint of my subarray
        muls    #4, d0
        move.l  20(a6), a0
        move.l  (a0,d0), d0 * d1 = array[midpoint]
        cmp.l   16(a6), d0 * compare key with array[midpoint]
        beq equal
        bgt recurse_left
        bra recurse_right

cleanup:
        movea.l a6, a7
        movea.l (a7)+, a6
        rts

noval:
        move.l  #-1, d0
        bra cleanup

equal:
        move.l -4(a6), d0
        bra cleanup
         * d0 contains the index of the key

recurse_left:
        move.l  20(a6), -(a7) * pass parameter A
        move.l  16(a6), -(a7) * pass the key
        move.l  12(a6), -(a7) * pass the same lower bound
        move.l  -4(a6), d0
        sub.l   #1, d0
        move.l  d0, -(a7)
        bsr f
        bra cleanup

recurse_right:
        move.l  20(a6), -(a7) * pass parameter A
        move.l  16(a6), -(a7) * pass the key
        move.l  -4(a6), d0
        add.l   #1, d0
        move.l  d0, -(a7) * pass midpoint + 1 as lower bound
        move.l  8(a6), -(a7) * pass the same high bound
        bsr f
        bra cleanup

* *****************************************************************************
* If you need local variables, you can add variable definitions below this line
* *****************************************************************************
        end
        