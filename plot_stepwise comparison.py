import matplotlib.pyplot as plt

labels = ['Base', 'Reconfig', 'Quantum']
loss = [0.0211, 0.00727, 0.0043]

plt.bar(labels, loss)

plt.xlabel("Stage")
plt.ylabel("Loss (pu)")
plt.title("Stepwise Loss Comparison")

for i, v in enumerate(loss):
    plt.text(i, v + 0.0005, f"{v:.4f}", ha='center')

plt.show()