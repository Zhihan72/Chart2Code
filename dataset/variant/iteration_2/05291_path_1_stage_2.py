import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visitors = [
    [105, 120, 150, 200, 300, 320, 450, 430, 280, 200, 150, 110],  # 2010
    [108, 125, 155, 205, 305, 330, 460, 440, 290, 210, 160, 115],  # 2011
    [110, 130, 160, 210, 310, 340, 470, 450, 300, 220, 170, 120],  # 2012
    [115, 135, 165, 215, 315, 350, 480, 460, 310, 230, 175, 125],  # 2013
    [120, 140, 170, 220, 320, 360, 490, 470, 320, 240, 180, 130],  # 2014
    [125, 145, 175, 225, 325, 370, 500, 480, 330, 250, 185, 135],  # 2015
    [130, 150, 180, 230, 330, 380, 510, 490, 340, 260, 190, 140],  # 2016
    [135, 155, 185, 235, 335, 390, 520, 500, 350, 270, 195, 145],  # 2017
    [140, 160, 190, 240, 340, 400, 530, 510, 360, 280, 200, 150],  # 2018
    [145, 165, 195, 245, 345, 410, 540, 520, 370, 290, 205, 155],  # 2019
]

new_colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00', 
              '#FFFF33', '#A65628', '#F781BF', '#999999', '#CE93D8']  # New color palette

fig, ax = plt.subplots(figsize=(14, 8))

for i, year in enumerate(years):
    ax.plot(months, visitors[i], label=f"Year {str(year)}", marker='o', color=new_colors[i])

ax.set_title("Visitor Statistics Across Seasons\nPark Summary Over the Years", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Calendar Months', fontsize=12)
ax.set_ylabel('Visitor Count', fontsize=12)

ax.legend(title="Année", title_fontsize='12', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()