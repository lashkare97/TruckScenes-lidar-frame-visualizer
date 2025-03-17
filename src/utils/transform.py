import numpy as np

def get_transformation_matrix(entry):
    """Generates a 4x4 transformation matrix from translation and rotation."""
    t = np.array(entry["translation"])
    q = np.array(entry["rotation"])
    w, x, y, z = q
    R = np.array([
        [1 - 2*y**2 - 2*z**2, 2*x*y - 2*z*w, 2*x*z + 2*y*w],
        [2*x*y + 2*z*w, 1 - 2*x**2 - 2*z**2, 2*y*z - 2*x*w],
        [2*x*z - 2*y*w, 2*y*z + 2*x*w, 1 - 2*x**2 - 2*y**2],
    ])
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T
