import sympy

# Defining Symbols
x = sympy.Symbol('x')
a, b, c = sympy.symbols('a, b, c')

# Expression in Sympy
y = a * x**2 + b*x + c

# Sympify
x_root_1 = sympy.sympify('(-b + sqrt(b**2 - 4*a*c))/(2*a)')
x_root_2 = sympy.sympify('(-b - sqrt(b**2 - 4*a*c))/(2*a)')

# Substitution
y_subs = y.subs(x, x_root_1)

# Simplification
y_should_be_zero = y_subs.simplify()

# Solving
x_roots = sympy.solve(y, x)

# Differentiation
y_prime = y.diff(x)

# Lambdify (Turn SymPy expressions into normal functions)
x_root_fun = sympy.lambdify([a, b, c], x_root_2)
y_fun = sympy.lambdify([x, a, b, c], y)

num_a, num_b, num_c = 1.5, -2.5, 1.
this_should_also_be_zero = y_fun(x_root_fun(num_a, num_b, num_c), num_a, num_b, num_c)



