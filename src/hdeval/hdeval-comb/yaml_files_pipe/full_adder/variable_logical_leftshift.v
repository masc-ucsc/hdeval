
module variable_logical_leftshift(input [4:0] shift_n_i, input [31:0] val_i, output [31:0] result_o);
    
    assign result_o = (shift_n_i == 5'd0)  ? val_i :
                      (shift_n_i == 5'd1)  ? val_i << 1 :
                      (shift_n_i == 5'd2)  ? val_i << 2 :
                      (shift_n_i == 5'd3)  ? val_i << 3 :
                      (shift_n_i == 5'd4)  ? val_i << 4 :
                      (shift_n_i == 5'd5)  ? val_i << 5 :
                      (shift_n_i == 5'd6)  ? val_i << 6 :
                      (shift_n_i == 5'd7)  ? val_i << 7 :
                      (shift_n_i == 5'd8)  ? val_i << 8 :
                      (shift_n_i == 5'd9)  ? val_i << 9 :
                      (shift_n_i == 5'd10) ? val_i << 10 :
                      (shift_n_i == 5'd11) ? val_i << 11 :
                      (shift_n_i == 5'd12) ? val_i << 12 :
                      (shift_n_i == 5'd13) ? val_i << 13 :
                      (shift_n_i == 5'd14) ? val_i << 14 :
                      (shift_n_i == 5'd15) ? val_i << 15 :
                      (shift_n_i == 5'd16) ? val_i << 16 :
                      (shift_n_i == 5'd17) ? val_i << 17 :
                      (shift_n_i == 5'd18) ? val_i << 18 :
                      (shift_n_i == 5'd19) ? val_i << 19 :
                      (shift_n_i == 5'd20) ? val_i << 20 :
                      (shift_n_i == 5'd21) ? val_i << 21 :
                      (shift_n_i == 5'd22) ? val_i << 22 :
                      (shift_n_i == 5'd23) ? val_i << 23 :
                      (shift_n_i == 5'd24) ? val_i << 24 :
                      (shift_n_i == 5'd25) ? val_i << 25 :
                      (shift_n_i == 5'd26) ? val_i << 26 :
                      (shift_n_i == 5'd27) ? val_i << 27 :
                      (shift_n_i == 5'd28) ? val_i << 28 :
                      (shift_n_i == 5'd29) ? val_i << 29 :
                      (shift_n_i == 5'd30) ? val_i << 30 :
                      (shift_n_i == 5'd31) ? val_i << 31 :
                                             32'b0;
    
endmodule

