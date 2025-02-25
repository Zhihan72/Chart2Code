import matplotlib.pyplot as plt

# Data: Activities and their corresponding percentage shares
activities = ['Social Media', 'Entertainment', 'Online Shopping', 'Education', 'Work', 'News Reading', 'Other']
percentages = [30, 20, 15, 10, 10, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c7f0c2']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(activities, percentages, color=colors, edgecolor='black')

# Title and axis labels
ax.set_title("2023 Global Internet Users' Activity Distribution", fontsize=14, weight='bold', pad=20)
ax.set_xlabel("Percentage (%)", fontsize=12)

# Invert y-axis to have the highest percentage on top
ax.invert_yaxis()

# Annotate percentage values on each bar
for i in range(len(activities)):
    ax.text(percentages[i] + 1, i, f'{percentages[i]}%', va='center', fontsize=10, weight='bold')

# Display the plot
plt.tight_layout()
plt.show()