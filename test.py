import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import sys

# monkey patches visualization and provides helpers to load geometries
sys.path.append('..')
import open3d_tutorial as o3dtut
# change to True if you want to interact with the visualization windows
o3dtut.interactive = False

print("Read Container Image")
color_raw = o3d.io.read_image("/home/abel/pang_tut/container.jpg")
plt.title("Image")
plt.imshow(color_raw)
plt.show()
