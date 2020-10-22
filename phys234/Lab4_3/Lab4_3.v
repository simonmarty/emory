`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:36:07 09/26/2019
// Design Name:   Lab2_3
// Module Name:   C:/Users/phys234user/Documents/Luis/Lab4_3/Lab4_3.v
// Project Name:  Lab4_3
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Lab2_3
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Lab4_3;

	// Inputs
	reg [7:0] I;

	// Outputs
	wire [7:0] O;

	// Instantiate the Unit Under Test (UUT)
	Lab2_3 uut (
		.I(I), 
		.O(O)
	);

	initial begin
		// Initialize Inputs
		I = 0;

		// Wait 100 ns for global reset to finish
		#100;
      I = 120;
		// Add stimulus here

	end
      
endmodule

