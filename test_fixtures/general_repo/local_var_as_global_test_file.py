# This file for tests/test_general_validators/test_has_local_var_named_as_global.py


def func_for_test_local_var_as_global():
    LOCAL_VAR = 10
    return LOCAL_VAR + 3