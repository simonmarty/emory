`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:50:58 09/17/2019 
// Design Name: 
// Module Name:    Lab3_1 
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
module Lab3_1(
    input A,
    input B,
    input C,
    input D,
    output O
    );

assign O = ~A&~B&C | B&C&~D|~A&B&~C&D|A&~B&~C&D;
endmodule
