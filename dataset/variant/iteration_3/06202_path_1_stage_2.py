import matplotlib.pyplot as plt
import numpy as np

# Data Construction
years = np.arange(2000, 2021)
avg_temp_greenland = np.array([-15, -14.8, -14.7, -14.5, -14.3, -14.1, -13.9, -13.5, 
                               -13.0, -12.8, -12.5, -12.2, -12.1, -11.9, -11.5, -11.2, 
                               -10.9, -10.5, -10.3, -10.1, -9.8])

# Creating the Plot
plt.figure(figsize=(14, 8))

# Line Plot
plt.plot(years, avg_temp_greenland, color='#1f77b4', linestyle='-', linewidth=2, marker='o')

# Consistent color for highlighting
plt.axhline(y=-14, color='#1f77b4', linestyle='--', alpha=0.7)
plt.axvspan(2015, 2020, color='#1f77b4', alpha=0.1)

for notable_year in [2004, 2010, 2016]:
    plt.annotate('', xy=(notable_year, avg_temp_greenland[notable_year - 2000]), 
                 xytext=(notable_year, avg_temp_greenland[notable_year - 2000] + 0.5),
                 arrowprops=dict(facecolor='#1f77b4', arrowstyle='->'))

# Adjust Layout
plt.tight_layout()

# Display the Plot
plt.show()