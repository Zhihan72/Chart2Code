import matplotlib.pyplot as plt
import numpy as np

hobbies = [
    "Photography", 
    "Writing", 
    "Crafting", 
    "Music", 
    "Gardening", 
    "Reading", 
    "Cooking/Baking", 
    "Gaming", 
    "Exercise"
]

percentages = [5, 8, 10, 15, 25, 30, 35, 40, 45]

# Apply a single color consistently across all data groups
single_color = 'skyblue'

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.bar(hobbies, percentages, color=single_color, edgecolor='black')
ax.set_ylim(0, 50)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
plt.show()