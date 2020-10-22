`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:59:56 10/10/2019 
// Design Name: 
// Module Name:    Main 
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
module Main(
    input Btn1,
    input Btn2,
    input Btn3,
    input Btn4,
	 
	 output reg [2:0] L1,
	 output reg [2:0] L2,
	 output reg [2:0] L3,
	 output reg [2:0] L4,
	 
	 //output reg Spk,
	 
    input setVal,
    input Test,
	 input Reset
    );
	
	reg [1:0] White = 2'b00;
	reg [1:0] Red = 2'b00;
	reg [7:0] store = 8'b00000000;
		
	
	always @ (posedge setVal) begin
		store <= {L1,L2,L3,L4};
	end
	
	
	always @ (posedge Reset) begin
		store <= 2'b00;
		White <= 2'b00;
		Red <= 2'b00;
	end
	
	//always @(posedge clk or posedge Btn1) begin
    // detect rising edge
    //if (Btn1old != Btn1 && Btn1 == 1'b1)
        //  button_raise <= 1'b1
    //button_old <= button;
    // increment number
    //if(button_raise == 1b'1)
	 
	always @ (posedge Btn1) begin
		L1 <= L1 + 1;
	end
	
	always @ (posedge Btn2) begin
		L2 <= L2 + 1;
	end
	
	always @ (posedge Btn3) begin
		L3 <= L3 + 1;
	end
	
	always @ (posedge Btn4) begin
		L4 <= L4 + 1;
	end

endmodule
