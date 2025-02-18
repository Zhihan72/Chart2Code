import matplotlib.pyplot as plt

languages = ['Rust', 'Python', 'Java', 'JavaScript', 'C++', 'Go', 'Ruby', 'PHP']
usage_percentages = [4, 29, 16, 24, 12, 5, 7, 3]

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(
    usage_percentages, 
    labels=languages, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#66B3FF'] * len(languages),  # Single consistent color applied
    explode=(0.1, 0.1, 0, 0.1, 0, 0, 0.1, 0), 
    wedgeprops=dict(width=0.3)
)

ax.axis('equal')
ax.set_title('Open Source Coding in 2025\nLanguage Popularity', fontsize=15, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()