`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:55:29 09/24/2019
// Design Name:   Lab4_1
// Module Name:   C:/Users/phys234user/Documents/Luis/Lab4_1/Lab4_1Test.v
// Project Name:  Lab4_1
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Lab4_1
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Lab4_1Test;

	// Inputs
	reg A;
	reg B;
	reg C;
	reg D;
	reg E;
	reg F;

	// Outputs
	wire [1:0] O;

	// Instantiate the Unit Under Test (UUT)
	Lab4_1 uut (
		.A(A), 
		.B(B), 
		.C(C), 
		.D(D), 
		.E(E), 
		.F(F), 
		.O(O)
	);

	initial begin
		// Initialize Inputs
		A = 1;
		B = 1;
		C = 1;
		D = 1;
		E = 1;
		F = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here

	end
      
endmodule

