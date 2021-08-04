from matplotlib import pyplot as plt

x = [10, 25, 100, 70, 76, 100, 200, 900, 15]
y = [15, 28, 1150, 72, 73, 150, 130, 500, 22]

plt.scatter(x,y, label = ' some munbers')
plt.xlabel(' X- Axis')
plt.ylabel(' Y- Axis')
plt.title ('  Rondom scatter numbers ')
plt.legend()
plt.show()