# pylc3-examples
[![Travis CI Build Status](https://travis-ci.org/TricksterGuy/pylc3-examples.svg?branch=master)](https://travis-ci.org/TricksterGuy/pylc3-examples)

Example pylc3 testers and lc-3 assembly code for documention for pyLC3 0.9.0

The examples should be viewed in the following order.


1) [simple_add] - This example shows a basic test in which two values in labels, sums them, and stores the result at an ANSWER label. It exists as a sample test along with the code which makes the test pass.
2) [simple_sum] - This example shows another basic test which sums values in an array. This test demonstrates how pyLC3 handles modifying sequential memory addresses and how template code should be handled in regards to that.
3) [simple_string] - This example shows another basic test which deals with strings, how strings are written to memory and checked.
4) [simple_io] - This example shows how console input and console output are handled.
5) [lc3_calling_convention_basic] - This example demonstrates how pyLC3 handles testing subroutines using the lc3 calling convention described in the textbook. The test code shows a subroutine that takes a variable number of arguments and returns double the sum of the arguments.
6) [lc3_calling_convention_extra] - This example shows how to test a subroutine that takes in something other than integers. Addresses to strings and arrays are passed into the function, and special methods are used to dump data at a specific address.
7) [lc3_calling_convention_recursive] - This example shows how to test a subroutine that's recursive. More importantly how to test that subroutines are calling other subroutines correctly with the correct set of parameters.

[simple_add]: <simple_add>
[simple_sum]: <simple_sum>
[simple_string]: <simple_string>
[simple_io]: <simple_io>
[lc3_calling_convention_basic]: <lc3_calling_convention_basic>
[lc3_calling_convention_extra]: <lc3_calling_convention_extra>
[lc3_calling_convention_recursive]: <lc3_calling_convention_recursive>
