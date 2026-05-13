from load_flow import load_flow, calculate_loss, convert_to_pu
from data import line_data, load_data

line_data_pu = convert_to_pu(line_data)

V, I = load_flow(line_data_pu, load_data)

print("\nBase Case Results:\n")

for i in range(1, 34):
    print(f"Bus {i}: {abs(V[i]):.4f} pu")

loss = calculate_loss(line_data_pu, I)
print(f"\nTotal Power Loss: {loss:.6f} pu")