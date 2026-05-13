
# Quantum Power System Optimization using HHL, VQLS and QAOA

## Overview

This project presents the application of quantum computing techniques for power system analysis and optimization. Classical load flow methods are compared with quantum algorithms such as HHL (Harrow–Hassidim–Lloyd Algorithm), VQLS (Variational Quantum Linear Solver), and QAOA (Quantum Approximate Optimization Algorithm) on IEEE benchmark distribution systems.

The project focuses on:
- Classical and quantum load flow analysis
- Network reconfiguration
- Loss minimization
- Voltage profile improvement
- Quantum optimization using Qiskit

---

# Objectives

- Perform load flow analysis on IEEE test systems
- Compare classical and quantum approaches
- Apply HHL and VQLS for solving linear systems
- Implement QAOA for distribution network reconfiguration
- Reduce active power losses
- Improve voltage profile of the system

---

# IEEE Test Systems Used

## 1. IEEE 3-Bus System
Used for validating classical and quantum load flow methods.

### Features
- 3 buses
- 3 branches
- Mesh network
- FDLF implementation
- HHL implementation
- VQLS implementation

---

## 2. IEEE 13-Bus System
Used to analyze scalability of quantum load flow methods.

### Features
- Balanced equivalent model
- Load flow analysis
- Quantum linear solver implementation

---

## 3. IEEE 33-Bus System
Used for network reconfiguration and optimization.

### System Specifications
- Number of Buses: 33
- Number of Branches: 32
- Number of Tie Lines: 5
- Base Voltage: 12.66 kV
- Total Active Load: 3.775 MW
- Total Reactive Load: 2.32 MVAr

---

# Methods Implemented

## Classical Methods
- Gauss–Seidel Load Flow
- Newton–Raphson Load Flow
- Fast Decoupled Load Flow (FDLF)

---

## Quantum Methods

### HHL Algorithm
Quantum algorithm used for solving linear systems of equations.

### VQLS
Hybrid quantum-classical algorithm for solving linear systems.

### QAOA
Quantum optimization algorithm used for network reconfiguration and loss minimization.

---

# Network Reconfiguration

The IEEE 33-bus system was optimized using QAOA-based network reconfiguration.

### Objective
- Minimize total power loss
- Maintain radial structure
- Improve voltage profile

### Tie Lines Used
- 8–21
- 9–15
- 12–22
- 18–33
- 25–29

### Optimal Configuration
The QAOA algorithm selected the optimal tie-line combination resulting in minimum loss.

---

# Results

## Base Case Loss
- 2.11 MW

## Optimized Loss
- 0.727 MW

## Loss Reduction
- Approximately 65%

## Improvements Achieved
- Reduced power loss
- Improved voltage profile
- Better network efficiency

---

# Technologies and Tools Used

- Python
- Qiskit
- NumPy
- Matplotlib
- Jupyter Notebook

---

# Repository Structure

```text
Quantum-Power-System-Optimization/
│
├── README.md
├── requirements.txt
│
├── 3_bus_system/
│   ├── fdlf_3bus.py
│   ├── hhl_3bus.py
│   └── vqls_3bus.py
│
├── ieee13_bus/
│   ├── ieee13_fdlf.py
│   ├── ieee13_hhl.py
│   └── ieee13_vqls.py
│
├── ieee33_bus/
│   ├── load_flow.py
│   ├── qaoa_reconfiguration.py
│   ├── capacitor_optimization.py
│   └── data.py
│
├── results/
│   ├── graphs/
│   ├── screenshots/
│   └── outputs/
│
└── thesis/
    └── report.pdf
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Quantum-Power-System-Optimization.git
```

---

## Create Virtual Environment

```bash
python -m venv qiskit_env
```

---

## Activate Environment

### Windows

```bash
.\qiskit_env\Scripts\activate
```

### Linux / Mac

```bash
source qiskit_env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Future Scope

- Real quantum hardware implementation
- Large-scale power system optimization
- Smart grid applications
- Renewable energy integration
- DER and IBR optimization
- Hybrid quantum-classical power system solvers

---

# References

1. A. W. Harrow, A. Hassidim, and S. Lloyd, “Quantum algorithm for linear systems of equations,” Physical Review Letters, Vol. 103, No. 15, 2009.

2. J. R. Shewchuk, “An Introduction to the Conjugate Gradient Method Without the Agonizing Pain,” Carnegie Mellon University, 1994.

3. IBM Quantum Experience, https://quantum-computing.ibm.com/

4. Qiskit Documentation, https://qiskit.org/

---

# Authors

Harsh Jha  
B.Tech Electrical Engineering  
National Institute of Technology Agartala

---

# License

This project is developed for academic and research purposes.
