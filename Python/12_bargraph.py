import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y1=[57,48,39,25,20,10]
y2=[28,30,21,25,18,16]

countries = ['United States','China','Great Britain','Russia','Germany','Japan']

plt.bar(x-0.2, y1, width=0.40,color="red")
plt.bar(x+0.2, y2, width=0.40,color="green")
plt.xticks(x,countries)

medals = ['Gold medal','Silver medal']
plt.title('Bar graph medals tally')
plt.xlabel('Countries')
plt.ylabel('Medals')
plt.legend(medals)
plt.show()
