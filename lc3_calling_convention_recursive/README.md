lc3 calling convention_recursive
===

This demo just showcases how to check a subroutine that uses the lc3 calling
convention that is recursive.

The lc3 calling convention just specifies how parameters are passed to
subroutines, which the parameters are pushed onto the stack in opposite order
and then you JSR to the subroutine. That means that R6 will point to the first
parameter.

At the time we return from the subroutine R6 will point to the answer followed
by the parameters from that subroutine.

This demo demonstrates a subroutine that is recursive with a single argument,
the famous McCarthy91 function which always returns 91. This demo will show how
to expect a particular subroutine call that must be made to ensure the high
level code is followed.
