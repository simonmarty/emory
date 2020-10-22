`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:09:36 09/24/2019 
// Design Name: 
// Module Name:    Lab4_2 
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
module Lab4_2(
    input [7:0] I,
    output reg O
    );

	always @ (*) begin
		if(I >= 50 && I <=60)
			O = 1;
		else
			O = 0;
	end
endmodule
