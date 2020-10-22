`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:09:56 09/10/2019 
// Design Name: 
// Module Name:    Lab2Problem3 
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
module Lab2Problem3(
    input A,
    input B,
    input C,
    output X,
    output Y
    );

assign X = (~A&~C) | (~A&B&C);
assign Y = ~X&C;

endmodule
