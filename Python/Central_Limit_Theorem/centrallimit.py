import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io

def capture_frame():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return Image.open(buf)

detail = 25
runs = 3
z = 10

frames_1 = [] 

x = np.linspace(0, z, num=detail)
y = np.full((len(x)), 1.0)

plt.title("Initial Function: Unit Step")
plt.stem(x, y)
frames_1.append(capture_frame())
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, 10, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.xlim([0,10])
    plt.stem(x, y)
    frames_1.append(capture_frame())
    plt.show()

frames_2 = [] 

x = np.linspace(0, 10, num=detail)
y = np.random.rand(detail)

plt.title("Initial Function: Random Data Points")
plt.stem(x, y)
frames_2.append(capture_frame())
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, z, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.stem(x, y)
    frames_2.append(capture_frame())
    plt.show()

frames_3 = [] 

x = np.linspace(0, 10, num=detail)
y = np.abs(np.sin(x)) * np.full((len(x)), 1.0)

plt.title("Initial Function: Absolute Value Sinusoid")
plt.stem(x, y)
frames_3.append(capture_frame())
plt.show()

for r in range(0, runs):
    y = np.convolve(y, y)
    x = np.linspace(0, 10, num=len(y))
    plt.title("Convolution = " + str(r + 1))
    plt.xlim([0,10])
    plt.stem(x, y)
    frames_3.append(capture_frame())
    plt.show()

# Let's save the .gif
all_frames = frames_1 + frames_2 + frames_3
all_frames[0].save('all_cases.gif', save_all=True, append_images=all_frames[1:], duration=1000, loop=0)