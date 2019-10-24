import lc3_unit_test_case
import pylc3

class SimpleAddTest(lc3_unit_test_case.LC3UnitTestCase):

    parameters = [
        (5,5), (3,6), (15,10), (24,27),
        (36,16), (1,1), (15,25), (19,7)
    ]

    @parameterize(parameters, 'ADD({0}, {1}')
	def testAdd(self, a, b):
        #-------------------------------
        # Initialization / Loading Step
        #-------------------------------
		# Initialize lc-3 state.
		# Three options for initialization based on MemoryFillStrategy
        # 1) Fill with a specified value.
        # 2) Choose a single random value and fill memory with it.
        # 3) Give every memory address a random value.

		# Here option 2 is done and every memory address gets a random value.
        self.init(pylc3.MemoryFillStrategy.random_fill_with_seed, 10)

		# Load the students assembly file, if it fails to load then the test fails.
        self.loadAsmFile('simple_add.asm')

		#-------------------------------------------
        # Setup Preconditions and Expectations Step
        #-------------------------------------------
		# Setup parameters, give the value at label's A and B a specific value.
        self.setValue('A', a)
        self.setValue('B', b)

		#----------
        # Run Step
		#----------
		# Run the students code. You can pass in a number of instructions to execute
		# With no params though it will run until it halts (via a halt statement, or an error)
        # or until DEFAULT_MAX_EXECUTIONS instructions have executed.
        self.runCode()

		#----------------------------
		# Assert Postconditions Step
		#----------------------------
		# This first assertion checks if the code HALTed cleanly.
        # The underlying C++ library (liblc3) has a mode where if the simulator executes an invalid instruction
        # the simulation will end. This checks if the lc3 was halted via a HALT instruction.
        self.assertHalted()
        # This checks if the code produced no runtime warnings.
        # Some common warnings are if the code accesses memory in privileged regions.
        self.assertNoWarnings()
        # This checks if the value at label answer is equal to the expected value.
        self.assertValue('ANS', A + B)
