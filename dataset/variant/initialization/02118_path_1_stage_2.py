import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'Rust', 'Ruby', 'JavaScript', 'C++', 'PHP', 'Go']
usage_percentages = [16, 29, 4, 7, 24, 12, 3, 5]
colors = ['#99FF99', '#FF9999', '#98FB98', '#FFD700', '#66B3FF', '#FFCC99', '#C2C2F0', '#FFA07A']

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(
    usage_percentages, 
    labels=languages, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=(0, 0.1, 0, 0, 0, 0, 0, 0), 
    shadow=True, 
    wedgeprops=dict(width=0.3)
)

ax.axis('equal')
ax.set_title('Open Source Coding in 2025\nLanguage Popularity', fontsize=15, fontweight='bold', pad=20)
ax.legend(languages, title="Top Languages", loc='upper right', bbox_to_anchor=(1.2, 1))

plt.tight_layout()
plt.show()