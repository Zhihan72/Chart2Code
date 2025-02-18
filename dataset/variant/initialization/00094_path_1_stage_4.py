import matplotlib.pyplot as plt

# Randomly altered labels and text
ship_types = ['Defense', 'Exploration', 'Medical', 'Cargo', 'Diplomatic', 'Transport', 'Scientific']
percentages = [30, 20, 5, 15, 10, 10, 10]
colors = ['#ff7f0e', '#1f77b4', '#8c564b', '#2ca02c', '#9467bd', '#e377c2', '#d62728']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, labels=ship_types)

# Changed title and labels
ax.set_title('Starship Missions')
ax.set_xlabel('Axis X Label Altered')
ax.set_ylabel('Axis Y Label Altered')

plt.show()