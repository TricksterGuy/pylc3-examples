linked_list
===

This demo just showcases a simple use of fillNode/assertNodeAt.

In pyLC3 "nodes" can be a node of any type consisting of arbitrary data.

This function can be used to create linked lists, trees, and other linked
datastructures.

This demo makes uses of the fillXXX family of functions. These functions just dump,
the type out at some address you choose. These functions can not be used if the
address has a label. The reasoning for this is that pyLC3 will just write starting at the
address given, if there is important data after the label it will get overriden resulting
in a potentially hazardous situation.

The demo just makes a linked list circular, by setting the last node's next to be the head.
