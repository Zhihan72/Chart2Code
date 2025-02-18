import matplotlib.pyplot as plt

# Data
consumption_percentages = [20, 20, 15, 20, 15, 10]
colors = ['#6db33f', '#e07b39', '#9cc3d5', '#d58339', '#a34f4f', '#8B4513']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Donut chart
ax.pie(
    consumption_percentages, colors=colors,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.4), explode=(0.05,) * len(consumption_percentages)
)

# Display the plot
plt.show()