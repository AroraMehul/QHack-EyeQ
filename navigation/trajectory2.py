import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML
from celluloid import Camera
# %matplotlib inline

# Animate a single trajectory
pick_traj = 5      # Select a trajectory to simulate

# Set up the graph using Matplotlib
fig, ax = plt.subplots(figsize=(8,3))
ax.set(xlim=(-100, 3100), ylim=(-10, 810))
ax.set_ylabel('Height/m', fontsize=15)
ax.set_xlabel('Range/m', fontsize=15)
ax.get_xaxis().set_label_coords(0.5, 0.12)

# Initiate camera
camera = Camera(fig)

# Create individual frames
for j in range(1,traj_X.shape[1]+1):
    
    # Projectile's trajectory
    x = traj_X[pick_traj][0:j]
    y = traj_Y[pick_traj][0:j]
    
    # Show Projectile's location
    ax.plot(x[-1], y[-1], marker='o', markersize=12, markeredgecolor='r', markerfacecolor='r')
    
    # Show Projectile's trajectory
    ax.plot(x, y, color='b', lw=2, linestyle='--')
    
    # Capture frame
    camera.snap()

# Create animation
anim = camera.animate(interval = 40, repeat = True, repeat_delay = 500)

# Inline display
HTML(anim.to_html5_video())