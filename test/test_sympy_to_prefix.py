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
    assert expr3_prefix ==  ['add', 's+', '3', 'add', 'x', 'add', 'y', 'z']
    assert expr4_prefix ==  ['add', 's+', '3', 'add', 'E', 'add', 'x', 'add', 'y', 'z']
    ic(expr5_prefix)
    assert expr5_prefix ==  ['add', 's+', '3', 'add', 'E', 'add', 'a', 'add', 'y', 'add', 'z',
        'mul', 's-', '1', 'x']
    ic(expr6_prefix)
    assert expr6_prefix ==  ['add', 's-', '3', 'add', 'E', 'add', 'x', 'add', 'y', 'add', 'z', 'sin', 'x']
    
def test_many_arguments_mult():
    expr1 = sympy.parsing.parse_expr("x*y")
    expr2 = sympy.parsing.parse_expr("x*y*z")
    expr3 = sympy.parsing.parse_expr("x*y*z*3")

    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    assert expr1_prefix == ["mul", "x", "y"]
    assert expr2_prefix == ["mul", "x", "mul", "y", "z"]
    assert expr3_prefix ==  ['mul', 's+', '3', 'mul', 'x', 'mul', 'y', 'z']

def test_div():
    expr1 = sympy.parsing.parse_expr("x/y")
    expr2 = sympy.parsing.parse_expr("x/y/z")
    expr3 = sympy.parsing.parse_expr("-1/3")
    expr4 = sympy.parsing.parse_expr("x/42")
    # TODO: sadly x/42 first gets converted to 1/42 * x and won't give the nicer
    # output ['div', 'x', 's+', '4', '2'], might want to fix this at some point
    
    expr1_prefix = sympy_to_prefix(expr1)
    expr2_prefix = sympy_to_prefix(expr2)
    expr3_prefix = sympy_to_prefix(expr3)
    expr4_prefix = sympy_to_prefix(expr4)
    assert expr1_prefix == ["mul", "x", 'pow', "y",  's-', '1']
    assert expr2_prefix == ["mul", "x", 'mul', 'pow', "y", 's-', '1', 'pow', 'z', 's-', '1']
    ic(expr3_prefix)
    assert expr3_prefix == ['mul', 's-', '1', 'pow', 's+', '3', 's-', '1']
    assert expr4_prefix == ['mul', 'mul', 's+', '1', 'pow', 's+', '4', '2', 's-', '1', 'x']
    
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

def test_marty_sqampls():
    """
    manually copy marty squared amplitudes here to test them
    """
    expr_2to3a = "-1/11664*i*e^3*(i*e^3*s_24*((-128)*m_c^2*s_23 + 128*s_13*s_25 + 128*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + 1/5832*i*e^3*(i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(64*m_c^2*m_d^2 + (-32)*m_d^2*s_15 + 32*m_c^2*s_34 + (-32)*s_14*s_35 + (-32)*s_13*s_45)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop))"
    expr_2to3a_sympy = sympy.parse_expr(expr_2to3a.replace("^", "**"))
    expr_2to3a_prefix = sympy_to_prefix(expr_2to3a_sympy)
    ic(len(expr_2to3a_prefix))

    expr_2to3b = "-1/729*i*e^3*(i*e^3*((-64)*m_s^4*m_u^2 + (-16)*m_s^2*s_14*s_23 + -1/4*m_s^2*((-64)*m_s^2*s_13 + 128*s_12*s_23) + 32*m_s^2*m_u^2*s_24 + 32*s_12*s_23*s_24 + 16*m_s^2*s_12*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + (-16)*i*e^3*(m_s^2*m_u^2*s_12 + (-2)*m_s^2*m_u^2*s_23 + -s_14*s_23^2 + -m_u^2*s_12*s_24 + s_13*s_23*s_24 + (-2)*m_s^2*m_u^2*s_34 + m_s^2*s_13*s_34 + s_12*s_23*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -i*e^3*(16*m_s^2*s_12*s_23 + (-64)*m_s^2*m_u^2*s_24 + 32*m_u^2*s_24^2 + 16*m_s^2*s_14*s_34 + -1/4*m_s^2*(64*s_14*s_23 + (-64)*s_13*s_24 + 64*s_12*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -16/729*i*e^3*(i*e^3*(m_s^2*m_u^2*s_14 + (-2)*m_s^2*m_u^2*s_23 + m_s^2*s_13*s_23 + -m_u^2*s_14*s_24 + (-2)*m_s^2*m_u^2*s_34 + s_14*s_23*s_34 + s_13*s_24*s_34 + -s_12*s_34^2)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -1/16*i*e^3*(16*m_s^2*s_12*s_23 + (-64)*m_s^2*m_u^2*s_24 + 32*m_u^2*s_24^2 + 16*m_s^2*s_14*s_34 + -1/4*m_s^2*(64*s_14*s_23 + (-64)*s_13*s_24 + 64*s_12*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + 1/16*i*e^3*((-64)*m_s^4*m_u^2 + 16*m_s^2*s_14*s_23 + 32*m_s^2*m_u^2*s_24 + (-16)*m_s^2*s_12*s_34 + 32*s_14*s_24*s_34 + -1/4*m_s^2*((-64)*m_s^2*s_13 + 128*s_14*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + 16/729*i*e^3*(i*e^3*(m_s^2*m_u^2*s_12 + (-2)*m_s^2*m_u^2*s_23 + -s_14*s_23^2 + -m_u^2*s_12*s_24 + s_13*s_23*s_24 + (-2)*m_s^2*m_u^2*s_34 + m_s^2*s_13*s_34 + s_12*s_23*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -i*e^3*(m_s^2*m_u^2*s_14 + (-2)*m_s^2*m_u^2*s_23 + m_s^2*s_13*s_23 + -m_u^2*s_14*s_24 + (-2)*m_s^2*m_u^2*s_34 + s_14*s_23*s_34 + s_13*s_24*s_34 + -s_12*s_34^2)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -1/4*i*e^3*((-16)*m_s^2*m_u^4 + 8*m_s^2*m_u^2*s_13 + (-8)*m_u^2*s_13*s_24 + 16*s_13*s_23*s_34 + 16*m_u^2*(m_u^2*s_24 + (-2)*s_23*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop))"
    expr_2to3b_sympy = sympy.parse_expr(expr_2to3b.replace("^", "**"))
    expr_2to3b_prefix = sympy_to_prefix(expr_2to3b_sympy)
    ic(len(expr_2to3b_prefix))

    expr_2to3c = "-1/144*i*e^3*(i*e^3*s_12*(128*m_u^2*s_23 + 128*s_25*s_34 + 128*s_24*s_35)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + 2*i*e^3*m_t^2*(64*m_u^2*s_12 + (-32)*m_u^2*s_23 + (-32)*s_25*s_34 + (-32)*s_24*s_35 + 32*s_12*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)))/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + -1/36*i*e^3*(i*e^3*m_t^2*(64*m_t^2*m_u^2 + (-32)*m_u^2*s_13 + (-32)*s_15*s_34 + (-32)*s_14*s_35 + 32*m_t^2*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + 1/2*i*e^3*m_t^2*(64*m_u^2*s_12 + (-32)*m_u^2*s_23 + (-32)*s_25*s_34 + (-32)*s_24*s_35 + 32*s_12*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)))/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop))"
    expr_2to3c_sympy = sympy.parse_expr(expr_2to3c.replace("^", "**"))
    expr_2to3c_prefix = sympy_to_prefix(expr_2to3c_sympy)
    ic(len(expr_2to3c_prefix))

