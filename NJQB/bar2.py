import matplotlib.pyplot as plt
import numpy as np

w = 0.4
x = ["CS", "IT", "AI&DS", "EXTC", "Chemical"]
boys = [100, 40, 60, 240, 300]
girls = [200, 70, 30, 120, 15]
bar1 = np.arange(len(x))
bar2 = [i + w for i in bar1]

plt.bar(bar1, boys, w, label="boys")
plt.bar(bar2, girls, w, label="girls")
plt.xlabel("Courses")
plt.ylabel("Students")
plt.title("Student vs Courses")
plt.xticks(bar1 + w/2, x)
plt.legend()
plt.tight_layout()
plt.show()