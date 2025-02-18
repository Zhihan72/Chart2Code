import matplotlib.pyplot as plt

# Define the data
shares = [35, 25, 20, 10]

# Define new colors for each sector
new_colors = ['#3cb44b', '#4363d8', '#e6194B', '#ffe119']

# Define explode for highlighting a sector
explode = (0, 0.1, 0, 0)

# Create the donut chart
fig, ax = plt.subplots(figsize=(9, 9))
wedges, text_labels, percent_labels = ax.pie(
    shares, 
    autopct='%1.1f%%', 
    startangle=180, 
    colors=new_colors, 
    explode=explode, 
    shadow=True,
    wedgeprops=dict(width=0.3)  # Adding a width to create the donut shape
)

# Add legend with different location
ax.legend(wedges, ['Hydro', 'Wind', 'Solar', 'Biomass'], loc="upper left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()