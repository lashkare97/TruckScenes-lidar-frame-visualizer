import numpy as np
import open3d as o3d

def simulate_semantic_colors(pcd):
    """Assigns colors based on height thresholds for a pseudo-semantic effect."""
    pts = np.asarray(pcd.points)
    colors = np.zeros((len(pts), 3))
    for i in range(len(pts)):
        z = pts[i, 2]
        if z < 0.3:
            colors[i] = [0.4, 0.4, 0.4]  # Road (gray)
        elif z < 1.2:
            colors[i] = [1.0, 0.0, 0.0]  # Vehicle (red)
        elif z < 2.5:
            colors[i] = [1.0, 1.0, 0.0]  # Pedestrian (yellow)
        elif z < 4.0:
            colors[i] = [0.0, 1.0, 0.0]  # Vegetation (green)
        else:
            colors[i] = [0.5, 0.0, 0.5]  # Building (purple)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    return pcd
