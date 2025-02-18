import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visitors = [
    [110, 115, 145, 190, 290, 300, 440, 420, 270, 190, 140, 105],  # 2010 altered
    [115, 130, 150, 200, 295, 315, 455, 435, 280, 205, 155, 110],  # 2011 altered
    [112, 128, 158, 208, 308, 338, 468, 448, 298, 218, 168, 118],  # 2012 altered
    [118, 132, 165, 212, 318, 345, 475, 455, 305, 228, 172, 123],  # 2013 altered
    [122, 138, 169, 218, 319, 362, 487, 468, 322, 239, 178, 127],  # 2014 altered
    [128, 143, 172, 230, 335, 375, 505, 485, 335, 248, 183, 132],  # 2015 altered
    [133, 148, 177, 232, 332, 382, 508, 493, 345, 258, 192, 137],  # 2016 altered
    [137, 153, 182, 238, 336, 385, 515, 503, 350, 263, 197, 142],  # 2017 altered
    [143, 158, 188, 242, 342, 408, 528, 512, 362, 278, 202, 148],  # 2018 altered
    [147, 162, 193, 247, 349, 412, 535, 527, 375, 295, 208, 153],  # 2019 altered
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