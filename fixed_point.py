from scipy.optimize import fsolve
def equations(vars):
    alpha = 3.64
    gamma_scd = 0.75
    gamma_A_mal = 0.042
    gamma_T_mal = 0.0047
    gamma_C_mal = 0.047
    gamma_natural = 0.346
    ma = 0.1
    mt = 0.2
    u,v,w,X, y,z,d,e,f = vars
    eq1 = 0.25*alpha*z*z*(1-(u+v+w+X+y+z+d+e+f))/((X+y+z)) - mt*u - gamma_scd*u
    eq2 = alpha*(1-(u+v+w+X+y+z+d+e+f))*(y*y/(X+y+z) + 0.5*y*z/(X+y+z) +
    0.25*z*z/(X+y+z) ) - mt*v - gamma_C_mal*v
    eq3 = alpha*(0.5*z*z/(X+y+z) + 0.5*y*z/(X+y+z))*(1-(u+v+w+X+y+z+d+e+f)) - mt*w
    eq4 = ma*d - gamma_scd*X - gamma_natural*X
    eq5 = ma*f - gamma_A_mal*y - gamma_natural*y
    eq6 = ma*e - gamma_natural*z
    eq7 = mt*u - ma*d - gamma_scd*d
    eq8 = mt*w - ma*e
    eq9 = mt*v - ma*f - gamma_T_mal*f
    return [eq1, eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9]
u,v,w,x,y,z,d,e,f = fsolve(equations,(1,1,1,1,1,1,1,1,1))
print(f"""u = {u}
v = {v}
w = {w}
x = {x}
y = {y}
z = {z}
d = {d}
e = {e}
f = {f}""")
