import pyLC3
import unittest
# Changed in 0.9.0, MemoryFillStrategy is now in the pyLC3 module.
#from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
import pyLC3.pylc3 as pyLC3Constants
# Changed in 0.9.0, This was used by TAs at georgia tech to name test cases
# this mechanism is now integrated with the soft assertion system.
#from decorators import parameterize
from parameterized import parameterized

class SimpleAddTest(pyLC3.LC3UnitTestCase):

    # Required if you want JSON output. This will generate a json file with the output per test assertion.
    # Valid values are JsonOutputPerAssertion or JsonExpandedOutputPerAssertion.
    # See 
    json_report_func = pyLC3.unittests.lc3_unit_test_case.JsonOutputPerAssertion

    @parameterized.expand([
        (5,5),
        (3,6),
        (15,10),
        (24,27),
        (36,16),
        (1,1),
        (15,25),
        (19,7)
    ])
    def testAdd(self, a, b):
        #-----------------------------------------------------------------------
        # Test setup
        #-----------------------------------------------------------------------
        # New in 0.9.0. For soft assertions to work, it is required to set
        # self.display_name to the name of the specific test case.
        # At the end of the test a JSON file is generated with all the results.
        # and partial credit can be rewarded for specific assertions and test
        # case name.
        #
        # The individual assertions will be named ADD(a,b)/assertionName.
        # For instance with the assertHalted below it will be named assuming 
        # a=5, b=5.
        # ADD(5,5)/halted
        self.display_name = 'ADD(%d,%d)' % (a, b)

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

        # Load the assembly file, if it fails to load then the test immediately
        # ends. It is a fatal assertion meaning we can't continue the test.
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
        # This checks if the value at label answer is equal to the expected
        # value. 
        self.assertValue('ANS', a + b)

        # None of the above assertions will stop the test if they fail. At the end
        # of the test in LC3UnitTestCase.tearDown will the check to make sure no
        # assertions failed was made and then it will fail the test. The failure
        # message will include all of the assertions that failed.

        # For each test case the JSON file will include the following 5 checks given the
        # assertions made in this test. For instance if the only test case was 19, 7 the
        # JSON file will look exactly like below.
        
        # Note to get JSON output cls.json_report_func needs to be set. See above for
        # what to set this field to.

        #{
        #"SimpleAddTest":[
        #{
        #       "display-name":"ADD(19,7)/assembles",
        #       "passed":true
        # },
        #{
        #        "display-name":"ADD(19,7)/version",
        #        "passed":true
        # },
        #{
        #        "display-name":"ADD(19,7)/halted",
        #        "passed":true
        # },
        # {
        #        "display-name":"ADD(19,7)/warnings",
        #        "passed":true
        #},
        #{
        #        "display-name":"ADD(19,7)/value: ANS",
        #        "passed":true
        #}]}

        # assembles  - Did the file assemble, if this fails then it will be the only thing
        #              present for that test case.
        # version    - Using the correct version of the LC3. Can be ignored.
        # halted     - Did the program run correctly, this is also a hard assertion.
        # warnings   - Did the program run without causing a warning.
        # value: ANS - Was the value at location ANS correct.
        
        # Additionallty the assertion names can be renamed, by passing name to any assertXXX
        # function.


if __name__ == '__main__':
    unittest.main()