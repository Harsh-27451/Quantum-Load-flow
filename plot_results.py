import matplotlib.pyplot as plt
from load_flow import load_flow, convert_to_pu
from data import line_data, load_data

line_data_pu = convert_to_pu(line_data)
V, _ = load_flow(line_data_pu, load_data)

voltages = [abs(V[i]) for i in range(1, 34)]

plt.plot(range(1,34), voltages, marker='o')
plt.xlabel("Bus Number")
plt.ylabel("Voltage (pu)")
plt.title("Voltage Profile - IEEE 33 Bus System")
plt.grid()

plt.show()