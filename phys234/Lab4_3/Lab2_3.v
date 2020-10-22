`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:34:42 09/26/2019 
// Design Name: 
// Module Name:    Lab2_3 
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
module Lab2_3(
    input [7:0] I,
    output reg [7:0] O
    );

always @(*) begin
	O = ~I + 1;
end

endmodule
