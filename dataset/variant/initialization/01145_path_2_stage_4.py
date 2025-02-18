import matplotlib.pyplot as plt

# Define data
civilizations = ['Egypt', 'Mesop.', 'Greeks', 'Romans', 'Mayans']
wonders_count = [15, 8, 12, 20, 5]

# New colors for the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF']

# Explode certain slices for emphasis
explode = (0, 0.1, 0, 0.1, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    wonders_count,
    labels=civilizations,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    startangle=140
)

# Display the plot
plt.show()