import numpy as np

def cos2(x, n):
    if n == 2:
        H_2 = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
        return H_2 @ x
    else:
        # recursive case: n >= 4
        n1 = n // 2
        
        # Orthogonal matrix (Hadamard-like)
        I_half = np.eye(n1)
        I_tilde_half = np.flip(I_half, axis=1)
        H = np.block([
            [I_half, I_tilde_half], 
            [I_half, -I_tilde_half]
        ])
        H_n = (1 / np.sqrt(2)) * H
        u = H_n @ x
        
        # Diagonal weight matrix [W_c] - matrix 3
        W_entries = [1] * n1 + [ (1 / np.cos((2*k - 1)*np.pi / (2*n))) / 2 for k in range(1, n1+1) ]
        W_c = np.diag(W_entries)
        v = W_c @ u
        
        # Recursive DCT-II on halves - matrix 2
        z1 = cos2(v[:n1], n1)
        z2 = cos2(v[n1:], n1)
        
        # Bidiagonal matrix - matrix 1
        B = np.eye(n1)
        np.fill_diagonal(B[:-1, 1:], 1)
        B[0, 0] = np.sqrt(2)
        B_c = np.block([
            [np.eye(n1), np.zeros((n1, n1))], 
            [np.zeros((n1, n1)), B]
        ])
        w = B_c @ np.concatenate([z1, z2])
        
        y_my = np.concatenate([w[::2], w[1::2]])
        perm = np.arange(n).reshape(2, -1).T.flatten()
        y = w[perm]

        return y


  def cos3(x, n):
    if n == 2:
        # base case: n = 2
        H_2 = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
        y = H_2 @ x
        return y

    else:
        # recursive case: n >= 4
        n1 = n // 2

        P_n = np.concatenate([x[::2], x[1::2]])

        B = np.eye(n1)
        np.fill_diagonal(B[:-1, 1:], 1)
        B[0, 0] = np.sqrt(2)

        B_c_T = np.block([
            [np.eye(n1), np.zeros((n1, n1))],
            [np.zeros((n1, n1)), B.T]
        ])
        u = B_c_T @ P_n

        z1 = cos3(u[:n1], n1)
        z2 = cos3(u[n1:], n1)

        W_c = np.diag([1] * n1 + [1 / np.cos((2 * k - 1) * np.pi / (2 * n)) / 2 for k in range(1, n1 + 1)])
        w = W_c @ np.concatenate([z1, z2])

        I_half = np.eye(n1)
        I_tilde_half = np.flip(I_half, axis=1)
        H = np.block([
            [I_half, I_tilde_half],
            [I_half, -I_tilde_half]
        ])
        H_n_T = (1 / np.sqrt(2)) * H.T
        y = H_n_T @ w

        return y

####################################################################

# Test case

encoded_dataset = np.array([cos2(message, n) for message in dataset])
encoded_dataset[np.abs(encoded_dataset) < 1e-10] = 0
encoded_dataset = np.round(encoded_dataset, decimals=10)
print(encoded_dataset)

decoded_dataset = np.array([cos3(encode, n) for encode in encoded_dataset])
decoded_dataset[np.abs(decoded_dataset) < 1e-10] = 0
decoded_dataset = np.round(decoded_dataset, decimals=10)
print(decoded_dataset)


