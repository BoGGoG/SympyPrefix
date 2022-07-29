import os
import sys
import inspect
from icecream import ic
import sympy as sp
from sympy import srepr
from sympy.core.sympify import sympify

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(script_dir)
sys.path.insert(0, root_dir)


from source.SympyPrefix import prefix_to_sympy, sympy_tokenize, sympy_tokenize_str, vectorize_ds, vectorize_sentence, pad_right, sympy_to_prefix, repeat_operator_until_correct_binary, format_number


x = sp.Symbol("x")


expr_2to3a = "-1/11664*i*e^3*(i*e^3*s_24*((-128)*m_c^2*s_23 + 128*s_13*s_25 + 128*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + 1/5832*i*e^3*(i*e^3*m_d^2*(32*m_c^2*s_23 + 64*m_c^2*s_24 + (-32)*s_15*s_24 + (-32)*s_13*s_25 + (-32)*s_12*s_35)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)) + (-2)*i*e^3*m_d^2*(64*m_c^2*m_d^2 + (-32)*m_d^2*s_15 + 32*m_c^2*s_34 + (-32)*s_14*s_35 + (-32)*s_13*s_45)/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop)))/((m_d^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)*(s_24 + -1/2*reg_prop))"
expr_2to3a_sympy = sp.parse_expr(expr_2to3a.replace("^", "**"))
expr_2to3a_prefix = sympy_to_prefix(expr_2to3a_sympy)
expr_2to3a_prefix_simplify = sympy_to_prefix(sp.simplify(expr_2to3a_sympy))
expr_2to3a_prefix_expand = sympy_to_prefix(sp.expand(expr_2to3a_sympy))
expr_2to3a_prefix_factor = sympy_to_prefix(sp.factor(expr_2to3a_sympy))
expr_2to3a_prefix_powsimp = sympy_to_prefix(sp.powsimp(expr_2to3a_sympy))
ic(len(expr_2to3a_prefix))
ic(len(expr_2to3a_prefix_simplify))
ic(len(expr_2to3a_prefix_expand))
ic(len(expr_2to3a_prefix_factor))
ic(len(expr_2to3a_prefix_powsimp))

expr_2to3b = "-1/729*i*e^3*(i*e^3*((-64)*m_s^4*m_u^2 + (-16)*m_s^2*s_14*s_23 + -1/4*m_s^2*((-64)*m_s^2*s_13 + 128*s_12*s_23) + 32*m_s^2*m_u^2*s_24 + 32*s_12*s_23*s_24 + 16*m_s^2*s_12*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + (-16)*i*e^3*(m_s^2*m_u^2*s_12 + (-2)*m_s^2*m_u^2*s_23 + -s_14*s_23^2 + -m_u^2*s_12*s_24 + s_13*s_23*s_24 + (-2)*m_s^2*m_u^2*s_34 + m_s^2*s_13*s_34 + s_12*s_23*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -i*e^3*(16*m_s^2*s_12*s_23 + (-64)*m_s^2*m_u^2*s_24 + 32*m_u^2*s_24^2 + 16*m_s^2*s_14*s_34 + -1/4*m_s^2*(64*s_14*s_23 + (-64)*s_13*s_24 + 64*s_12*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -16/729*i*e^3*(i*e^3*(m_s^2*m_u^2*s_14 + (-2)*m_s^2*m_u^2*s_23 + m_s^2*s_13*s_23 + -m_u^2*s_14*s_24 + (-2)*m_s^2*m_u^2*s_34 + s_14*s_23*s_34 + s_13*s_24*s_34 + -s_12*s_34^2)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -1/16*i*e^3*(16*m_s^2*s_12*s_23 + (-64)*m_s^2*m_u^2*s_24 + 32*m_u^2*s_24^2 + 16*m_s^2*s_14*s_34 + -1/4*m_s^2*(64*s_14*s_23 + (-64)*s_13*s_24 + 64*s_12*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + 1/16*i*e^3*((-64)*m_s^4*m_u^2 + 16*m_s^2*s_14*s_23 + 32*m_s^2*m_u^2*s_24 + (-16)*m_s^2*s_12*s_34 + 32*s_14*s_24*s_34 + -1/4*m_s^2*((-64)*m_s^2*s_13 + 128*s_14*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + 16/729*i*e^3*(i*e^3*(m_s^2*m_u^2*s_12 + (-2)*m_s^2*m_u^2*s_23 + -s_14*s_23^2 + -m_u^2*s_12*s_24 + s_13*s_23*s_24 + (-2)*m_s^2*m_u^2*s_34 + m_s^2*s_13*s_34 + s_12*s_23*s_34)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -i*e^3*(m_s^2*m_u^2*s_14 + (-2)*m_s^2*m_u^2*s_23 + m_s^2*s_13*s_23 + -m_u^2*s_14*s_24 + (-2)*m_s^2*m_u^2*s_34 + s_14*s_23*s_34 + s_13*s_24*s_34 + -s_12*s_34^2)/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)) + -1/4*i*e^3*((-16)*m_s^2*m_u^4 + 8*m_s^2*m_u^2*s_13 + (-8)*m_u^2*s_13*s_24 + 16*s_13*s_23*s_34 + 16*m_u^2*(m_u^2*s_24 + (-2)*s_23*s_34))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop)))/((m_s^2 + -s_24 + 1/2*reg_prop)*(m_s^2 + -s_23 + -s_24 + s_34 + 1/2*reg_prop))"
expr_2to3b_sympy = sp.parse_expr(expr_2to3b.replace("^", "**"))
expr_2to3b_prefix = sympy_to_prefix(expr_2to3b_sympy)
expr_2to3b_back = prefix_to_sympy(expr_2to3b_prefix)
expr_2to3b_prefix_simplify = sympy_to_prefix(sp.simplify(expr_2to3b_sympy))
expr_2to3b_prefix_expand = sympy_to_prefix(sp.expand(expr_2to3b_sympy))
expr_2to3b_prefix_factor = sympy_to_prefix(sp.factor(expr_2to3b_sympy))
expr_2to3b_prefix_powsimp = sympy_to_prefix(sp.powsimp(expr_2to3b_sympy))
ic(len(expr_2to3b_prefix))
ic(len(expr_2to3b_prefix_simplify))
ic(len(expr_2to3b_prefix_expand))
ic(len(expr_2to3b_prefix_factor))
ic(len(expr_2to3b_prefix_powsimp))

expr_2to3c = "-1/144*i*e^3*(i*e^3*s_12*(128*m_u^2*s_23 + 128*s_25*s_34 + 128*s_24*s_35)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + 2*i*e^3*m_t^2*(64*m_u^2*s_12 + (-32)*m_u^2*s_23 + (-32)*s_25*s_34 + (-32)*s_24*s_35 + 32*s_12*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)))/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + -1/36*i*e^3*(i*e^3*m_t^2*(64*m_t^2*m_u^2 + (-32)*m_u^2*s_13 + (-32)*s_15*s_34 + (-32)*s_14*s_35 + 32*m_t^2*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)) + 1/2*i*e^3*m_t^2*(64*m_u^2*s_12 + (-32)*m_u^2*s_23 + (-32)*s_25*s_34 + (-32)*s_24*s_35 + 32*s_12*s_45)/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop)))/((s_12 + 1/2*reg_prop)*(m_t^2 + s_12 + -s_13 + -s_23 + 1/2*reg_prop))"
expr_2to3c_sympy = sp.parse_expr(expr_2to3c.replace("^", "**"))
expr_2to3c_prefix = sympy_to_prefix(expr_2to3c_sympy)
expr_2to3c_back = prefix_to_sympy(expr_2to3c_prefix)
expr_2to3c_prefix_simplify = sympy_to_prefix(sp.simplify(expr_2to3c_sympy))
expr_2to3c_prefix_expand = sympy_to_prefix(sp.expand(expr_2to3c_sympy))
expr_2to3c_prefix_factor = sympy_to_prefix(sp.factor(expr_2to3c_sympy))
expr_2to3c_prefix_powsimp = sympy_to_prefix(sp.powsimp(expr_2to3c_sympy))
ic(len(expr_2to3c_prefix))
ic(len(expr_2to3c_prefix_simplify))
ic(len(expr_2to3c_prefix_expand))
ic(len(expr_2to3c_prefix_factor))
ic(len(expr_2to3c_prefix_powsimp))

expr_2to3d = "4/81*e^4*(16*m_c^2*m_u^2 + (-8)*m_c^2*s_13 + 8*s_14*s_23 + (-8)*m_u^2*s_24 + 8*s_12*s_34)*(m_u^2 + -s_13 + 1/2*reg_prop)^(-2)"
expr_2to3d_sympy = sp.parse_expr(expr_2to3d.replace("^", "**"))
expr_2to3d_prefix = sympy_to_prefix(expr_2to3d_sympy)
expr_2to3d_back = prefix_to_sympy(expr_2to3d_prefix)
expr_2to3d_prefix_simplify = sympy_to_prefix(sp.simplify(expr_2to3d_sympy))
expr_2to3d_prefix_expand = sympy_to_prefix(sp.expand(expr_2to3d_sympy))
expr_2to3d_prefix_factor = sympy_to_prefix(sp.factor(expr_2to3d_sympy))
expr_2to3d_prefix_powsimp = sympy_to_prefix(sp.powsimp(expr_2to3d_sympy))
ic(len(expr_2to3d_prefix))
ic(len(expr_2to3d_prefix_simplify))
ic(len(expr_2to3d_prefix_expand))
ic(len(expr_2to3d_prefix_factor))
ic(len(expr_2to3d_prefix_powsimp))

# ic| len(expr_2to3a_prefix): 545
# ic| len(expr_2to3a_prefix_simplify): 212
# ic| len(expr_2to3a_prefix_expand): 10474
# ic| len(expr_2to3a_prefix_factor): 200
# ic| len(expr_2to3a_prefix_powsimp): 545
# ic| len(expr_2to3b_prefix): 1619
# ic| len(expr_2to3b_prefix_simplify): 427
# ic| len(expr_2to3b_prefix_expand): 32018
# ic| len(expr_2to3b_prefix_factor): 378
# ic| len(expr_2to3b_prefix_powsimp): 1582
# ic| len(expr_2to3c_prefix): 547
# ic| len(expr_2to3c_prefix_simplify): 198
# ic| len(expr_2to3c_prefix_expand): 9153
# ic| len(expr_2to3c_prefix_factor): 201
# ic| len(expr_2to3c_prefix_powsimp): 547
# ic| len(expr_2to3d_prefix): 86
# ic| len(expr_2to3d_prefix_simplify): 75
# ic| len(expr_2to3d_prefix_expand): 411
# ic| len(expr_2to3d_prefix_factor): 75
# ic| len(expr_2to3d_prefix_powsimp): 115
# factor seems to be working the best!
