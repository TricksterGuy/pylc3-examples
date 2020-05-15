import pyLC3
import unittest
import collections

# Changed in 0.9.0, MemoryFillStrategy is now in the pyLC3 module.
#from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
import pyLC3.pylc3 as pyLC3Constants
# Changed in 0.9.0, This was used by TAs at georgia tech to name test cases
# this mechanism is now integrated with the soft assertion system.
#from decorators import parameterize
from parameterized import parameterized

# It is required to have a namedtuple for verifying the node's data.
# Since node's in pyLC3 can have any arbitrary data as storage, this
# is to have nicer output informing the students which fields are
# incorrect.  
NodeData = collections.namedtuple('NodeData', 'data')

class LinkedListTest(pyLC3.LC3UnitTestCase):

    @parameterized.expand([
        # [[Node addresses per Node], [Data per Node]]
        [[0x5000]                , [11]],
        [[0x4000, 0x40A0, 0x4010], [32, 10, 11]],
        [[0x60B0, 0x61C0, 0x6110, 0x6210, 0x6505], [32, 10, 11, 23, 77]],
    ])
    def testLinkedList(self, node_nexts, node_data):
        #-----------------------------------------------------------------------
        # Test setup
        #-----------------------------------------------------------------------
        # New in 0.9.0. For soft assertions to work, it is required to set
        # self.display_name to the name of the specific test case.
        # At the end of the test a JSON file is generated with all the results.
        # and partial credit can be rewarded for specific assertions and test
        # case name.
        self.display_name = 'circular(%s)' % '->'.join('x%04x(%d)' % elem for elem in zip(node_nexts, node_data))

        #-----------------------------------------------------------------------
        # Initialization / Loading Step
        #-----------------------------------------------------------------------
        # At this step we initialize the lc-3 and specify how memory is
        # initialized. We may also set various attributes of the lc-3 such as:
        # if we are using the 2019 revision of the lc-3, whether to enable
        # interrupts, and other things.
        # ----------------------------------------------------------------------
        
        # Initialize lc-3 state.
        # Three options for initialization based on MemoryFillStrategy
        # 1) Fill with a specified value.
        # 2) Choose a single random value and fill memory with it.
        # 3) Give every memory address a random value.

        # Here option 2 is done and every memory address gets a random value.
        # 10 here is the random seed used.
        self.init(pyLC3Constants.MemoryFillStrategy.single_random_value_fill, 10)

        # Load the assembly file, if it fails to load then the test fails.
        self.loadAsmFile('linked_list.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------

        # Setup our linked list "node_nexts" is a list of addresses of the nodes
        # with each address being linked to the address afterward.
        for i, (next_addr, data) in enumerate(zip(node_nexts, node_data)):
            n = 0 if i + 1 == len(node_nexts) else node_nexts[i + 1]
            # Sets a node at address next_addr whose next pointer is n
            # And data is a single integer in data.

            # We use the named_tuple we created above to make calling this
            # function easier. Alternatively we could just pass (data,).

            # Nodes in pyLC3 can contain arbitrary data, this is to make the
            # function useful in many applications. The nodes can also have
            # multiple next addresses.

            # This will set:
            #   MEM[next_addr] = n
            #   MEM[next_addr + 1] = data
            self.fillNode(next_addr, n, NodeData(data))

        # Set label for student to find the first node.
        self.setValue("LL", node_nexts[0])

        #-----------------------------------------------------------------------
        # Run Step
        #-----------------------------------------------------------------------
        # Run the students code. You can pass in a number of instructions to
        # execute. With no params though it will run until it halts (via a halt
        # statement, an error occurs explained below, or until
        # DEFAULT_MAX_EXECUTIONS instructions have executed).
        self.runCode()

        #-----------------------------------------------------------------------
        # Assert Postconditions Step
        #-----------------------------------------------------------------------
        # Lastly we check the state of the lc-3 after the code has ran and
        # finished. The first thing that you want to do is check if the lc-3
        # has halted cleanly and no warning messages were produced. You then
        # check all of the postconditions.
        #
        # Again it is important that the underlying lc-3 state be used for
        # assertions, and only use the assertions provided by the
        # lc3_unit_test_case class as those methods will produce the replay
        # string when an assertion fails.

        # This first assertion checks if the code HALTed cleanly.
        # The underlying C++ library (liblc3) has a mode where if the simulator
        # executes an invalid instruction the simulator will end the program.
        # This checks if the lc-3 was halted via a HALT instruction.
        
        # A note on fatal vs hard vs soft assertions, by default failing this
        # assertion will be treated as a hard assertion fail. Hard assertions when
        # they fail will make all subsequent assertions not be checked (but still
        # are logged to the json test report). The only other default hard
        # assertion is assertReturned. Fatal assertions on the other hand will
        # act as a normal assertion does in a unittest framework. The test
        # immediately ends if it fails, the only fatal assertion is loadAsmFile
        # since if that fails no other functions will work correctly.
        self.assertHalted()

        # This checks if the code produced no runtime warning messages.
        # Some common warnings are if the code accesses or writes to memory in
        # privileged regions of memory.
        self.assertNoWarnings()

        # Now check the the linked list nodes
        for i, (next_addr, data) in enumerate(zip(node_nexts, node_data)):
            n = node_nexts[0] if i + 1 == len(node_nexts) else node_nexts[i + 1]
            # Much like fillNode it has its opposite assertNodeAt It works the same
            # way, however a namedtuple is required for the data parameter. This is
            # for a nicer output when the test fails.

            # This will check:
            #   MEM[next_addr] == n
            #   MEM[next_addr + 1] == data

            # This assertion creates two checks in the JSON file
            #   1) nodeAtNext: x<next_addr>
            #   2) nodeAtData: x<next_addr + 1>
            self.assertNodeAt(next_addr, n, NodeData(data))

if __name__ == '__main__':
    unittest.main()
