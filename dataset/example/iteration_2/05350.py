import matplotlib.pyplot as plt
import numpy as np

# Let's create a backstory: We will visualize the popularity of different programming languages over the last decade based on the number of GitHub repositories created per year.

# Define years
years = np.arange(2013, 2023)

# Define number of repos for different languages (data is arbitrary but realistic)
languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
repos_data = np.array([
    [150, 165, 180, 200, 220, 250, 300, 350, 400, 450],  # Python
    [100, 120, 140, 160, 180, 200, 220, 240, 260, 280],  # JavaScript
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170],    # Java
    [60, 70, 80, 85, 90, 100, 110, 120, 125, 130],       # C++
    [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]             # Ruby
])

# Create the bar plot
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width and positions
bar_width = 0.15
positions = np.arange(len(years))

# Create bars for each language
for i, language in enumerate(languages):
    ax.bar(positions + i * bar_width, repos_data[i], width=bar_width, label=language)

# Adding context to our plot
ax.set_title('Popularity of Programming Languages on GitHub (2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Number of Repositories', fontsize=14)
ax.set_xticks(positions + bar_width * (len(languages) / 2))
ax.set_xticklabels(years, rotation=45)
ax.legend(title='Languages', fontsize=12)

# Annotating the highest repository count for each language
for i, repos in enumerate(repos_data):
    max_repo = max(repos)
    year_max = years[repos.argmax()]
    ax.annotate(f'{max_repo}', 
                xy=(year_max - 2013 + i * bar_width, max_repo), 
                xycoords='data', 
                xytext=(0, 5), 
                textcoords='offset points', 
                ha='center', 
                fontsize=9,
                fontstyle='italic')

# Display grid lines for better readability
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlapping
plt.tight_layout()

# Show the bar chart
plt.show()