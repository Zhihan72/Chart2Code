import matplotlib.pyplot as plt
import numpy as np

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

brightness_bins = ['0-2', '2-4', '4-6', '6-8', '8-10']
stars_jan = [30, 45, 50, 35, 20]
stars_jun = [20, 30, 55, 40, 25]
stars_dec = [25, 35, 45, 50, 30]

fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Plotting the subplots in the new order: Dec, Jan, Jun
axs[0].bar(brightness_bins, stars_dec, color='lightcoral', edgecolor='black')
axs[0].set_title('Star Brightness in Dec')
axs[0].set_xlabel('Brightness Range (Magnitude)')
axs[0].set_ylabel('Number of Stars')
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

axs[1].bar(brightness_bins, stars_jan, color='lightskyblue', edgecolor='black')
axs[1].set_title('Star Brightness in Jan')
axs[1].set_xlabel('Brightness Range (Magnitude)')
axs[1].grid(axis='y', linestyle='--', alpha=0.7)

axs[2].bar(brightness_bins, stars_jun, color='lightgreen', edgecolor='black')
axs[2].set_title('Star Brightness in Jun')
axs[2].set_xlabel('Brightness Range (Magnitude)')
axs[2].grid(axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Brightness of Stars in Different Constellations:\nObservation Data for Selected Months', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()