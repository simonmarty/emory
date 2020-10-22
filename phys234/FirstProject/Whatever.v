`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   13:35:15 09/05/2019
// Design Name:   moduleProjectOne
// Module Name:   C:/Users/phys234user/Documents/Luis/FirstProject/Whatever.v
// Project Name:  FirstProject
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: moduleProjectOne
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module Whatever;

	// Inputs
	reg x;
	reg y;

	// Outputs
	wire z;

	// Instantiate the Unit Under Test (UUT)
	moduleProjectOne uut (
		.x(x), 
		.y(y), 
		.z(z)
	);

	initial begin
		// Initialize Inputs
		x = 0;
		y = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		always #100 {x,y}=+1;
	end
      
endmodule

