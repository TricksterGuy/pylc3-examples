import pyLC3
import unittest
# Changed in 0.9.0, MemoryFillStrategy is now in the pyLC3 module.
#from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
import pyLC3.pylc3 as pyLC3Constants
# Changed in 0.9.0, This was used by TAs at georgia tech to name test cases
# this mechanism is now integrated with the soft assertion system.
#from decorators import parameterize
from parameterized import parameterized


class SimpleIOTest(pyLC3.LC3UnitTestCase):

    @parameterized.expand([
        [""],
        [" "],
        ["aaaa"],
        ["A"],
        ["ABC"],
        ["HeLlO"],
        ["littleComputer3IsSoCoOoOoLio"],
    ])
    def testIO(self, s):
        #-----------------------------------------------------------------------
        # Test setup
        #-----------------------------------------------------------------------
        # New in 0.9.0. For soft assertions to work, it is required to set
        # self.display_name to the name of the specific test case.
        # At the end of the test a JSON file is generated with all the results.
        # and partial credit can be rewarded for specific assertions and test
        # case name.
        self.display_name = 'IO %s' % s

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

        # Here option 1 is done filling each memory address with the HALT
        # instruction (TRAP x25)
        self.init(pyLC3Constants.MemoryFillStrategy.fill_with_value, 0xF025)

        # Load the assembly file, if it fails to load then the test fails.
        self.loadAsmFile('simple_io.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------

        # Sets console input to the string given. Unlike setString no nul
        # terminator is appended to the string.
        self.setConsoleInput(s + "\n")

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
        # This checks if the console output produced matches exactly. Note that
        # unlike simple_string_test.py the output should not end with a nul
        # terminator character.
        answer = ''.join([e for e in s if e >= 'A' and e <= 'Z'])
        #
        # To reference this in the json file it will be named
        # IO string/console output
        # i.e. IO aaaa/console output
        self.assertConsoleOutput(answer)


if __name__ == '__main__':
    unittest.main()
