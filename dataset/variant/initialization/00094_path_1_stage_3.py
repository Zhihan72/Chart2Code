import matplotlib.pyplot as plt

ship_types = ['Exploration', 'Defense', 'Cargo', 'Scientific', 'Diplomatic', 'Medical', 'Transport']
percentages = [20, 30, 15, 10, 10, 5, 10]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, labels=ship_types)

plt.show()