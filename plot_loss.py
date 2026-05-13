import matplotlib.pyplot as plt

labels = ['Base', 'Reconfigured', 'Quantum']

# Use your actual values
losses = [0.0211, 0.00727, 0.0043]  

plt.bar(labels, losses)

plt.xlabel("Method")
plt.ylabel("Power Loss (pu)")
plt.title("Loss Reduction Comparison")

for i, v in enumerate(losses):
    plt.text(i, v + 0.0005, f"{v:.4f}", ha='center')

plt.show()