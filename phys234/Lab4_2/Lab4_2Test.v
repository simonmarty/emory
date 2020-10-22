`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   14:13:49 09/24/2019
// Design Name:   Lab4_2
// Module Name:   C:/Users/phys234user/Documents/Luis/Lab4_2/Lab4_2Test.v
// Project Name:  Lab4_2
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Lab4_2
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Lab4_2Test;

	// Inputs
	reg [7:0] I;

	// Outputs
	wire O;

	// Instantiate the Unit Under Test (UUT)
	Lab4_2 uut (
		.I(I), 
		.O(O)
	);

	initial begin
		// Initialize Inputs
		I = 0;

		// Wait 100 ns for global reset to finish
		#100;
		I = 50;
        
		// Add stimulus here

	end
      
endmodule

