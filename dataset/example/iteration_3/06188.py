import matplotlib.pyplot as plt
import numpy as np

# Backstory: The following chart showcases the evolution of natural diet preferences within a community over a decade (2025-2035).
# This can include how different dietary sources (e.g., fruits, vegetables, grains, dairy, proteins) have changed popularity.

# Define the years from 2025 to 2035
years = np.arange(2025, 2036)

# Diet preference data in arbitrary units
fruits = [20, 22, 25, 27, 29, 31, 33, 35, 37, 40, 42]
vegetables = [15, 16, 18, 19, 20, 23, 24, 25, 26, 28, 30]
grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dairy = [25, 24, 23, 22, 21, 21, 20, 19, 18, 17, 17]
proteins = [30, 28, 27, 25, 24, 22, 21, 20, 19, 18, 17]

# Create the stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, fruits, vegetables, grains, dairy, proteins, 
              labels=['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Proteins'], 
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700'], alpha=0.8)

# Title and axis labels
plt.title('Evolution of Dietary Preferences (2025-2035)\nCommunity Nutrition Trends', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, fontweight='bold', color='darkslategray')
plt.ylabel('Diet Composition (Arbitrary Units)', fontsize=12, fontweight='bold', color='darkslategray')

# Adding a legend outside the main plot area
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Dietary Sources', fontsize=10)

# Grid for better readability
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Annotating significant changes in dietary trends
annotations = {
    2027: 'Increased Vegetable Consumption',
    2030: 'Popularity Boost of Fruits',
    2033: 'Dairy Consumption Decline'
}

for year, text in annotations.items():
    total_amount = sum([fruits[year-2025], vegetables[year-2025], grains[year-2025], dairy[year-2025], proteins[year-2025]])
    plt.annotate(text, xy=(year, total_amount), xytext=(year, total_amount + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10, ha='center', color='darkred', backgroundcolor='white')

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Show plot
plt.show()