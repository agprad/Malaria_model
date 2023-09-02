import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Parameters
alpha = 3.64
gamma_scd = 0.75
gamma_A_mal = 0.042
gamma_T_mal = 0.0047
gamma_C_mal = 0.047
gamma_natural = 0.346
mt = 0.2
ma = 0.1
initals = [0, 0, 0, 1/3, 1/3, 1/3, 0, 0,0]
# u v w x y z d e f
#function
def Disease(x,t):
    u = x[0] #Child Afflicted
    v = x[1] #Child Non Carrier
    w = x[2] #Child Carrier
    X = x[3] #Adult Afflicted
    y = x[4] #Adult Non Carrier
    z = x[5] #Adult Carrier
    d = x[6] #Teen afflicted
    e = x[7] #Teen Carrier
    f = x[8] #Teen Non Carrier
    dx = np.zeros(9)
    dx[0] = 0.25*alpha*z*z*(1-(u+v+w+X+y+z+d+e+f))/((X+y+z)) - mt*u - gamma_scd*u
    dx[1] = alpha*(1-(u+v+w+X+y+z+d+e+f))*(y*y/(X+y+z) + 0.5*y*z/(X+y+z) +
    0.25*z*z/(X+y+z) ) - mt*v - gamma_C_mal*v
    dx[2] = alpha*(0.5*z*z/(X+y+z) + 0.5*y*z/(X+y+z))*(1-(u+v+w+X+y+z+d+e+f)) - mt*w
    dx[3] = ma*d - gamma_scd*X - gamma_natural*X
    dx[4] = ma*f - gamma_A_mal*y - gamma_natural*y
    dx[5] = ma*e - gamma_natural*z
    dx[6] = mt*u - ma*d - gamma_scd*d
    dx[7] = mt*w - ma*e
    dx[8] = mt*v - ma*f - gamma_T_mal*f
    return dx
#solving odes
t = np.array(np.linspace(0,1000,50000))
x = np.array(odeint(Disease,initals,t))
u = x[:,0]
v = x[:,1]
w = x[:,2]
X = x[:,3]
y = x[:,4]
z = x[:,5]
d = x[:,6]
e = x[:,7]
f = x[:,8]
N = X+y+z+u+v+w+d+e+f
#plotting
plt.figure(figsize=(8,5))
plt.plot(t,u,label = 'Child Afflicted')
plt.plot(t,v,label = 'Child Non Carrier')
plt.plot(t,w,label = 'Child Carrier')
plt.plot(t,X,label = 'Adult Afflicted')
plt.plot(t,y,label = 'Adult Non Carrier')
plt.plot(t,z,label = 'Adult Carrier')
plt.plot(t,d,label = 'Teen afflicted')
plt.plot(t,e,label = 'Teen Carrier')
plt.plot(t,f,label = 'Teen Non Carrier')
plt.plot(t,N,label = 'Total')
plt.legend(loc="best")
plt.xlabel("Years")
plt.ylabel("Fraction")
plt.show()