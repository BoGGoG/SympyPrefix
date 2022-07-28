import os
import sys
import inspect
from icecream import ic
import sympy as sp
from sympy import srepr
from sympy import sympify

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.SympyPrefix import format_integer, unformat_integer, sympy_to_prefix, prefix_to_sympy, format_number

def test_unformat_number():
    nums_str = [ 
            "1",
            "2",
            "1/3",
            "1/2",
            "0",
            "E"
            ]
    nums_sp = [sympify(x) for x in nums_str]
    nums_formatted = [format_number(x) for x in nums_sp]
    ic(nums_formatted[0])
    nums_recovered = [prefix_to_sympy(x) for x in nums_formatted]
    for i in range(len(nums_sp)):
        assert nums_sp[i] == nums_recovered[i]
        ic(nums_sp[i])
        ic(nums_formatted[i])
        ic(srepr(nums_recovered[i]))

def test_unformat_integer():
    test_int1 = sp.parsing.parse_expr("1")
    test_int2 = sp.parsing.parse_expr("2")
    test_int3 = sp.parsing.parse_expr("0")
    test_int4 = sp.parsing.parse_expr("-1")
    test_int5 = sp.parsing.parse_expr("-1234")
    test_int6 = sp.parsing.parse_expr("+1234")

    test_int_formated1 = format_integer(test_int1)
    test_int_formated2 = format_integer(test_int2)
    test_int_formated3 = format_integer(test_int3)
    test_int_formated4 = format_integer(test_int4)
    test_int_formated5 = format_integer(test_int5)
    test_int_formated6 = format_integer(test_int6)

    test_int_recovered1 = unformat_integer(test_int_formated1)
    test_int_recovered2 = unformat_integer(test_int_formated2)
    test_int_recovered3 = unformat_integer(test_int_formated3)
    test_int_recovered4 = unformat_integer(test_int_formated4)
    test_int_recovered5 = unformat_integer(test_int_formated5)
    test_int_recovered6 = unformat_integer(test_int_formated6)
 
    assert test_int1 == test_int_recovered1
    assert test_int2 == test_int_recovered2
    assert test_int3 == test_int_recovered3
    assert test_int4 == test_int_recovered4
    assert test_int5 == test_int_recovered5
    assert test_int6 == test_int_recovered6

    assert test_int2 != test_int_recovered1

def test_prefix_to_sympy_functions():
    """
    transform below expressions to prefix using `sympy_to_prefix` 
    and then recover them using `prefix_to_sympy`.
    """
    exprs = [ 
            "x+y+sin(3)",
            "x",
            "1",
            "1/2",
            "x*y + 3",
            "-42",
            "0",
            "x**2 / y + exp(-y**2 + abs(-2*x))",
            "42*sin(cos(exp(abs(1/x) + 13) - atanh(y)))",
            "sin(cos(x**2))",
            "x/42",
            "42/x",
            "x/(42*y)",
            "1/sin(32*x)",
            "exp(1/2)",
            "exp(-1/2)",
            "exp(1)",
            "exp(0)",
            "exp(-1)",
            "exp(sin(-1))",
            "exp(sin(E))",
            "log(x)",
            "log(x**-1)",
            "sin(x**32)",
            "x/E",
            "exp(-x**2 / 2)",
            ]
    exprs = [sympify(x) for x in exprs]
    exprs_prefix = [sympy_to_prefix(e) for e in exprs]
    ic(exprs_prefix[0])
    exprs_recovered = [prefix_to_sympy(e) for e in exprs_prefix]

    for i in range(len(exprs)):
        ic(i)
        ic(exprs[i])
        ic(exprs_prefix[i])
        ic(exprs_recovered[i])
        assert exprs[i] == exprs_recovered[i]

def test_prefix_to_sympy_functions_2():
    """
    Here I always add functions that have caused problems and then I fix them.

    - expr1: 'E' was not in the variables list
    """
    expr1 = sympify("x**4*(1/24 + E) + x**3/6 + x**2*(1/2 + E) + x + 1 + E")
    expr_prefix1 = sympy_to_prefix(expr1)
    expr_recovered1 = prefix_to_sympy(expr_prefix1)
    assert expr1 == expr_recovered1

    expr2 = sympify("pi")
    expr_prefix2 = sympy_to_prefix(expr2)
    expr_recovered2 = prefix_to_sympy(expr_prefix2)
    assert expr2 == expr_recovered2

    expr3 = sp.core.numbers.pi
    expr_prefix3 = sympy_to_prefix(expr3)
    expr_recovered3 = prefix_to_sympy(expr_prefix3)
    assert expr3 == expr_recovered3


    expr4 = sp.core.numbers.Pi
    ic(expr4)
    ic(srepr(expr4))
    expr_prefix4 = sympy_to_prefix(expr4)
    ic(expr_prefix4)
    # expr_recovered4 = prefix_to_sympy(expr_prefix4)
    # ic(expr_recovered4)

    expr5 = sp.core.numbers.ImaginaryUnit
    expr5 = sp.core.numbers.ImaginaryUnit
    ic(expr5)
    ic(srepr(expr5))
    expr_prefix5 = sympy_to_prefix(expr5)
    ic(expr_prefix5)

