import os
import sys
import inspect
from icecream import ic
import sympy
from sympy import srepr
from sympy.core.sympify import sympify

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.SympyPrefix import sympy_tokenize, sympy_tokenize_str, vectorize_ds, vectorize_sentence, pad_right, sympy_to_prefix, repeat_operator_until_correct_binary, format_number

x = sympy.Symbol("x")
y = sympy.Symbol("y")

def test_many_arguments_add():
    """
    Sympy would give ["add", "x", "y", "z"], but we need "add" to take exactly 2 arguments
    
    About the order of the arguments: Sympy sorts the arguments uniquely, but they don't say how.
    Mentioned [here](https://docs.sympy.org/latest/tutorial/manipulation.html)
    I think it's numbers > variables (lexicographically ordered) > functions
    """
    expr1 = sympy.parsing.parse_expr("x+y")
    expr2 = sympy.parsing.parse_expr("x+y+z")
    expr3 = sympy.parsing.parse_expr("x+y+z+3")
    expr4 = sympy.parsing.parse_expr("x+y+z+3+E")
    expr5 = sympy.parsing.parse_expr("a-x+y+z+3+E")
    expr6 = sympy.parsing.parse_expr("sin(x)+x+y+z-3+E")

    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    expr4_prefix = sympy_to_prefix(expr4)
    expr5_prefix = sympy_to_prefix(expr5)
    expr6_prefix = sympy_to_prefix(expr6)
    assert expr1_prefix == ["add", "x", "y"]
    assert expr2_prefix == ["add", "x", "add", "y", "z"]
    assert expr3_prefix ==  ['add', 'int', 's+', '3', 'add', 'x', 'add', 'y', 'z']
    assert expr4_prefix ==  ['add', 'int', 's+', '3', 'add', 'E', 'add', 'x', 'add', 'y', 'z']
    ic(expr5_prefix)
    assert expr5_prefix ==  ['add', 'int', 's+', '3', 'add', 'E', 'add', 'a', 'add', 'y', 'add', 'z',
        'mul', 'int', 's-', '1', 'x']
    ic(expr6_prefix)
    assert expr6_prefix ==  ['add', 'int', 's-', '3', 'add', 'E', 'add', 'x', 'add', 'y', 'add', 'z', 'sin', 'x']
    
def test_many_arguments_mult():
    expr1 = sympy.parsing.parse_expr("x*y")
    expr2 = sympy.parsing.parse_expr("x*y*z")
    expr3 = sympy.parsing.parse_expr("x*y*z*3")

    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    assert expr1_prefix == ["mul", "x", "y"]
    assert expr2_prefix == ["mul", "x", "mul", "y", "z"]
    assert expr3_prefix ==  ['mul', 'int', 's+', '3', 'mul', 'x', 'mul', 'y', 'z']

def test_div():
    expr1 = sympy.parsing.parse_expr("x/y")
    expr2 = sympy.parsing.parse_expr("x/y/z")
    expr3 = sympy.parsing.parse_expr("-1/3")
    expr4 = sympy.parsing.parse_expr("x/42")
    # TODO: sadly x/42 first gets converted to 1/42 * x and won't give the nicer
    # output ['div', 'x', 'int', 's+', '4', '2'], might want to fix this at some point
    
    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    expr4_prefix = sympy_to_prefix(expr4)
    assert expr1_prefix == ["mul", "x", 'pow', "y", 'int', 's-', '1']
    assert expr2_prefix == ["mul", "x", 'mul', 'pow', "y", 'int', 's-', '1', 'pow', 'z', 'int', 's-', '1']
    assert expr3_prefix == ['mul', 'int', 's-', '1', 'pow', 'int', 's+', '3', 'int', 's-', '1']
    assert expr4_prefix == ['mul', 'mul', 'int', 's+', '1', 'pow', 'int', 's+', '4', '2', 'int', 's-', '1', 'x']
    
def test_format_number():
    numbers_str = [ 
            "1",
            "-1",
            "2",
            "1/2",
            "1/3",
            "-1/2",
            "-1/3",
            "1/12",
            "-1/12",
            "0",
            "E",
            ]
    numbers_sp = [sympify(x) for x in numbers_str]
    numbers_formatted = [format_number(x) for x in numbers_sp]
    for i in range(len(numbers_sp)):
        ic(numbers_str[i])
        ic(numbers_sp[i])
        ic(numbers_formatted[i])

