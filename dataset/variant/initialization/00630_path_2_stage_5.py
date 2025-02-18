import matplotlib.pyplot as plt

# Data
consumption_percentages = [20, 20, 15, 20, 15, 10]
single_color = '#6db33f'  # Selected a single consistent color

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(aspect="equal"))

# Donut chart
ax.pie(
    consumption_percentages, colors=[single_color] * len(consumption_percentages),
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
    wedgeprops=dict(width=0.4), explode=(0.05,) * len(consumption_percentages)
)

# Display the plot
plt.show()