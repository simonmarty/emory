`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:54:39 09/12/2019
// Design Name:   Lab2Problem4
// Module Name:   C:/Users/phys234user/Documents/Luis/Lab2Problem4/Lab2Problem4Test.v
// Project Name:  Lab2Problem4
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Lab2Problem4
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Lab2Problem4Test;

	// Inputs
	reg A;
	reg B;
	reg C;

	// Outputs
	wire X;
	wire Y;

	// Instantiate the Unit Under Test (UUT)
	Lab2Problem4 uut (
		.A(A), 
		.B(B), 
		.C(C), 
		.X(X), 
		.Y(Y)
	);

	initial begin
		// Initialize Inputs
		A = 0;
		B = 0;
		C = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here

	end
      
endmodule

