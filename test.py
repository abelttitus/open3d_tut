import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import sys



mesh = o3d.io.read_traingle_mesh("/home/abel/open3d_tut/bathtub_0154.ply")
o3d.visualization.draw_geometries([mesh])
