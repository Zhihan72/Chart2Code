import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Mar", "May", "Feb", "Aug", "Jun", "Apr", "Sep", "Jul", "Oct", "Nov", "Dec", "Jan"])
city1_temp = np.array([10, 20, 7, 29, 25, 15, 23, 30, 17, 10, 6, 5])
city3_temp = np.array([8, 17, 2, 26, 22, 12, 21, 27, 15, 8, 3, 0])

fig, ax = plt.subplots(figsize=(12, 6))

# Changed colors for the city temperature plots
ax.plot(months, city1_temp, marker='o', linestyle='-', color='m')  # Changed from 'b' to 'm'
ax.plot(months, city3_temp, marker='d', linestyle='-.', color='c')  # Changed from 'g' to 'c'

ax.set_title("City Temperature Changes Throughout 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Time of Year", fontsize=12)
ax.set_ylabel("Degrees Celsius", fontsize=12)

for i in range(len(months)):
    ax.text(months[i], city1_temp[i] + 0.5, f"{city1_temp[i]}°C", ha='center', va='bottom', fontsize=9)
    ax.text(months[i], city3_temp[i] + 0.5, f"{city3_temp[i]}°C", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()