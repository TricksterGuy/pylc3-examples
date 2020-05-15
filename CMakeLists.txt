cmake_minimum_required(VERSION 3.5)

project(pylc3-examples)

include(FindPythonInterp)

enable_testing()

function(make_test TEST TEST_FILE)
    get_filename_component(PARENT_DIR ${TEST_FILE} DIRECTORY)
    add_test(
        NAME ${TEST}
        COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${TEST_FILE}
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/${PARENT_DIR}
    )
endfunction(make_test TEST TEST_FILE)

make_test(simple_add_test simple_add/simple_add_test.py)
make_test(simple_sum_test simple_sum/simple_sum_test.py)
make_test(simple_string_test simple_string/simple_string_test.py)
make_test(simple_io_test simple_io/simple_io_test.py)
make_test(student_test simple_data/student_test.py)
make_test(linked_list_test linked_list/linked_list_test.py)
make_test(double_subr_test lc3_calling_convention_basic/double_subr_test.py)
make_test(add_chars_test lc3_calling_convention_extra/add_chars_test.py)
make_test(mccarthy91_test lc3_calling_convention_recursive/mccarthy91_test.py)
make_test(mccarthy91_pbr_test subroutine_pass_by_regs/mccarthy91_test.py)

