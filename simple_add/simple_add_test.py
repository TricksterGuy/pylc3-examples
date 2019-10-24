import pyLC3
import unittest
from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
from decorators import parameterize

class SimpleAddTest(pyLC3.LC3UnitTestCase):

    cases = [(5,5), (3,6), (15,10), (24,27), (36,16), (1,1), (15,25), (19,7)]

    @parameterize(cases, 'ADD({0}, {1})')
    def testAdd(self, a, b):
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
        self.init(MemoryFillStrategy.random_fill_with_seed, 10)

        # Load the assembly file, if it fails to load then the test fails.
        self.loadAsmFile('simple_add.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------

        # Setup parameters, give the VALUE at labels A and B a specific value.
        # It is very important to not modify the internal lc-3 state
        # (self.state) directly.
        #
        # Any modifications over the initial state of the lc-3 are logged and if
        # the test fails a string is produced for replaying the test in the GUI
        # simulator with the same setup.
        self.setValue('A', a)
        self.setValue('B', b)

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
        self.assertHalted()
        # This checks if the code produced no runtime warning messages.
        # Some common warnings are if the code accesses or writes to memory in
        # privileged regions of memory.
        self.assertNoWarnings()
        # This checks if the value at label answer is equal to the expected
        # value. 
        self.assertValue('ANS', a + b)


if __name__ == '__main__':
    unittest.main()
