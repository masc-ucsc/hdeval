
module full_adder(input [0:0] a, input [0:0] b, input [0:0] cin, output [0:0] sum, output [0:0] cout);

// Compute the sum
assign sum = a ^ b ^ cin;

// Compute the carry-out
assign cout = (a & b) | (b & cin) | (a & cin);

endmodule

