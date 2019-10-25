import pyLC3
import unittest
from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
from decorators import parameterize

class SimpleAddTest(pyLC3.LC3UnitTestCase):

    cases = [
        [[]],
        [[1]],
        [[5]],
        [[2, 5, 9]],
        [[1, 5, 2, 4, 8, 3, 2, 1, 11, 123]],
        [[32767, 1]],
        [[-1, -1]],
    ]

    @parameterize(cases, 'SUM({0})')
    def testAdd(self, arr):
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

        # Here option 1 is done and every memory address gets the value xBABA.
        self.init(MemoryFillStrategy.fill_with_value, 0xBABA)

        # Load the assembly file, if it fails to load then the test fails.
        self.loadAsmFile('simple_sum.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------

        # Setup parameters. This time for ARRAY_LENGTH_LOC we don't want to set
        # the value at the label. We want to treat the value at that label as an
        # address and write to that address. Fortunately this is what setPointer
        # does, it is like an STI.
        self.setPointer('ARRAY_LENGTH_LOC', len(arr))
        # For the array itself we use setArray. Remember that this will not
        # write the array staring at the address of label ARRAY_LOC, but at the
        # address contained at the label. To reiterate from the .asm file pylc3
        # will not directly write an array referenced by a label due to the fact
        # that the student can add data after the label and if the array in the
        # python grader is large enough it can and will clobber student data.
        self.setArray('ARRAY_LOC', arr)

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
        # Much like with setPointer, assertPointer also exists. This assertion
        # will check if the value contained at the memory address contained in
        # ANSWER_LOC is the specified value. 
        self.assertPointer('ANSWER_LOC', sum(arr) & 0xFFFF)
        # And assertArray exists as well instead of setting an array it will
        # check the array given.
        self.assertArray('ARRAY_LOC', arr)


if __name__ == '__main__':
    unittest.main()
