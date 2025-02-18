import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
new_york = np.array([30, 32, 45, 55, 65, 75, 80, 78, 70, 60, 50, 35])
los_angeles = np.array([55, 58, 60, 65, 70, 75, 80, 82, 78, 70, 62, 58])
chicago = np.array([25, 28, 40, 50, 60, 70, 75, 73, 65, 55, 45, 30])
houston = np.array([50, 55, 60, 70, 80, 85, 90, 92, 85, 75, 65, 55])
miami = np.array([60, 62, 68, 72, 78, 85, 88, 87, 83, 77, 68, 62]) # New data series

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(months, new_york, marker='o', linestyle='-', markersize=6, linewidth=2, label='New York', color='red')
ax.plot(months, los_angeles, marker='s', linestyle='--', markersize=6, linewidth=2, label='Los Angeles', color='green')
ax.plot(months, chicago, marker='^', linestyle='-', markersize=6, linewidth=2, label='Chicago', color='orange')
ax.plot(months, houston, marker='D', linestyle=':', markersize=6, linewidth=2, label='Houston', color='blue')
ax.plot(months, miami, marker='p', linestyle='-.', markersize=6, linewidth=2, label='Miami', color='purple') # Plot new data

ax.set_title("Temperature Trends in Major US Cities Over One Year", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Temperature (°F)', fontsize=14)
ax.legend(title='Cities', fontsize=12, title_fontsize=14, loc='upper left')

ax.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

annotations = {
    'New York': [0, 3],   
    'Los Angeles': [0, 7],
    'Chicago': [0, 6],
    'Houston': [0, 7],
    'Miami': [0, 8] # Add annotations for Miami
}

for city, data in zip(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], [new_york, los_angeles, chicago, houston, miami]):
    for idx in annotations[city]:
        ax.annotate(f"{data[idx]}°F", 
                    (months[idx], data[idx]), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    arrowprops=dict(arrowstyle='->', linestyle='-', color='black'))

plt.tight_layout()
plt.show()