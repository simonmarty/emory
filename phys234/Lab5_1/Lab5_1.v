`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:45:45 09/26/2019 
// Design Name: 
// Module Name:    Lab5_1 
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
module Lab5_1(
    input [7:0] Dbus,
    input [2:0] Sbus,
	 output reg [7:0] Obus
    );
	 
always @ (*) begin
	case(Sbus) 
		0: Obus = Dbus;
		1: Obus = {1'b0, Dbus[7:1]};
		2: Obus = {Dbus[6:0], 1'b0};
		3: Obus = {Dbus[0:0], Dbus[7:1]};
		4: Obus = {Dbus[6:0], Dbus[7:7]};
		5: Obus = {Dbus[7:7],Dbus[7:7], Dbus[6:1]};  
		6: Obus = {Dbus[1:0], Dbus[7:2]};
		7:	Obus = Dbus;
	endcase


end
endmodule
