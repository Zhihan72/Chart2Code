import matplotlib.pyplot as plt

# Define star systems with coordinates (x, y), brightness
star_systems = [
    [2, 3, 5.6],  
    [7, 1, 4.2],  
    [1, 9, 7.1],  
    [6, 8, 6.3],  
    [9, 5, 8.4]   
]

# Using y_coords as the category and brightness as the bar length
y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]

fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
ax.barh(y_coords, brightness, color='blue', alpha=0.7, edgecolor='black')

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()