import matplotlib.pyplot as plt

ship_types = ['Defense', 'Exploration', 'Medical', 'Cargo', 'Diplomatic', 'Transport', 'Scientific']
percentages = [30, 20, 5, 15, 10, 10, 10]
# Shuffled colors list
colors = ['#8c564b', '#e377c2', '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(percentages, autopct='%1.1f%%', startangle=140, colors=colors, labels=ship_types)

ax.set_title('Starship Missions')
ax.set_xlabel('Axis X Label Altered')
ax.set_ylabel('Axis Y Label Altered')

plt.show()