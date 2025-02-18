import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Average monthly steps counts (in thousands)
adults_steps = np.array([85, 90, 95, 100, 105, 110, 115, 110, 105, 100, 95, 90])
seniors_steps = np.array([50, 55, 60, 65, 70, 75, 80, 75, 70, 65, 60, 55])

# Create the plot
plt.figure(figsize=(14, 7))

# Plot lines for each remaining age group
plt.plot(months, adults_steps, label="Adults", color='tab:blue', linestyle='--', marker='s', linewidth=2)
plt.plot(months, seniors_steps, label="Seniors", color='tab:red', linestyle='-.', marker='^', linewidth=2)

# Highlight the month with the highest steps count for each remaining group
max_steps = {"Adults": 115, "Seniors": 80}
max_months = {"Adults": "Jul", "Seniors": "Jul"}
for group, steps in max_steps.items():
    plt.axvline(x=max_months[group], color='grey', linestyle=':', linewidth=1)
    plt.text(max_months[group], steps + 5, f'{group} Peak: {steps}K', fontsize=10, color='grey')

# Set chart title and labels
plt.title("Monthly Steps Count Analysis\nfor Different Age Groups - Year 2023", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Monthly Steps (in thousands)", fontsize=12)

# Add legend and grid
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate a notable trend change
plt.annotate('Drop in Activity', xy=("Sep", 70), xytext=("Jul", 80),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()