import numpy as np

def padded_generator_matrix(n, w0, z0):
    zeta = np.exp(-2j * np.pi / n)
    M_tilde = np.array([[(w0 / z0) ** j * zeta**(k * j) for j in range(n)] for k in range(n)], dtype=complex)
    return M_tilde

def idft(y, n):
    n1 = n // 2
    
    if n == 2:
        return np.array([y[0] + y[1], y[0] - y[1]]) / 2
    
    elif n >= 4:
        q = np.concatenate((y[0:n:2], y[1:n:2]))
        
        b1 = idft(q[:n1], n1)
        b2 = idft(q[n1:], n1)
        
        b_out = np.concatenate((b1, b2))
        
        zeta = np.exp(-2j * np.pi / n)
        Dn = np.diag([zeta**k for k in range(n1)])
        Hn = np.block([[np.eye(n1), np.eye(n1)],
                       [Dn, -Dn]])
        
        Hn_conj = np.conjugate(Hn).T
        z1 = np.dot(Hn_conj, b_out)
        out = z1 / 2
        return out

def lrc(y, n, q, r, w0, z0):
    if n >= 2:
        z1 = idft(y, n)
        
        D_hat_n = np.diag([(z0 / w0) ** k for k in range(n)])
        z2 = np.dot(D_hat_n, z1)
        
        J_rxn = np.hstack([np.eye(r), np.zeros((r, n - r))])
        z3 = np.dot(J_rxn, z2)
        
        z3 = z2
        
        z4 = np.abs(z3)
        
        z5 = np.ceil(z4)
        # z5 = np.round(z4)
        
        x_tilde = np.mod(z5, q)
        return x_tilde
    return y

################################################################

# Test Case:

n = 16
r = 3
q = 5

w0 = 4
z0 = 3

x = np.random.randint(0, q, n)
print("original message: ", x)

M_tilde = padded_generator_matrix(n, w0, z0)
y = np.dot(M_tilde, x)
print("\nencoded message: ", y)

x_tilde = lrc(y, n, q, r, w0, z0)
print("\nRecovered x_tilde:", x_tilde)
