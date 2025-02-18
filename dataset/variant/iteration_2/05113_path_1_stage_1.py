import matplotlib.pyplot as plt
import numpy as np

# Years and corresponding energy consumption efficiency for different EV models
years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])

# Efficiency data for four different EV models
efficiency_model_A = np.array([34, 32, 30, 28, 26, 24, 22])
efficiency_model_B = np.array([36, 34, 33, 29, 27, 25, 23])
efficiency_model_C = np.array([38, 36, 34, 33, 31, 29, 27])
efficiency_model_D = np.array([40, 37, 35, 32, 30, 28, 26])  # New Model D

# Plotting the data
plt.figure(figsize=(14, 8))
plt.plot(years, efficiency_model_A, 'o-', label='EV Model A', color='green')
plt.plot(years, efficiency_model_B, 's--', label='EV Model B', color='blue')
plt.plot(years, efficiency_model_C, 'd-.', label='EV Model C', color='purple')
plt.plot(years, efficiency_model_D, 'x:', label='EV Model D', color='orange')  # Added line for Model D

# Add titles and labels
plt.title('Progress in Electric Vehicle Efficiency (2010-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Efficiency (kWh/100 miles)', fontsize=12)

# Highlight significant improvements with annotations
plt.annotate('Introduction of high-efficiency motors', 
             xy=(2016, 28), xytext=(2014, 32), 
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='blue')
plt.annotate('Advancement in battery technology', 
             xy=(2020, 24), xytext=(2018, 28), 
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
             fontsize=11, color='green')

# Add grid and legend
plt.grid(linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()