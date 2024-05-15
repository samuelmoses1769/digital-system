import sympy as sp

t, s = sp.symbols('t s')

def f(t):
    return sp.Piecewise((0, t < 0), (1, (0 <= t) & (t < 1)), (10, (1 <= t) & (t < 6)), (0, t >= 6))

def laplace_transform(f, t, s):
    return sp.integrate(sp.exp(-s * t) * f(t), (t, 0, sp.oo))

F_transform = laplace_transform(f, t, s)

print(F_transform)