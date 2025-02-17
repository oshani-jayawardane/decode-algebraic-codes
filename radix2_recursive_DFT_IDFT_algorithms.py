import numpy as np
from scipy.fft import fft, ifft

def dft(u, n):
    n1 = n // 2
    if n == 2:  
        return np.array([u[0] + u[1], u[0] - u[1]])
    
    zeta = np.exp(-2j * np.pi / n)
    Dn = np.diag([zeta**k for k in range(n1)])
    Hn = np.block([[np.eye(n1), np.eye(n1)],
                   [Dn, -Dn]])
    
    p = np.dot(Hn, u)
    
    s1 = dft(p[:n1], n1)
    s2 = dft(p[n1:], n1)
    
    interleaved = np.empty((len(s1) + len(s2)), dtype=complex)
    interleaved[0::2] = s1  # even indices with s1
    interleaved[1::2] = s2  # odd indices with s2
    
    y = interleaved

    return y


def idft(y, n):
    n1 = n// 2
    
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

#############################################################

# Test Case

np.random.seed(42)

n = 16
q = 5
num_samples = 3

dataset = np.random.randint(0, q, size=(num_samples, n))
print(dataset)

encoded_dataset = np.array([dft(message, n) for message in dataset])
encoded_dataset[np.abs(encoded_dataset) < 1e-10] = 0
encoded_dataset = np.round(encoded_dataset, decimals=10)
print(encoded_dataset)

decoded_dataset = np.array([idft(encode, n) for encode in encoded_dataset])
decoded_dataset[np.abs(decoded_dataset) < 1e-10] = 0
decoded_dataset = np.round(decoded_dataset, decimals=10)
print(decoded_dataset)

