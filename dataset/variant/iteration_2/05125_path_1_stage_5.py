import matplotlib.pyplot as plt

franchises = ['ST', 'SW', 'DW', 'Dune', 'Other', 'Exp']
popularity_percentages = [25, 30, 10, 15, 10, 10]  # Shuffled values within the list
colors = ['#1e90ff', '#ff4500', '#ff8c00', '#32cd32', '#ff1493', '#6a5acd']  # Shuffled colors to match data
explode = (0, 0.1, 0, 0, 0, 0)  # Shuffled explode to match the highest value

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(
    popularity_percentages, 
    explode=explode, 
    labels=franchises, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9)
)

ax.set_aspect('equal')
plt.show()