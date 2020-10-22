`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:47:47 09/10/2019 
// Design Name: 
// Module Name:    Gates 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module Gates(input A, input B, input C, input D, output X, output Y);
	 assign X=(~A&~C)|(~C&D)|(~A&B)|(A&~B&D);
	 assign Y=(A|B|~C)&(~A|C|D)&(~A|~B|~C);

endmodule
