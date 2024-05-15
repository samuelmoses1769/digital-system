import sympy as sp

t = sp.Symbol('t')

def f(t):
    return sp.Piecewise((1, t >= 0), (0, True))

def laplace_transform(f, t, s):
    return sp.integrate(sp.exp(-s * t) * f(t), (t, 0, sp.oo))

F_transform = laplace_transform(f, t, sp.symbols('s'))

print(F_transform)