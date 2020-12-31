# pylc3-examples

Example pylc3 testers and lc-3 assembly code for documention for pyLC3 0.11.1

The examples should be viewed in the following order.


1) [simple_add] - This example shows a basic test in which two values in labels, sums them, and stores the result at an ANSWER label. It exists as a sample test along with the code which makes the test pass.
2) [simple_sum] - This example shows another basic test which sums values in an array. This test demonstrates how pyLC3 handles modifying sequential memory addresses and how template code should be handled in regards to that.
3) [simple_string] - This example shows another basic test which deals with strings, how strings are written to memory and checked.
4) [simple_io] - This example shows how console input and console output are handled.
5) [simple_data] - This example shows how to write arbitrary data out to memory (datastructures, structs, records) and how to also check arbitrary datastructures in memory.  This method is preferred when you have several related data fields and you want to group them. The example also demonstrates an assembly program with plugins are how pyLC3 handles plugins.
6) [linked_list] - This example has a test with a linked list. It follows from the simple_data test in that pyLC3 can also write nodes into memory. Nodes can also contain arbitrary data and multiple next addresses, so it can be extended to other linked datastructures such as trees, skiplists, etc.
7) [lc3_calling_convention_basic] - This example demonstrates how pyLC3 handles testing subroutines using the lc3 calling convention described in the textbook. The test code shows a subroutine that takes a variable number of arguments and returns double the sum of the arguments.
8) [lc3_calling_convention_extra] - This example shows how to test a subroutine that takes in something other than integers. Addresses to strings and arrays are passed into the function, and special methods are used to dump data at a specific address.
9) [lc3_calling_convention_recursive] - This example shows how to test a subroutine that's recursive. More importantly how to test that subroutines are calling other subroutines correctly with the correct set of parameters.
10) [subroutine_pass_by_regs] - This example shows how to test a subroutine using pass by registers rather than the lc3 calling convention. The example is a pass by registers version of the above example.

[simple_add]: <simple_add>
[simple_sum]: <simple_sum>
[simple_string]: <simple_string>
[simple_io]: <simple_io>
[simple_data]: <simple_data>
[linked_list]: <linked_list>
[lc3_calling_convention_basic]: <lc3_calling_convention_basic>
[lc3_calling_convention_extra]: <lc3_calling_convention_extra>
[lc3_calling_convention_recursive]: <lc3_calling_convention_recursive>
[subroutine_pass_by_regs]: <subroutine_pass_by_regs>
