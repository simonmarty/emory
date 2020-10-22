`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:34:35 09/24/2019 
// Design Name: 
// Module Name:    Lab4_1 
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
module Lab4_1(
    input A,
    input B,
    input C,
    input D,
    input E,
    input F,
    output reg [1:0] O
    );
	 wire[2:0] sum;
	 assign sum = A + B + C + D + E + F;
	 
	 always @ (*) begin
		if(sum > 4) begin
			O[0] = 1;
			O[1] = 1;
		end else if(sum > 3) begin
			O[1] = 1;
			O[0] = 0;
		end else if(sum == 3) begin
			O[0] = 1;
			O[1] = 0;
		end
	 end


endmodule
