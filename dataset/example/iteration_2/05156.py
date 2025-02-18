import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart visualizes the growth of different programming languages in terms of search interest over the past decade.
# Each line represents the search interest percentage for a specific language on a leading search engine.

# Years for x-axis
years = np.arange(2010, 2021)

# Search interest for different languages (fictional data, % of total search interest)
python_interest = [10, 15, 20, 30, 40, 50, 60, 70, 75, 80, 85]
java_interest = [40, 38, 35, 33, 30, 28, 25, 23, 22, 20, 18]
javascript_interest = [20, 22, 25, 30, 35, 40, 45, 48, 50, 53, 55]
csharp_interest = [15, 17, 19, 17, 15, 14, 12, 11, 12, 13, 12]
ruby_interest = [15, 13, 11, 10, 9, 8, 7, 6, 6, 6, 5]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the line chart for each programming language
ax.plot(years, python_interest, marker='o', linestyle='-', color='blue', linewidth=2, label='Python')
ax.plot(years, java_interest, marker='s', linestyle='-', color='green', linewidth=2, label='Java')
ax.plot(years, javascript_interest, marker='^', linestyle='-', color='orange', linewidth=2, label='JavaScript')
ax.plot(years, csharp_interest, marker='d', linestyle='-', color='purple', linewidth=2, label='C#')
ax.plot(years, ruby_interest, marker='x', linestyle='-', color='red', linewidth=2, label='Ruby')

# Setting title and labels
ax.set_title('Search Interest in Programming Languages (2010-2020)', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Search Interest (%)', fontsize=14)

# Adding a legend to identify languages
ax.legend(loc='upper left', fontsize=12, title='Languages', title_fontsize=14)

# Enable grid for easier value estimation
ax.grid(True, linestyle='--', alpha=0.7)

# Annotating key points in the data
ax.annotate('Python rises to preeminence', xy=(2018, 75), xytext=(2015, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=12, color='blue')
ax.annotate('JavaScript’s steady growth', xy=(2010, 20), xytext=(2014, 30),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=12, color='orange')

# Ensuring x-tick labels are readable by rotating them
plt.xticks(years, rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()