import matplotlib.pyplot as plt
import numpy as np

# Data input creation
institutions = ['Universities', 'Tech Companies', 'Hospitals', 'Government Offices', 'Research Institutions']
categories = ['Social Media', 'Work/Emails', 'Streaming', 'Research', 'Shopping']

# Percentage of internet activity by institution
data_by_institution = {
    "Universities": [40, 20, 15, 20, 5],
    "Tech Companies": [10, 50, 10, 25, 5],
    "Hospitals": [5, 40, 5, 35, 15],
    "Government Offices": [5, 45, 5, 35, 10],
    "Research Institutions": [10, 15, 5, 60, 10]
}

# Single color for the pie chart
color = '#66b3ff'  # Use one consistent color for all pie segments

# Custom function to format the percentage labels in the pie chart
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{:.1f}%\n({:d})'.format(pct, val)
    return my_autopct

def plot_pie_chart(data, institution, categories, color):
    fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(aspect="equal"))
    
    # Create the pie chart with a single color for all segments
    wedges, texts, autotexts = ax.pie(
        data,
        labels=categories,
        autopct=make_autopct(data),
        startangle=140,
        colors=[color] * len(data),  # Apply the single color across all segments
        pctdistance=0.8,
        wedgeprops=dict(width=0.3, edgecolor='w', linewidth=0.5),
        textprops=dict(color='white', fontsize=9, fontweight='bold')
    )
    
    # Draw a white circle at the center to create a donut look
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Add a title and ensure the pie is round
    ax.set_title(f"{institution}:\nInternet Usage Breakdown", fontsize=14, fontweight='bold')
    
    # Add a legend
    ax.legend(wedges, categories, title="Usage Category", loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize='small')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()

# Plot each institution's data
for institution, data in data_by_institution.items():
    plot_pie_chart(data, institution, categories, color)