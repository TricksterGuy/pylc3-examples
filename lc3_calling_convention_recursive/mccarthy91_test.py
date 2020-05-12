import pyLC3
import unittest
# Changed in 0.9.0, MemoryFillStrategy is now in the pyLC3 module.
#from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
import pyLC3.pylc3 as pyLC3Constants
# Changed in 0.9.0, This was used by TAs at georgia tech to name test cases
# this mechanism is now integrated with the soft assertion system.
#from decorators import parameterize
from parameterized import parameterized

class McCarthy91Test(pyLC3.LC3UnitTestCase):

    @parameterized.expand([
        [101],
        [102],
        [90],
        [0],
        [1],
        [56]
    ])
    def testMcCarthy91(self, n):
        #-----------------------------------------------------------------------
        # Test setup
        #-----------------------------------------------------------------------
        # New in 0.9.0. For soft assertions to work, it is required to set
        # self.display_name to the name of the specific test case.
        # At the end of the test a JSON file is generated with all the results.
        # and partial credit can be rewarded for specific assertions and test
        # case name.
        self.display_name = 'mccarthy91(%d)' % n
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
        self.loadAsmFile('mccarthy91.asm')

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
        # PC = MCCARTHY91
        # R7 = a Dummy Value (default x8000)
        # R6 = a Dummy Value (default xF000)
        # R5 = a Dummy Value (default xCAFE)
        # MEM[R6] = n
        #
        # A breakpoint is placed at whatever address R7 is pointing to.
        self.callSubroutine('MCCARTHY91', params=[n])
        
        # Expect subroutine calls to be made. This is important especially for
        # recursive subroutine verification as if this is left off the grader
        # would accept an iterative solution without any subroutine calls.
        #
        # The subroutine call checker is very strict and will fail if the code
        # calls subroutines that are not expected. You can mark subroutine calls
        # as optional to whitelist them.
        #
        # Only subroutine calls made by the initial subroutine call should be
        # listed here. The call checker works using inductive reasoning.
        # You check the base case, then a case that causes 1 recursive call and
        # so on.
        if n < 100:
            # If we aren't the base case then we will call once with n + 11
            # and then 91 if the base case of the recursive call wasn't made.
            self.expectSubroutineCall('MCCARTHY91', [n + 11])
            self.expectSubroutineCall('MCCARTHY91', 
                [91 if n + 11 < 100 else n + 1])

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
        self.assertReturnValue(n - 10 if n > 100 else 91)
        # This assert checks if any registers are clobbered (value changed as a
        # side effect of subroutine). At the very least R5 and R7 should not be
        # clobbered, but others may decide to check all registers.
        self.assertRegistersUnchanged([5, 7])
        # This assert checks if R6 ended up being decremented by 1 by the end of
        # the subroutine, it needs the expected stack value along with the
        # dummy values in R5 (old frame pointer) and R7 (return address).
        self.assertStackManaged(stack=0xEFFE,
                                return_address=0x8000,
                                old_frame_pointer=0xCAFE)
        # The last assert checks if the appropriate subroutine calls were made.
        # In pylc3 subroutine call verification is only done with the top level
        # function calls and not all of them. See the subroutine call test for
        # a reasoning on why we do testing this way.
        
        # assertSubroutineCallsMade() works on previous calls to
        # expectSubroutineCall()
        self.assertSubroutineCallsMade()


if __name__ == '__main__':
    unittest.main()
