import matplotlib.pyplot as plt

y=[57,48,39,25,20,10]

countries = ['United States','China','Great Britain','Russia','Germany','Japan']
myexplode = [0.2, 0, 0, 0,0,0]

plt.pie(y,labels=countries,explode=myexplode)
#plt.legend()

plt.show()
