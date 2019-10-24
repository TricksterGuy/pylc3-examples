from parameterized import parameterized

# Apparently this must start with the name of the function followed by
# an underscore, or the test silently fails
def display_name(fmt):
    def testcase_func_name(testcase_func, param_num, param):
        return fmt.format(*param.args)

    return testcase_func_name

def basic_name(testcase_func, param_num, param):
    return '{}_{}'.format(testcase_func.__name__, param_num)

def parameterize(params, fmt):
    return parameterized.expand(
        params,
        doc_func=display_name(fmt),
        testcase_func_name=basic_name)