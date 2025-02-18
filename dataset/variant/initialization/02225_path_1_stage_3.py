import matplotlib.pyplot as plt

energy_share = [33, 25, 20, 12, 5, 3, 2]
colors = ['#2ca02c', '#8c564b', '#aec7e8', '#ffcc00', '#1f77b4', '#9467bd', '#ff7f0e']

plt.figure(figsize=(10, 8))
plt.pie(
    energy_share, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85
)

plt.show()