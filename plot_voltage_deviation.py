import matplotlib.pyplot as plt
from load_flow import load_flow, convert_to_pu
from data import line_data, load_data
import numpy as np

# -------------------------
# BASE CASE
# -------------------------
line_data_pu = convert_to_pu(line_data)
V_base, _ = load_flow(line_data_pu, load_data)
volt_base = [abs(V_base[i]) for i in range(1, 34)]

# -------------------------
# OPTIMIZED CASE
# (Close 9-15, Open 5-6)
# -------------------------
line_data_opt = np.array(line_data).tolist()

# Add tie line
line_data_opt.append([9,15,0.0,0.0])

# Remove line 5-6
line_data_opt = [line for line in line_data_opt if not (line[0]==5 and line[1]==6)]

line_data_opt = convert_to_pu(line_data_opt)

V_opt, _ = load_flow(line_data_opt, load_data)
volt_opt = [abs(V_opt[i]) for i in range(1, 34)]

# -------------------------
# VOLTAGE DEVIATION
# -------------------------
dev_base = [abs(v - 1.0) for v in volt_base]
dev_opt = [abs(v - 1.0) for v in volt_opt]

# -------------------------
# PLOT
# -------------------------
bus = range(1,34)

plt.plot(bus, dev_base, label="Base", marker='o')
plt.plot(bus, dev_opt, label="Optimized", marker='x')

plt.xlabel("Bus Number")
plt.ylabel("Voltage Deviation (|V - 1|)")
plt.title("Voltage Deviation Comparison")

plt.legend()
plt.grid()

plt.show()