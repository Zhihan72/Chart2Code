import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = list(range(2000, 2021))

# Hypothetical average annual temperatures for Atlantis and El Dorado
temp_atlantis = [15.3, 15.4, 15.8, 15.7, 16.0, 16.3, 16.4, 16.6, 16.7, 16.8, 17.0, 17.2, 17.3, 17.5, 17.6, 17.8, 18.0, 18.2, 18.3, 18.5, 18.7]
temp_el_dorado = [17.5, 17.6, 17.8, 17.8, 18.0, 18.1, 18.3, 18.5, 18.6, 18.8, 19.0, 19.1, 19.3, 19.4, 19.6, 19.7, 19.9, 20.0, 20.2, 20.4, 20.5]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the temperature lines for Atlantis and El Dorado
ax.plot(years, temp_atlantis, label='Atlantis', marker='o', linestyle='-', color='blue', linewidth=2)
ax.plot(years, temp_el_dorado, label='El Dorado', marker='s', linestyle='--', color='red', linewidth=2)

# Title and labels
plt.title('Average Annual Temperature Changes in Atlantis and El Dorado (2000-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)

# Adding a legend
plt.legend(title='Cities', fontsize=10)

# Adding grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Adding data points annotation
for i, (atl_temp, eld_temp) in enumerate(zip(temp_atlantis, temp_el_dorado)):
    ax.text(years[i], atl_temp + 0.1, f'{atl_temp:.1f}', ha='center', fontsize=9, color='blue')
    ax.text(years[i], eld_temp + 0.1, f'{eld_temp:.1f}', ha='center', fontsize=9, color='red')

# Using tight layout for more space-efficient display
plt.tight_layout()

# Display the plot
plt.show()