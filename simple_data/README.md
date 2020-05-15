student
===

This demo just showcases a simple use of fillData/assertDataAt.
And a little about complx's plugin system.

Whenever you want to dump an arbitrary structure of related data this is the function
to do it.

In pyLC3 these datastructures are represented as tuples.
Each element of this tuple can be one of 4 things:

1) A 16 bit integer.
2) An array of 16 bit integers.
3) A string.
4) A tuple following this format.

pyLC3 will flatten out the data and write it to sequential memory addresses. Note that
no padding or packing of these elements are done.

This demo makes uses of the fillXXX family of functions. These functions just dump,
the type out at some address you choose. These functions can not be used if the
address has a label. The reasoning for this is that pyLC3 will just write starting at the
address given, if there is important data after the label it will get overriden resulting
in a potentially hazardous situation.

The demo just prints out the name of the student in the test along with computing their grade.
The assembly code makes use of plugins in complx to run. Two plugins are used.

1) A new trap called UDIV which takes in R0 = n R1 = d and has the following effect:
  R0 = n / d
  R1 = n % d
2) A new instruction for multiplying two arguments.
  MUL DR, SR1, SR2
  MUL DR, SR1, IMM5

When the assembly code uses plugins we must be sure to tell pyLC3 to enable processing of plugins
or else the code may not assemble or have unexpected results.
