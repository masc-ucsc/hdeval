
module full_adder(input [0:0] a, input [0:0] b, input [0:0] cin, output [0:0] sum, output [0:0] cout);
  assign sum = a ^ b ^ cin;  // Sum is XOR of a, b, and cin
  assign cout = (a & b) | (b & cin) | (a & cin);  // Carry out is majority function of a, b, and cin
endmodule

