`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:57:11 09/26/2019
// Design Name:   Lab5_1
// Module Name:   C:/Users/phys234user/Documents/Luis/Lab5_1/Lab5_1Test.v
// Project Name:  Lab5_1
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: Lab5_1
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Lab5_1Test;

	// Inputs
	reg [7:0] Dbus;
	reg [2:0] Sbus;

	// Outputs
	wire [7:0] Obus;

	// Instantiate the Unit Under Test (UUT)
	Lab5_1 uut (
		.Dbus(Dbus), 
		.Sbus(Sbus), 
		.Obus(Obus)
	);

	initial begin
		// Initialize Inputs
		Dbus = 0;
		Sbus = 0;

		// Wait 100 ns for global reset to finish
		#100;
      Dbus = 171;
		#100
		Sbus = 6;
		// Add stimulus here

	end
      
endmodule

