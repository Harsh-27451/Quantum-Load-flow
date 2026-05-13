# -----------------------------
# IMPORTS (COMPATIBLE VERSION)
# -----------------------------
from qiskit.algorithms.minimum_eigensolvers import QAOA
from qiskit.primitives import Sampler
from qiskit.algorithms.optimizers import COBYLA

from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer


# -----------------------------
# DEFINE QUBO PROBLEM
# -----------------------------
qp = QuadraticProgram()

# 5 binary variables (tie switches)
for i in range(5):
    qp.binary_var(name=f'x{i}')

# Objective: minimize loss
linear = {
    'x0': -0.003,
    'x1': -0.0138,
    'x2': -0.002,
    'x3': -0.0015,
    'x4': -0.0025
}

qp.minimize(linear=linear)

# Constraint: at most 2 switches ON
qp.linear_constraint(
    linear={'x0':1,'x1':1,'x2':1,'x3':1,'x4':1},
    sense='<=',
    rhs=2
)


# -----------------------------
# QAOA SETUP
# -----------------------------
sampler = Sampler()
optimizer = COBYLA(maxiter=100)

qaoa = QAOA(sampler=sampler, optimizer=optimizer, reps=2)

algo = MinimumEigenOptimizer(qaoa)


# -----------------------------
# RUN OPTIMIZATION
# -----------------------------
result = algo.solve(qp)


# -----------------------------
# OUTPUT
# -----------------------------
print("\nOptimal Solution:")
print(result)

print("\nSelected Switches:")

tie_map = ["8-21", "9-15", "12-22", "18-33", "25-29"]

for i, val in enumerate(result.x):
    if val == 1:
        print(f"Activate Tie Line: {tie_map[i]}")