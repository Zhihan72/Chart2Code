import matplotlib.pyplot as plt
import numpy as np

# Define the years and investment data for each company
years = np.arange(2015, 2024)
company_a = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])
company_b = np.array([80, 100, 150, 180, 220, 250, 300, 350, 400])
company_c = np.array([60, 80, 100, 130, 150, 180, 220, 260, 300])
company_d = np.array([50, 60, 70, 90, 110, 140, 170, 200, 240])

companies = ["Company A", "Company B", "Company C", "Company D"]

# Plot setup
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the area chart using stackplot with a single color
ax.stackplot(years, company_a, company_b, company_c, company_d, labels=companies, colors=['#1f77b4'], alpha=0.8)

# Titles and labels
ax.set_title('Investment Growth of Tech Companies (2015-2023)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Investment (Millions USD)', fontsize=12)

# Set x-ticks for each year
ax.set_xticks(years)
ax.tick_params(axis='x', rotation=45)

# Add legend
ax.legend(loc='upper left', title='Companies', fontsize=10, title_fontsize='13')

# Annotations for data insight
ax.annotate('Company A R&D Surge', xy=(2020, 300), xytext=(2017, 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='darkorange')

ax.annotate('Company B Market Expansion', xy=(2022, 350), xytext=(2019, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='royalblue')

# Adding grid and enhancing readability
ax.grid(True, linestyle='--', alpha=0.6)

# Tight layout adjustment
plt.tight_layout()

# Display the plot
plt.show()