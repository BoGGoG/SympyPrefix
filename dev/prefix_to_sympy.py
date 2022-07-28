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
