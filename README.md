# SympyPrefix
Convert sympy expressions to prefix notation and back.

## Example
```python
expr = sympy.parse_expr("4/81*e^4*(16*m_c^2*m_u^2 + (-8)*m_c^2*s_13 + 8*s_14*s_23 + (-8)*m_u^2*s_24 + 8*s_12*s_34)*(m_u^2 + -s_13 + 1/2*reg_prop)^(-2))")
expr_prefix = prefix_to_sympy(expr)
--> ['add', 'mul', 'mul', 's-', '1', 'pow', 's+', '1', '1', '6', '6', '4', 's-', '1', 'mul', 'i', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 'i', 'mul', 's_24', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 's-', '1', '2', '8', 'mul', 's_23', 'pow', 'm_c', 's+', '2', 'add', 'mul', 's+', '1', '2', '8', 'mul', 's_12', 's_35', 'mul', 's+', '1', '2', '8', 'mul', 's_13', 's_25', 'mul', 's-', '2', 'mul', 'i', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'm_d', 's+', '2', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 's-', '3', '2', 'mul', 's_12', 's_35', 'add', 'mul', 's-', '3', '2', 'mul', 's_13', 's_25', 'add', 'mul', 's-', '3', '2', 'mul', 's_15', 's_24', 'add', 'mul', 's+', '3', '2', 'mul', 's_23', 'pow', 'm_c', 's+', '2', 'mul', 's+', '6', '4', 'mul', 's_24', 'pow', 'm_c', 's+', '2', 'mul', 'mul', 's+', '1', 'pow', 's+', '5', '8', '3', '2', 's-', '1', 'mul', 'i', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 'i', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'm_d', 's+', '2', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 's-', '3', '2', 'mul', 's_12', 's_35', 'add', 'mul', 's-', '3', '2', 'mul', 's_13', 's_25', 'add', 'mul', 's-', '3', '2', 'mul', 's_15', 's_24', 'add', 'mul', 's+', '3', '2', 'mul', 's_23', 'pow', 'm_c', 's+', '2', 'mul', 's+', '6', '4', 'mul', 's_24', 'pow', 'm_c', 's+', '2', 'mul', 's-', '2', 'mul', 'i', 'mul', 'pow', 'e', 's+', '3', 'mul', 'pow', 'm_d', 's+', '2', 'mul', 'pow', 'add', 's_24', 'mul', 'mul', 's-', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 's-', '1', 'mul', 'pow', 'add', 's_34', 'add', 'pow', 'm_d', 's+', '2', 'add', 'mul', 'mul', 's+', '1', 'pow', 's+', '2', 's-', '1', 'reg_prop', 'add', 'mul', 's-', '1', 's_23', 'mul', 's-', '1', 's_24', 's-', '1', 'add', 'mul', 's-', '3', '2', 'mul', 's_13', 's_45', 'add', 'mul', 's-', '3', '2', 'mul', 's_14', 's_35', 'add', 'mul', 's-', '3', '2', 'mul', 's_15', 'pow', 'm_d', 's+', '2', 'add', 'mul', 's+', '3', '2', 'mul', 's_34', 'pow', 'm_c', 's+', '2', 'mul', 's+', '6', '4', 'mul', 'pow', 'm_c', 's+', '2', 'pow', 'm_d', 's+', '2']
expr_back = prefix_to_sympy(expr_prefix)
expr_back == expr
--> True
```

Might have to add variables to `variables` in `SympyPrefix.py`.

## Integer Encoding
Integers are encoded as "sign digit1 digit2 ...", so e.g.

`123 --> [s+, 1, 2, 3]`
`-12 --> [s-, 1, 2]`

## Multiplication/Summation
In order for it to be invertible one either needs parentheses or every operand has to have a fixed number of arguments.
So `sum 1 2 3` (which would be `1*2*3`) does not work, but needs to be `sum 1 sum 2 3` (sum always takes 2 argumetns).
The same is true for `mult`.


# Why?
In order to work with the expressions in Machine Learning.

