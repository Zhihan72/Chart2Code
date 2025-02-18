import matplotlib.pyplot as plt

# Define the data
shares = [35, 25, 20, 10]

# Define new colors for each sector
new_colors = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8']

# Define explode to highlight the 'Solar Power' sector
explode = (0.1, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, _, _ = ax.pie(
    shares, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=new_colors, 
    explode=explode
)

plt.tight_layout()
plt.show()