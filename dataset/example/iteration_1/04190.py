import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Growth Trends in Various Programming Languages' Popularity Over the Decade
# Data is based on the hypothetical usage/popularity index (higher is better).

# Years of observation
years = np.arange(2010, 2021)

# Popularity indices by language
python_popularity = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
javascript_popularity = np.array([40, 42, 44, 46, 48, 50, 52, 55, 57, 59, 62])
java_popularity = np.array([50, 52, 54, 56, 58, 59, 60, 61, 62, 63, 64])
csharp_popularity = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
ruby_popularity = np.array([20, 22, 24, 26, 28, 30, 32, 34, 35, 36, 38])

# Create the line plot with multiple subplots to differentiate trends and anomalies
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Main Line Plot
axes[0].plot(years, python_popularity, label='Python', color='blue', marker='o', linestyle='-', linewidth=2)
axes[0].plot(years, javascript_popularity, label='JavaScript', color='green', marker='s', linestyle='--', linewidth=2)
axes[0].plot(years, java_popularity, label='Java', color='red', marker='^', linestyle='-.', linewidth=2)
axes[0].plot(years, csharp_popularity, label='C#', color='purple', marker='D', linestyle=':', linewidth=2)
axes[0].plot(years, ruby_popularity, label='Ruby', color='brown', marker='*', linestyle='-', linewidth=2)

# Adding titles and labels
axes[0].set_title('Popularity Trends of Various Programming Languages (2010-2020)', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Popularity Index', fontsize=12)

# Add a legend
axes[0].legend(loc='upper left', fontsize=10)

# Grid Lines
axes[0].grid(True, linestyle='--', alpha=0.6)

# In-depth look at the Year-on-Year Difference to highlight growth rates (Subplot)
# Calculating differences year-on-year
python_diff = np.diff(python_popularity, prepend=python_popularity[0])
javascript_diff = np.diff(javascript_popularity, prepend=javascript_popularity[0])
java_diff = np.diff(java_popularity, prepend=java_popularity[0])
csharp_diff = np.diff(csharp_popularity, prepend=csharp_popularity[0])
ruby_diff = np.diff(ruby_popularity,prepend=ruby_popularity[0])

# Plotting year-on-year difference
axes[1].bar(years, python_diff, label='Python', color='blue', alpha=0.6)
axes[1].bar(years, javascript_diff, label='JavaScript', color='green', alpha=0.6, bottom=python_diff)
axes[1].bar(years, java_diff, label='Java', color='red', alpha=0.6, bottom=python_diff + javascript_diff)
axes[1].bar(years, csharp_diff, label='C#', color='purple', alpha=0.6, bottom=python_diff + javascript_diff + java_diff)
axes[1].bar(years, ruby_diff, label='Ruby', color='brown', alpha=0.6, bottom=python_diff + javascript_diff + java_diff + csharp_diff)

# Title and labels for the subplot
axes[1].set_title('Year-On-Year Changes in Popularity Index (2010-2020)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Change in Popularity Index', fontsize=12)

# Grid Lines
axes[1].grid(True, linestyle='--', alpha=0.6)

# Adding a legend
axes[1].legend(loc='upper left', fontsize=10, title="Languages", title_fontsize='13')

# Adjust layout to prevent text overlap
plt.tight_layout()

# Display the plot
plt.show()