import matplotlib.pyplot as plt

# Data series
percentages = [25, 35, 15, 10, 15, 8, 12]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

fig, ax = plt.subplots(figsize=(8, 8))

# Create a standard pie chart without radial style
ax.pie(percentages, startangle=140, colors=colors)

plt.show()