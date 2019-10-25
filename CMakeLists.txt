cmake_minimum_required(VERSION 3.5)

project(pylc3-examples)

find_package(PythonInterp REQUIRED)

enable_testing()


add_test(
    NAME simple_add_test 
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/simple_add/simple_add_test.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/simple_add
)

set_property(
    TEST simple_add_test 
    APPEND PROPERTY
    ENVIRONMENT PYTHONPATH=${CMAKE_CURRENT_SOURCE_DIR}/util:$ENV{PYTHONPATH}
)

add_test(
    NAME simple_sum_test 
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/simple_sum/simple_sum_test.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/simple_sum
)

set_property(
    TEST simple_sum_test 
    APPEND PROPERTY
    ENVIRONMENT PYTHONPATH=${CMAKE_CURRENT_SOURCE_DIR}/util:$ENV{PYTHONPATH}
)
