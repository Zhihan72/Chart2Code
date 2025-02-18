import matplotlib.pyplot as plt
import numpy as np

sectors = ['Res', 'Agri', 'Indus', 'Rec', 'Com']
# Swapping the usage values for 'Res' and 'Indus', and 'Agri' and 'Com'
water_usage = np.array([50, 70, 120, 30, 80])
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    colors=colors,  
    startangle=45
)

plt.setp(autotexts, size=10, color='black', weight='light')

ax.set_title("Water Use in AquaRidge", fontsize=14, fontweight='light', loc='right')

ax.legend(wedges, sectors, title="Sector", loc="upper right", fontsize=8)

ax.grid(linewidth=0.5, linestyle='--', color='gray')

plt.show()