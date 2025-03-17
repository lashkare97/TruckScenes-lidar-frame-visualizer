import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

def cluster_and_color(pcd):
    """Applies DBSCAN clustering and colors the clusters."""
    labels = np.array(pcd.cluster_dbscan(eps=0.6, min_points=15, print_progress=False))
    max_label = labels.max()
    cmap = plt.get_cmap("tab20")
    colors = cmap((labels % 20) / 20)
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    
    geometries = [pcd]
    for i in range(max_label + 1):
        cluster = pcd.select_by_index(np.where(labels == i)[0])
        box = cluster.get_axis_aligned_bounding_box()
        box.color = (1, 0, 0)
        geometries.append(box)
    return geometries
