import matplotlib.pyplot as plt

# Define data for the donut pie chart with additional data series
meanings = [40, 20, 15, 15, 10, 25, 5]
colors = ['#FF6347', '#FFD700', '#D8BFD8', '#FFDEAD', '#9ACD32', '#00CED1', '#FF69B4']
explode = (0.1, 0, 0, 0, 0, 0, 0)

# Plotting the donut pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(meanings, startangle=140, colors=colors, explode=explode,
                       shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1})

# Draw circle for donut shape
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the chart is a circle
ax.axis('equal')

# Display the chart
plt.show()