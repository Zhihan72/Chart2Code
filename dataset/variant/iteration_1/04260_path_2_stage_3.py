import matplotlib.pyplot as plt

data = [5, 10, 15, 20, 25, 30]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4']
labels = ['A', 'B', 'C', 'D', 'E', 'F']

plt.figure(figsize=(8, 6))
plt.bar(labels, data, color=colors)
plt.show()