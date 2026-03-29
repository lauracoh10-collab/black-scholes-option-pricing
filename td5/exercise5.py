import numpy as np
from scipy.integrate import quad

J=5
h=1/(J+1)
alpha=1
beta=2

def phi(x,j):
    if x< (j-1)*h: return 0
    elif x< j*h: return 1+ (x-j*h)/h
    elif x<(j+1)*h: return 1- (x-j*h)/h
    else: return 0

def phi_prime(x,j):
    if x< (j-1)*h: 
        return 0
    elif x<j*h: 
        return 1/h
    elif x< (j+1)*h:
        return -1/h
    else: 
        return 0
    
def phi_prime_phi_prime(x,i,j):
    return phi_prime(x,i)*phi_prime(x,j)


Ah=np.zeros((J,J),float)

for i in range(J):
    for j in range(J):
        integral, error = quad(phi_prime_phi_prime, 0, 1, args= (1+i, j+1))
        Ah[i, j] = integral





def f(x): return 12*(x**2)

def f_times_phi(x,j):
    return f(x)*phi(x,j)

Fh=np.zeros((J), float)

for i in range(J):
    j=i+1
    integral,error= quad(f_times_phi, 0, 1, args=(j))
    Fh[i]=integral

Uh= np.linalg.solve(Ah,Fh)
#Uh= np.allclose(Ah @ Uh, Fh)

def u_lifted(x): #u tilde
    val=0
    for j in range(1,J+1):
        val+=Uh[j-1]*phi(x,j)
    return val

def u0(x):
    return (alpha+ (beta-alpha)*x)

def u_unlifted(x):
    return u_lifted(x)+ u0(x)

Nx=200

x=np.arange(Nx, dtype=float)
y=np.arange(Nx, dtype=float)

s=0

for t in np.linspace(0.0, 1.0, Nx):
    x[s]=t
    y[s]= u_unlifted(t)
    s+= 1

import matplotlib.pyplot as plt




z= np.arange(Nx, dtype=float)

s=0
for t in np.linspace(0.0, 1.0, Nx):
    z[s]=-(t**4)+ 2*t+1
    s+= 1


plt.plot(x,y, "r", label="approx")
plt.plot(x,z, "b", label="exact")
plt.legend()
plt.show()
