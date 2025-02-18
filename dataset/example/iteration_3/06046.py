import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring the Growth of Two Tech Giants (2000-2020)

# Define the years
years = np.arange(2000, 2021)

# Data for number of users (in millions)
company_a_users = np.array([5, 10, 18, 30, 45, 63, 85, 110, 139, 171, 205, 243, 284, 328, 375, 425, 478, 534, 593, 655, 720])
company_b_users = np.array([2, 4, 9, 16, 26, 40, 58, 80, 106, 136, 170, 208, 250, 296, 346, 400, 458, 520, 586, 656, 730])

# Create the figure and the subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the data
ax1.plot(years, company_a_users, label='Company A Users', marker='o', linestyle='-', color='royalblue', linewidth=2, markersize=6)
ax1.plot(years, company_b_users, label='Company B Users', marker='^', linestyle='-', color='tomato', linewidth=2, markersize=6)

# Highlight significant milestones
ax1.annotate('Company A hits 100M users', xy=(2007, 100), xytext=(2003, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, fontweight='bold', color='darkblue')

ax1.annotate('Company B hits 100M users', xy=(2008, 100), xytext=(2005, 150),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=10, fontweight='bold', color='darkred')

# Highlight max users reached in 2020
ax1.axvline(x=2020, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax1.text(2021, 750, '2020 Peak Users', rotation=90, verticalalignment='center', fontsize=10, color='gray')

# Set chart title and labels
ax1.set_title("Rise of Tech Giants: Number of Users Growth (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Number of Users (in Millions)", fontsize=12)

# Add a legend
ax1.legend(loc='upper left', fontsize=10, title="Company", frameon=True)

# Add grid lines
ax1.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()