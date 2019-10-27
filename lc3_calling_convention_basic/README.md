lc3 calling convention_basic
===

This demo just showcases how to check a subroutine that uses the lc3 calling
convention.

The lc3 calling convention just specifies how parameters are passed to
subroutines, which the parameters are pushed onto the stack in opposite order
and then you JSR to the subroutine. That means that R6 will point to the first
parameter.

At the time we return from the subroutine R6 will point to the answer followed
by the parameters from that subroutine.

This demo demonstrates a subroutine with a variable number of arguments and it
simply sums all of the parameters and returns double that.
