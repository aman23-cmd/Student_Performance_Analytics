"""
Data Storytelling: Highlighting trends in performance
"""

import matplotlib.pyplot as plt

students = ['Sem1', 'Sem2', 'Sem3']
scores = [72, 80, 88]

plt.plot(students, scores, marker='o', linestyle='-', color='purple')
plt.title("Student Progress Over Semesters")
plt.xlabel("Semester")
plt.ylabel("Average Score")

# Annotate values
for i, txt in enumerate(scores):
    plt.annotate(txt, (students[i], scores[i]))

plt.grid(True)
plt.show()
