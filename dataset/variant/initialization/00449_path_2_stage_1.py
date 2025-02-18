import matplotlib.pyplot as plt

# Define data for the pie chart
meanings = [40, 20, 15, 15, 10]
colors = ['#FF6347', '#FFD700', '#D8BFD8', '#FFDEAD', '#9ACD32']
explode = (0.1, 0, 0, 0, 0)

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(meanings, startangle=140, colors=colors, explode=explode,
       shadow=True, wedgeprops={'edgecolor': 'black'})

# Ensure the pie chart is a circle
ax.axis('equal')

# Display the chart
plt.show()