import matplotlib.pyplot as plt
import numpy as np

# Data preparation
years = np.arange(2011, 2021)
apples_vitamin_c = np.array([5, 5.2, 5.3, 5.4, 5.1, 5.5, 5.7, 5.8, 5.6, 5.7])
apples_fiber = np.array([2.5, 2.6, 2.7, 2.6, 2.5, 2.8, 3.0, 3.1, 3.2, 3.3])
oranges_vitamin_c = np.array([50, 52, 53, 55, 54, 56, 57, 58, 59, 60])
oranges_fiber = np.array([2.4, 2.5, 2.5, 2.6, 2.5, 2.7, 2.8, 2.9, 3.0, 3.1])
bananas_vitamin_c = np.array([9, 8.9, 9.1, 9.2, 8.8, 9.3, 9.4, 9.5, 9.6, 9.6])
bananas_fiber = np.array([2.6, 2.7, 2.8, 2.9, 2.8, 3.0, 3.1, 3.2, 3.3, 3.4])
strawberries_vitamin_c = np.array([58, 60, 62, 63, 64, 65, 66, 67, 68, 69])
strawberries_fiber = np.array([2.9, 3.0, 3.1, 3.2, 3.2, 3.4, 3.5, 3.6, 3.7, 3.8])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot Vitamin C content
ax1.plot(years, apples_vitamin_c, color='#FF6347', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, oranges_vitamin_c, color='#FFA500', marker='s', linestyle='-', linewidth=2)
ax1.plot(years, bananas_vitamin_c, color='#FFD700', marker='^', linestyle='-', linewidth=2)
ax1.plot(years, strawberries_vitamin_c, color='#FF69B4', marker='d', linestyle='-', linewidth=2)

# Add secondary y-axis for Fiber content
ax2 = ax1.twinx()
ax2.plot(years, apples_fiber, color='#008000', marker='o', linestyle='--', linewidth=2)
ax2.plot(years, oranges_fiber, color='#556B2F', marker='s', linestyle='--', linewidth=2)
ax2.plot(years, bananas_fiber, color='#8B4513', marker='^', linestyle='--', linewidth=2)
ax2.plot(years, strawberries_fiber, color='#32CD32', marker='d', linestyle='--', linewidth=2)

# Title and labels
ax1.set_title("Nutrient Analysis of Popular Fruits (2011-2020)", fontsize=18, weight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Vitamin C Content (mg/100g)", fontsize=14, color='black')
ax2.set_ylabel("Fiber Content (g/100g)", fontsize=14, color='black')

# Customize ticks
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Add data labels for Vitamin C content
for i in range(len(years)):
    ax1.annotate(f'{apples_vitamin_c[i]}', (years[i], apples_vitamin_c[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10, color='#FF6347')
    ax1.annotate(f'{oranges_vitamin_c[i]}', (years[i], oranges_vitamin_c[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10, color='#FFA500')
    ax1.annotate(f'{bananas_vitamin_c[i]}', (years[i], bananas_vitamin_c[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10, color='#FFD700')
    ax1.annotate(f'{strawberries_vitamin_c[i]}', (years[i], strawberries_vitamin_c[i]), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10, color='#FF69B4')

# Add data labels for Fiber content
for i in range(len(years)):
    ax2.annotate(f'{apples_fiber[i]}', (years[i], apples_fiber[i]), textcoords="offset points", xytext=(5, -10), ha='center', fontsize=10, color='#008000')
    ax2.annotate(f'{oranges_fiber[i]}', (years[i], oranges_fiber[i]), textcoords="offset points", xytext=(5, -10), ha='center', fontsize=10, color='#556B2F')
    ax2.annotate(f'{bananas_fiber[i]}', (years[i], bananas_fiber[i]), textcoords="offset points", xytext=(5, -10), ha='center', fontsize=10, color='#8B4513')
    ax2.annotate(f'{strawberries_fiber[i]}', (years[i], strawberries_fiber[i]), textcoords="offset points", xytext=(5, -10), ha='center', fontsize=10, color='#32CD32')

# Ensure the layout is tight
plt.tight_layout()

# Show plot
plt.show()