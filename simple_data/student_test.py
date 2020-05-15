import pyLC3
import unittest
import collections

# Changed in 0.9.0, MemoryFillStrategy is now in the pyLC3 module.
#from pyLC3.unittests.lc3_unit_test_case import MemoryFillStrategy
import pyLC3.pylc3 as pyLC3Constants


# It is required to have a namedtuple for verifying the data.
# This is to have nicer output informing the students which fields 
# are incorrect.  
Student = collections.namedtuple('Student', ['name', 'num_tests', 'num_homeworks', 'tests', 'homeworks', 'grade'])

class StudentTest(pyLC3.LC3UnitTestCase):

    def testStudent(self):
        #-----------------------------------------------------------------------
        # Test setup
        #-----------------------------------------------------------------------
        # New in 0.9.0. For soft assertions to work, it is required to set
        # self.display_name to the name of the specific test case.
        # At the end of the test a JSON file is generated with all the results.
        # and partial credit can be rewarded for specific assertions and test
        # case name.
        self.display_name = 'Student'

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

        # Important! since the asm file uses plugins we need to be sure to enable
        # loading of complx's plugins. This must be done before loadAsmFile or
        # the program may not assemble.
        self.setPluginsEnabled(True)

        # Load the assembly file, if it fails to load then the test fails.
        self.loadAsmFile('student.asm')

        #-----------------------------------------------------------------------
        # Setup Preconditions and Expectations Step
        #-----------------------------------------------------------------------
        # At this step we setup the initial state for the test. This means
        # setting interesting memory addresses or labels to certain values,
        # setting up a subroutine or trap call, expecting a specific subroutine
        # call, or giving the lc-3 some console input to use for execution.
        # ----------------------------------------------------------------------

        # Set label for student to find themselves (ha!).
        self.setValue("STUDENT", 0x4000)

        # Set our student datastructure at address x4000. This is ok since address
        # x4000 doesn't have a label, however we do have a STUDENT label we just
        # set to x4000. as long as the address itself isn't labelled pyLC3 won't
        # complain.

        # Note I don't use the namedtuple here as I want to leave the "grade" field
        # randomized since it contains the answer.
        self.fillData(0x4000, ("Student", 3, 5, [100, 75, 80], [100, 50, 80, 60, 100]))

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

        # We printed out the student's name so check that here.
        self.assertConsoleOutput('Student')

        # Now lets check our data. Remember that a namedtuple is required when
        # using assertDataAt as it is required for nicer output and telling the
        # student exactly what area of our data was incorrect.
        #
        # To reference this in the json file it will be named
        # Student/dataAt: x4000
        self.assertDataAt(0x4000, Student('Student', 3, 5, [100, 75, 80], [100, 50, 80, 60, 100], 80))

if __name__ == '__main__':
    unittest.main()
