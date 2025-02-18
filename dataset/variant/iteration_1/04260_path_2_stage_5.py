import matplotlib.pyplot as plt

data = [5, 10, 15, 20, 30]
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#911eb4']
labels = ['X', 'B', 'Z', 'D', 'L']  # Altered the labels

plt.figure(figsize=(8, 6))
plt.bar(labels, data, color=colors)
plt.title('Randomized Bar Chart Title')  # Changed the title
plt.xlabel('Categories XYZDL')  # Altered the x-axis label
plt.ylabel('Values')  # Altered the y-axis label
plt.show()