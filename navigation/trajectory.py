import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd 

# ANIMATION FUNCTION
def func(num, dataSet, line):
    # NOTE: there is no .set_data() for 3 dim data...
    line.set_data(dataSet[0:2, :num])    
    line.set_3d_properties(dataSet[2, :num])    
    return line
 
 
# THE DATA POINTS
# t = np.arange(0,20,0.2) # This would be the z-axis ('t' means time here)
# x = np.cos(t)-1
# y = 1/2*(np.cos(2*t)-1)
df = pd.read_csv('/Users/vrutikshah/Documents/Work Related/QHack-EyeQ/demo1_dataset/odometry.csv')
dataSet = np.array([df[' x'], df[' y'], df[' z']])
# dataSet = np.array([df[' x'], df[' y']])
numDataPoints = len(df[' z'])
 
# GET SOME MATPLOTLIB OBJECTS
fig = plt.figure()
ax = Axes3D(fig)
 
# NOTE: Can't pass empty arrays into 3d version of plot()
line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] # For line plot
 
# AXES PROPERTIES]
# ax.set_xlim3d([limit0, limit1])
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_zlabel('time')
ax.set_title('Trajectory of electron for E vector along [120]')
 
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line), interval=1, blit=False)
line_ani.save(r'AnimationNew.mp4')

plt.show()