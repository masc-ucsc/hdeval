
module FullAdder(input a, input b, input ci, output sum, output co);
    assign {co, sum} = a + b + ci;
endmodule
module RippleCarryAdder(input [3:0] a, input [3:0] b, output [4:0] sum);
    wire c1, c2, c3;

    FullAdder FA0 (a[0], b[0], 1'b0, sum[0], c1);
    FullAdder FA1 (a[1], b[1], c1, sum[1], c2);
    FullAdder FA2 (a[2], b[2], c2, sum[2], c3);
    FullAdder FA3 (a[3], b[3], c3, sum[3], sum[4]);
endmodule

