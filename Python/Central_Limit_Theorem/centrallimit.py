import numpy as np
import matplotlib.pyplot as plt

detail = 25
runs = 3
z = 10

x = np.linspace(0, 10, num=detail)
y = np.random.rand(detail)

plt.title("Initial Function")
plt.stem(x, y)
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, 10, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.xlim([0,10])
    plt.stem(x, y)
    plt.show()

x = np.linspace(0, z, num=detail)
y = np.full((len(x)), 1.0)

plt.title("Initial Function")
plt.stem(x, y)
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, z, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.stem(x, y)
    plt.show()
    
x = np.linspace(0, 10, num=detail)
y = np.abs(np.sin(x)) * np.full((len(x)), 1.0)

plt.title("Initial Function")
plt.stem(x, y)
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, 10, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.xlim([0,10])
    plt.stem(x, y)
    plt.show()