lc3 calling convention_extra
===

This demo just showcases additional functions that can be used to set up tests.

The way pyLC3 likes to check subroutines is by directly calling them by moving
the PC to the subroutine label and satisfying the preconditions, as if there was a
"main method" that did it.

That means that some extra setup may be required. Suppose one of the parameters
was a pointer to an array out in memory somewhere.

This demo makes uses of the fillXXX family of functions. These functions just dump,
the type out at some address you choose. These functions can not be used if the
address has a label. The reasoning for this is that pyLC3 will just write starting at the
address given, if there is important data after the label it will get overriden resulting
in a potentially hazardous situation.

The demo doesn't do much, it just writes an integer (representing length of the following params),
string, and array to random locations. The subroutine takes each value from the array and adds it
to each corresponding character in the string. The integer read is returned.
