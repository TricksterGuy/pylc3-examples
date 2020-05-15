linked_list
===

This demo just showcases a simple use of fillNode/assertNodeAt.

In pyLC3 "nodes" can be a node of any type consisting of arbitrary data.

This function can be used to create linked lists, trees, and other linked
datastructures.

For the data for these nodes, it is represented as a tuple.
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

The demo just makes a linked list circular, by setting the last node's next to be the head.
