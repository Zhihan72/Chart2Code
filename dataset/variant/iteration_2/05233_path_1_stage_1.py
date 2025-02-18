import matplotlib.pyplot as plt

# Define the initiatives and their respective investment percentages
initiatives = ['Disaster Management', 'Wellbeing', 'Crisis Support', 'Pure Water', 'Eco Conservation']
investment_percentages = [30, 25, 20, 15, 10]

# Define custom colors for each initiative
colors = ['#FA8072', '#20B2AA', '#FFD700', '#4682B4', '#9ACD32']

# Highlight the 'Disaster Management' sector by exploding it slightly
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(
    investment_percentages, 
    labels=initiatives, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    wedgeprops={'edgecolor': 'black'}
)

# Customize text appearance
for text in texts:
    text.set_fontsize(12)
    text.set_weight('bold')
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_weight('bold')
    autotext.set_color('black')

# Add a title to the pie chart
plt.title("Charitable Group's Fund Allocation\nin Social Efforts (2023)", fontsize=16, fontweight='bold', pad=20)

# Add a legend to the chart
plt.legend(wedges, initiatives, title="Focus Areas", loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()