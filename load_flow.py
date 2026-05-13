import numpy as np

BASE_MVA = 10
BASE_KV = 12.66
Z_base = (BASE_KV ** 2) / BASE_MVA

def convert_to_pu(line_data):
    line_data = np.array(line_data, dtype=float)
    for i in range(len(line_data)):
        line_data[i][2] /= Z_base
        line_data[i][3] /= Z_base
    return line_data

def load_flow(line_data, load_data, max_iter=100, tol=1e-6):

    nb = int(max(line_data[:,1]))
    nl = len(line_data)

    children = {i: [] for i in range(1, nb+1)}
    for i in range(nl):
        fb, tb = int(line_data[i][0]), int(line_data[i][1])
        children[fb].append(i)

    V = np.ones(nb+1, dtype=complex)

    for _ in range(max_iter):
        V_prev = V.copy()

        I_load = np.zeros(nb+1, dtype=complex)
        for bus in load_data:
            P, Q = load_data[bus]
            S = complex(P/(BASE_MVA*1000), Q/(BASE_MVA*1000))
            I_load[bus] = np.conj(S / V[bus])

        I_branch = np.zeros(nl, dtype=complex)

        for i in reversed(range(nl)):
            fb, tb = int(line_data[i][0]), int(line_data[i][1])
            I_branch[i] = I_load[tb]
            for child in children[tb]:
                I_branch[i] += I_branch[child]

        V[1] = 1 + 0j

        for i in range(nl):
            fb, tb, R, X = int(line_data[i][0]), int(line_data[i][1]), line_data[i][2], line_data[i][3]
            Z = complex(R, X)
            V[tb] = V[fb] - Z * I_branch[i]

        if np.max(np.abs(V - V_prev)) < tol:
            break

    return V, I_branch

def calculate_loss(line_data, I_branch):
    loss = 0
    for i in range(len(line_data)):
        R = line_data[i][2]
        loss += (abs(I_branch[i])**2) * R
    return loss