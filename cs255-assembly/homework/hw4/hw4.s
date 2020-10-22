* Collaboration Statement:
* THIS  CODE  WAS MY OWN WORK , IT WAS  WRITTEN  WITHOUT  CONSULTING  ANY
* SOURCES  OUTSIDE  OF  THOSE  APPROVED  BY THE  INSTRUCTOR. Simon Marty
*
	xdef Start, Stop, End
	xdef Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
	xdef A, B, C
	xdef i, j, k
	xdef head
	xdef ans_b, ans_w, ans_l

Start:
*******************************************************************
* Put your assembler instructions here
* Write the answer to each question after the corresponding label.
* DO NOT REMOVE ANY LABEL IN THIS ASSIGNMENT
* *** Failure to do so will result in point dedections !!! ***
*******************************************************************


*         ans_b = A[8];	
Q1:
	movea.l	#A,a0
	move.b	8(a0), ans_b
	
*         ans_l = B[3];	
Q2:
	movea.l	#B, a0
	move.w	6(a0), d0
	ext.l	d0
	move.l	d0, ans_l

*         ans_l = C[k];	
Q3:
	move.l	k,d0
	muls	#4,d0
	movea.l	#C,a0
	move.l	(a0, d0), ans_l

*         ans_w = A[k + 2]; 
Q4:
	move.l	k,d0
	add.l	#2,d0
	movea.l	#A,a0
	move.b	(a0, d0), d1
	ext.w	d1
	move.w	d1, ans_w

*         ans_w = C[i * k]; 
Q5:
	movea.l	#C,a0
	move.l	k,d0
	move.b	i,d1
	ext.w	d1
	muls	d1,d0
	muls	#4, d0
	move.l	(a0, d0), d0
	move.w	d0, ans_w

*         ans_l = B[k+1] / A[i-1]; 
Q6:
	movea.l	#A, a0
	movea.l	#B, a1
	move.l	k, d0
	add.l	#1, d0
	muls	#2, d0

	move.b	i,d1
	ext.l	d1
	sub.l	#1,	d1
	
	move.w	(a1, d0), d0
	ext.l	d0
	move.b	(a0, d1), d1
	ext.l	d1
	
	divs	d1, d0
	ext.l d0
	move.l d0, ans_l

*         ans_l = B[A[i + 5] - 80]; 
Q7:
	move.b	i, d0
	ext.l	d0
	add.l	#5, d0
	movea.l	#A, a0
	move.b	(a0, d0), d0
	ext.l	d0
	sub.l	#80, d0
	muls	#2, d0
	movea.l	#B, a0
	move.w	(a0, d0), d0
	ext.l	d0
	move.l	d0, ans_l

*         ans_w = B[20]; 
Q8:
	movea.l	#B,a0
	move.w	40(a0), ans_w

*	  ans_l = head.value2;
Q9:
	movea.l	head, a0
	move.w	4(a0), d0
	ext.l	d0
	move.l	d0, ans_l	
		


*	  ans_w = head.next.next.value1;
Q10:
	move.l	head, a0
	move.l	6(a0), a0
	move.l	6(a0), a0
	move.w	2(a0), ans_w

*************************************************
* Don't write any code below this line
*************************************************

Stop:	nop
	    nop

*************************************************
* Don't touch these variables
* You do NOT need to define more variables !!!
*************************************************

************************************************************************
* Note the use of the even directive to locate the variables ans_w and j
* at an EVEN address due to the variables ans_b and i being bytes
* Short and int variables MUST start on an even address (or you 
* will get an "odd address" error)
************************************************************************

ans_b: ds.b 1
	   even
ans_w: ds.w 1
ans_l: ds.l 1

i:     dc.b  2
	   even
j:     dc.w  4
k:     dc.l  3

A:     dc.b   -11, 22, -33, 44, -55, 66, -77, 88, -99, 109

B:     dc.w   111, -222, 333, -444, 555, -666, 777, -888, 999, -5191

C:     dc.l   1111, -2222, 3333, -4444, 5555, -6666, 7777, -8888, 9999, -9983


head:   dc.l  list1

list3:  dc.l 2468
        dc.w 88
	dc.l list4
list2:  dc.l 1470
        dc.w 78
	dc.l list3
list4:  dc.l 4567
        dc.w 65
	dc.l list5
list1:  dc.l 1357
        dc.w 98
	dc.l list2
list5:  dc.l 9876
        dc.w 54
	dc.l 0


End:
	end

