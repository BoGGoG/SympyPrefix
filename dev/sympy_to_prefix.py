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


expr3 = sympy.parsing.parse_expr("-1/3")
# ic(expr3)
# ic(sympy_to_prefix(expr3))

