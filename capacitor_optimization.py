import matplotlib.pyplot as plt
from load_flow import load_flow, convert_to_pu
from data import line_data, load_data

# -------------------------
# BASE CASE
# -------------------------
line_data_pu = convert_to_pu(line_data)

V_base, loss_base = load_flow(line_data_pu, load_data)
volt_base = [abs(V_base[i]) for i in range(1, 34)]

# Convert loss to float safely
loss_base = float(loss_base[0] if hasattr(loss_base, "__len__") else loss_base)

# -------------------------
# CAPACITOR PLACEMENT
# -------------------------
load_data_cap = load_data.copy()

# Add capacitors at weak buses
for bus in [30, 31, 32]:
    P, Q = load_data_cap[bus]
    load_data_cap[bus] = (P, Q - 50)   # inject 50 kVAR

# -------------------------
# RUN LOAD FLOW AGAIN
# -------------------------
V_cap, loss_cap = load_flow(line_data_pu, load_data_cap)
volt_cap = [abs(V_cap[i]) for i in range(1, 34)]

# Convert loss to float safely
loss_cap = float(loss_cap[0] if hasattr(loss_cap, "__len__") else loss_cap)

# -------------------------
# PRINT RESULTS
# -------------------------
print("\n--- Capacitor Optimization ---")
print(f"Base Loss: {loss_base:.6f} pu")
print(f"With Capacitor Loss: {loss_cap:.6f} pu")

# -------------------------
# VOLTAGE COMPARISON PLOT
# -------------------------
bus = range(1, 34)

plt.plot(bus, volt_base, label="Base", marker='o')
plt.plot(bus, volt_cap, label="With Capacitor", marker='x')

plt.xlabel("Bus Number")
plt.ylabel("Voltage (pu)")
plt.title("Voltage Improvement using Capacitor Placement")

plt.legend()
plt.grid()
plt.show()

# -------------------------
# LOSS COMPARISON PLOT
# -------------------------
labels = ['Base', 'Capacitor']
losses = [loss_base, loss_cap]

plt.figure()
plt.bar(labels, losses)

plt.ylabel("Power Loss (pu)")
plt.title("Loss Reduction using Capacitor Placement")

for i, v in enumerate(losses):
    plt.text(i, v + 0.0005, f"{v:.4f}", ha='center')

plt.show()