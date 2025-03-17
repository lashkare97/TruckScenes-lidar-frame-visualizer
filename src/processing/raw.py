import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

def color_by_height(pcd):
    """Applies color based on Z-height."""
    pts = np.asarray(pcd.points)
    z_vals = pts[:, 2]
    z_min, z_max = z_vals.min(), z_vals.max()
    colors = plt.get_cmap("viridis")((z_vals - z_min) / (z_max - z_min + 1e-8))
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    return pcd
