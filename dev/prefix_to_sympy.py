import os
import sys
import inspect
from icecream import ic
import sympy as sp

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.SympyPrefix import sympy_tokenize, sympy_tokenize_str, vectorize_ds, vectorize_sentence, pad_right, sympy_to_prefix, repeat_operator_until_correct_binary, prefix_to_sympy, format_integer, unformat_integer

expr_arr0a = ['x']
expr_arr0b = ['s+', '4', '2']
expr_arr0c = ['add', 'mul', 'x', 'y', 'abs', 'x']
expr_arr0d = ['mul', 'x', 'pow', 'y', 's+', '2']
expr_arr0e = ['add', 's-', '4', '2', 'mul', 'x', 'y']

ic(prefix_to_sympy(expr_arr0a))
ic(prefix_to_sympy(expr_arr0b))
ic(prefix_to_sympy(expr_arr0c))
ic(prefix_to_sympy(expr_arr0d))
ic(prefix_to_sympy(expr_arr0e))

expr_2to3a = "-1/11664*i*e^3*(i*e^3*s_24*((-128)*m_c^2*s_23 + 128*s_13*s_25 + 128*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + 1/5832*i*e^3*(i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(64*m_c^2*m_d^2 + (-32)*m_d^2*s_15 + 32*m_c^2*s_34 + (-32)*s_14*s_35 + (-32)*s_13*s_45)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop))"
expr_2to3a_sympy = sp.parse_expr(expr_2to3a.replace("^", "**"))
expr_2to3a_prefix = sympy_to_prefix(expr_2to3a_sympy)
print(expr_2to3a_prefix)
# prefix_to_sympy(expr_2to3a_prefix)
