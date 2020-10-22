`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:55:33 09/12/2019 
// Design Name: 
// Module Name:    Lab2Problem4 
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
module Lab2Problem4(
    input A,
    input B,
    input C,
    output X,
    output Y
    );

assign X = ~(A|B)^(~A|~B|C)^(A|~C);
assign Y = (~A|B)^(A|~B)^(A|C);

endmodule
