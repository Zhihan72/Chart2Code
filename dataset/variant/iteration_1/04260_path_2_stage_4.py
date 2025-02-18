import matplotlib.pyplot as plt

data = [5, 10, 15, 20, 30]  # Removed data point 25 corresponding to label E
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#911eb4']  # Removed color for label E
labels = ['A', 'B', 'C', 'D', 'F']  # Removed label E

plt.figure(figsize=(8, 6))
plt.bar(labels, data, color=colors)
plt.show()