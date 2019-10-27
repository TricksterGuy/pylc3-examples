import pyLC3
import unittest
from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
from decorators import parameterize

class DoubleSubroutineTest(pyLC3.LC3UnitTestCase):

    cases = [
        [0, []],
        [1, [0]],
        [3, [0, 0, 0]],
        [1, [1]],
        [2, [1, 0]],
        [4, [80, 10, 40, 20]],
        [10, [6, 3, 2, 0, -99, 2, 34, 29, -117, 1000]],
    ]

    @parameterize(cases, 'DOUBLE({0}, {1})')
    def testDouble(self, argc, args):
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
        self.loadAsmFile('double_subr.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------
        
        # Call a subroutine named DOUBLE with the arguments given.
        # This will perform the following:
        # PC = DOUBLE
        # R7 = a Dummy Value (default x8000)
        # R6 = a Dummy Value (default xF000)
        # R5 = a Dummy Value (default xCAFE)
        # MEM[R6] = params[0]
        # MEM[R6 + 1] = params[1]
        # ...
        # MEM[R6 + len(params)-1] = params[len(params) - 1]
        #
        # A breakpoint is placed at whatever address R7 is pointing to.
        self.callSubroutine('DOUBLE', params=[argc]+args)

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

        # Note that we used assertReturned over assertHalted. assertReturned has
        # some extra checks to make sure that the subroutine called was returned
        # from correctly.
        self.assertReturned()
        # This checks if the code produced no runtime warning messages.
        # Some common warnings are if the code accesses or writes to memory in
        # privileged regions of memory.
        self.assertNoWarnings()

        # This assert checks if the value at MEM[R6] (which is the return value)
        # is the correct answer.
        self.assertReturnValue((sum(args) * 2) & 0xFFFF)
        # This assert checks if any registers are clobbered (value changed as a
        # side effect of subroutine). At the very least R5 and R7 should not be
        # clobbered, but others may decide to check all registers.
        self.assertRegistersUnchanged([5, 7])
        # This assert checks if R6 ended up being decremented by 1 by the end of
        # the subroutine, it needs the expected stack value along with the
        # dummy values in R5 (old frame pointer) and R7 (return address).
        self.assertStackManaged(stack=0xEFFF-len(args)-1,
                                return_address=0x8000,
                                old_frame_pointer=0xCAFE)
        # The last assert checks if the appropriate subroutine calls were made.
        # In pylc3 subroutine call verification is only done with the top level
        # function calls and not all of them. See the subroutine call test for
        # a reasoning on why we do testing this way.
        
        # assertSubroutineCallsMade() works on previous calls to
        # expectSubroutineCall() since we didn't make a call to that function it
        # will simply check if no subroutine calls were made.
        self.assertSubroutineCallsMade()


if __name__ == '__main__':
    unittest.main()
