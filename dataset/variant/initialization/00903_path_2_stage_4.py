import matplotlib.pyplot as plt
import numpy as np

countries = [
    "India", "Canada", "China", "United States", "France",
    "Germany", "Australia", "United Kingdom", "Japan", "South Korea",
    "Atlantis", "Elbonia"
]
education_percentages = [
    12.0, 28.0, 20.0, 38.0, 26.0,
    31.0, 30.0, 29.0, 36.0, 34.0,
    45.0, 15.0
]
population_millions = [
    1393.0, 38.0, 1412.0, 332.0, 67.5,
    83.2, 25.7, 67.2, 125.8, 51.7,
    5.0, 3.5
]

# Calculate degree holders in millions
degree_holders_millions = [pop * (pct / 100) for pop, pct in zip(population_millions, education_percentages)]

colors = plt.cm.viridis(np.linspace(0, 1, len(countries)))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

# Plot pie chart
axes[0].pie(degree_holders_millions, labels=countries, autopct='%1.1f%%', startangle=140, colors=colors)
axes[0].set_title('Bachelor\'s Degree Rates\n(Estimated 2022)', fontsize=16, pad=20)

# Plot horizontal bar chart
bars = axes[1].barh(countries, education_percentages, color=colors, height=0.6)
axes[1].set_title('Countries Having Higher Education\nStatistics 2022', fontsize=16, pad=20)
axes[1].set_xlabel('Education Level (%)', fontsize=12)
axes[1].invert_yaxis()

for bar in bars:
    width = bar.get_width()
    axes[1].text(width + 0.5, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', ha='left', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(wspace=0.3)

plt.show()